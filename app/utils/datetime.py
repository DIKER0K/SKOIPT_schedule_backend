from _datetime import datetime
from app.core.config import settings

def now() -> datetime:
    """
    Возвращает текущее время в timezone приложения
    """
    return datetime.now(tz=settings.tz)