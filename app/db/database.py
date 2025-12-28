from fastapi import Request


def get_db(request: Request):
    """
    Возвращает MongoDB из состояния приложения
    """
    return request.app.state.db
