from datetime import datetime
def year(request):
    """Добавляет переменную с текущим годом."""
    time = datetime.now()
    return {
        'year': time.year
    }