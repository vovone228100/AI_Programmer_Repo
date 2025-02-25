import timeit

def analyze_performance(code):
    """Запускает тест производительности кода."""
    exec_time = timeit.timeit(code, number=100)
    return f"⏳ Код выполняется за {exec_time:.5f} секунд."
