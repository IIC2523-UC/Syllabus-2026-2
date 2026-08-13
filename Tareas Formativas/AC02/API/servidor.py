from sys import argv
from typing import Any
from flask import Flask, jsonify, request


class RegistroNotas:
    def __init__(self) -> None:
        self.evaluaciones: list[str] = []
        self.notas: list[dict] = []

    def crear_evaluacion(self, evaluacion: str) -> None:
        if evaluacion not in self.evaluaciones:
            self.evaluaciones.append(evaluacion)
        return None

    def registrar_nota(self, evaluacion: str, alumno: str, nota: float) -> int:
        if evaluacion not in self.evaluaciones:
            raise ValueError(f"La evaluacion '{evaluacion}' no existe")

        self.notas.append(
            {
                "evaluacion": evaluacion,
                "alumno": alumno,
                "nota": float(nota),
            }
        )

        return sum(1 for n in self.notas if n["alumno"] == alumno)

    def obtener_nota(self, alumno: str, evaluacion: str) -> float | None:
        for registro in self.notas:
            if registro["alumno"] == alumno and registro["evaluacion"] == evaluacion:
                return registro["nota"]
        return None

    def listar_notas_alumno(self, alumno: str) -> list[tuple]:
        return [
            (registro["evaluacion"], registro["nota"])
            for registro in self.notas
            if registro["alumno"] == alumno
        ]

    def promedio_evaluacion(self, evaluacion: str) -> float | None:
        notas_eval = [
            registro["nota"]
            for registro in self.notas
            if registro["evaluacion"] == evaluacion
        ]

        if not notas_eval:
            return None

        return sum(notas_eval) / len(notas_eval)

    def stats_avanzadas(self, evaluacion: str) -> dict | None:
        notas_eval = sorted(
            registro["nota"]
            for registro in self.notas
            if registro["evaluacion"] == evaluacion
        )

        if not notas_eval:
            return None

        return {
            "mediana": _percentil(notas_eval, 0.5),
            "quartil": _percentil(notas_eval, 0.25),
            "minimo": min(notas_eval),
            "maximo": max(notas_eval),
        }


def _percentil(valores_ordenados: list[float], p: float) -> float:
    if len(valores_ordenados) == 1:
        return valores_ordenados[0]

    pos = (len(valores_ordenados) - 1) * p
    abajo = int(pos)
    arriba = min(abajo + 1, len(valores_ordenados) - 1)
    fraccion = pos - abajo
    return valores_ordenados[abajo] + (valores_ordenados[arriba] - valores_ordenados[abajo]) * fraccion


app = Flask(__name__)
registro = RegistroNotas()


@app.route("/evaluaciones", methods=["POST"])
def crear_evaluacion() -> Any:
    data = request.get_json(force=True)
    evaluacion = data.get("evaluacion")
    if not evaluacion:
        return jsonify({"error": "Falta 'evaluacion'"}), 400

    retorno = registro.crear_evaluacion(evaluacion)
    return jsonify(retorno)


@app.route("/notas", methods=["POST"])
def registrar_nota() -> Any:
    data = request.get_json(force=True)
    evaluacion = data.get("evaluacion")
    alumno = data.get("alumno")
    nota = data.get("nota")

    if not evaluacion or not alumno or nota is None:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    try:
        cantidad = registro.registrar_nota(evaluacion, alumno, nota)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    return jsonify(cantidad)


@app.route("/nota", methods=["GET"])
def obtener_nota() -> Any:
    alumno = request.args.get("alumno")
    evaluacion = request.args.get("evaluacion")

    if not alumno or not evaluacion:
        return jsonify({"error": "Faltan parametros"}), 400

    return jsonify(registro.obtener_nota(alumno, evaluacion))


@app.route("/notas/<alumno>", methods=["GET"])
def listar_notas(alumno: str) -> Any:
    return jsonify(registro.listar_notas_alumno(alumno))


@app.route("/promedio/<evaluacion>", methods=["GET"])
def promedio(evaluacion: str) -> Any:
    return jsonify(registro.promedio_evaluacion(evaluacion))


@app.route("/stats/<evaluacion>", methods=["GET"])
def stats(evaluacion: str) -> Any:
    return jsonify(registro.stats_avanzadas(evaluacion))


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Uso: python3 servidor.py <puerto>")
        exit(1)

    puerto = int(argv[1])
    app.run(host="127.0.0.1", port=puerto, debug=True)
