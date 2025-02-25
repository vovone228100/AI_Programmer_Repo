import os
import logging
from flask import Flask, request, jsonify, render_template
from ai_programmer import generate_code, debug_code
from github_manager import save_and_push_code
from project_planner import generate_project_plan

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    """Главная страница"""
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    """Генерация кода"""
    data = request.json
    prompt = data.get("prompt", "Напиши простой скрипт")
    language = data.get("language", "python")
    
    code = generate_code(prompt, language)
    fixed_code = debug_code(code)

    save_and_push_code(fixed_code, "generated_code.py")

    return jsonify({"message": "Код создан и загружен!", "code": fixed_code})

@app.route("/plan", methods=["POST"])
def plan():
    """Создание структуры проекта"""
    data = request.json
    description = data.get("description", "Создай веб-приложение")

    plan = generate_project_plan(description)

    return jsonify({"message": "План проекта создан!", "plan": plan})

if __name__ == "__main__":
    app.run(debug=True)
