import openai
import logging

def generate_project_plan(description):
    """Создаёт план проекта на основе запроса"""
    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Ты опытный архитектор программных проектов."},
            {"role": "user", "content": f"Создай структуру проекта: {description}"}
        ],
        temperature=0.4
    )
    plan = response.choices[0].message.content
    logging.info("✅ План проекта сгенерирован!")
    return plan
