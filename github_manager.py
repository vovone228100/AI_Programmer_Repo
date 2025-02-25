import os
import git
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()
GITHUB_REPO = os.getenv("GITHUB_REPO")

def commit_and_push(file_path, commit_message="Обновление кода"):
    """Коммитим и отправляем изменения в GitHub"""
    repo = git.Repo(".")
    repo.git.add(file_path)
    repo.index.commit(commit_message)
    repo.remote().push()
    print(f"🚀 Изменения отправлены в GitHub: {file_path}")

def save_and_push_code(code, filename="generated_code.py"):
    """Сохраняем код в файл и загружаем в GitHub"""
    file_path = filename
    with open(file_path, "w") as f:
        f.write(code)
    commit_and_push(file_path)
