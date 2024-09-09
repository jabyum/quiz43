from db import get_db
from db.models import Question, LiderResult


# Функция для добавления вопросов
def add_question_db(main_question, v1, v2, v3, v4,
                    correct_answer):
    with next(get_db()) as db:
        new_question = Question(main_question=main_question,
                                v1=v1, v2=v2, v3=v3, v4=v4,
                                correct_answer=correct_answer)
        db.add(new_question)
        db.commit()
        return "Вопрос успешно добавлен"


# Получить первые 20 вопросов
def get_questions_db():
    with next(get_db()) as db:
        all_questions = db.query(Question).all()
        return all_questions[:20]


# Топ 10 лидеров
def get_10_leaders():
    with next(get_db()) as db:
        leaders = db.query(LiderResult).order_by(LiderResult.correct_answers.desc())
        return leaders[:10]
