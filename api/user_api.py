from fastapi import APIRouter
from db.userservice import *
# создаем роутер(аналог блюпринта)
user_router = APIRouter(prefix="/user",
                        tags=["Пользователи"])
# регистрация юзера
@user_router.post("/register")
async def register_user(username: str, phone_number: str,
                        level: str = None):
    result = add_user_db(username, phone_number, level)
    if result:
        return {"status": 1, "message": result}
    return {"status": 0, "message": "Не удалось добавить юзера"}
# получение всех юзеров
@user_router.get("/all_users")
async def get_all_users():
    all_users = get_all_users_db()
    if all_users:
        return {"status": 1, "message": all_users}
    return {"status": 0, "message": "Не удалось подключиться к базе"}

# получение определенного пользователя
@user_router.get("/user-info")
async def get_exact_user(user_id: int):
    user = get_exact_user_by_id_db(user_id)
    if user:
        return {"status": 1, "message": user}
    return {"status": 0, "message": "Не удалось найти юзера"}
@user_router.delete("/user-info")
async def delete_user(user_id: int):
    result = delete_exact_user_db(user_id)
    if result:
        return {"status": 1, "message": "Юзер удален"}
    return {"status": 0, "message": "Не удалось удалить юзера"}

@user_router.post("/add-answer")
async def user_answer(q_id: int, user_answer: str, user_id:int, level: str = None):
    result = user_answer_db(q_id=q_id, user_answer=user_answer, user_id=user_id,
                            level=level)
    if result == "Такого вопроса нету":
        return {"status": 0, "message": result}
    elif result:
        return {"status": 1, "message": result}
    return {"status": 1, "message": "Неправильный ответ"}
@user_router.get('/user-result')
async def get_user_result(user_id: int):
    result = get_user_result_db(user_id)
    if result:
        return {'status': 1, 'message': result}
    else:
        return {'status': 0, 'message': 'No such user'}
