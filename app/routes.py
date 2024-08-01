@router.get("/api/v1/messages/")
async def get_messages(skip: int = 0, limit: int = 10):
    # Пример запроса к базе данных с пагинацией
    messages = [...]  # Реализуйте логику для получения данных с использованием skip и limit
    return messages
