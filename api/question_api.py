from fastapi import APIRouter
from db.testservice import *

question_router = APIRouter(prefix="/question", tags=["Вопросы"])

@question_router.post("/add-question")
async def add_question(main_question: str, v1:str, v2:str, v3:str, v4:str, correct_answer:str):
    result = add_question_db(main_question, v1, v2, v3, v4, correct_answer)
    if result:
        return {"status": 1, "message": result}
    return {"status": 0, "message": "Не удалось добавить вопрос"}

@question_router.get("/get-questions")
async def get_all_question():
    all_questions = get_questions_db()
    if all_questions:
        return {"status": 1, "message": all_questions}
    return {"status": 0, "message": "Не удалось подключиться к базе"}
@question_router.get('/leaders')
async def get_leaders():
    leaders = get_10_leaders()
    if leaders:
        return {'status': 1, 'message': leaders}
    else:
        return {'status': 0, 'message': 'No leaders yet'}
