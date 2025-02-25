import os
import logging
from flask import Flask, request, jsonify, render_template, send_file
from backend.generator import generate_code

app = Flask(__name__, template_folder="../frontend")

SAVE_PATH = "../generated_code/generated_code.py"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    logging.info(f"📥 Получен запрос: {data}")

    prompt = data.get("prompt", "Напиши простой скрипт")
    language = data.get("language", "python")

    code = generate_code(prompt, language)

    with open(SAVE_PATH, "w") as f:
        f.write(code)

    logging.info(f"✅ Код сохранён в {SAVE_PATH}")

    return jsonify({
        "message": "Код сгенерирован и сохранён.",
        "optimized_code": code,
        "download_url": "/download"
    })

@app.route("/download", methods=["GET"])
def download():
    if os.path.exists(SAVE_PATH):
        return send_file(SAVE_PATH, as_attachment=True)
    return jsonify({"error": "Файл не найден!"}), 404

if __name__ == "__main__":
    app.run(debug=True)
