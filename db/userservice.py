from db import get_db
from db.models import User, UserAnswer, Question, LiderResult


# Функция для добавления пользователя в бд
def add_user_db(username, phone_number, level=None):
    with next(get_db()) as db:
        new_user = User(username=username,
                        phone_number=phone_number,
                        level=level)
        db.add(new_user)
        db.commit()
        return True


# Функцию для получение всех пользователей
def get_all_users_db():
    with next(get_db()) as db:
        all_users = db.query(User).all()
        return all_users


# Функцию для получение определенного  пользователя по айди
def get_exact_user_by_id_db(user_id):
    with next(get_db()) as db:
        exact_user = db.query(User).filter_by(id=user_id).first()
        if exact_user:
            return exact_user
        return False
def delete_exact_user_db(user_id):
    # старый метод создания сессии
    db = next(get_db())
    exact_user = db.query(User).filter_by(id=user_id).first()
    db.delete(exact_user)
    db.commit()
    return True




# Функцию для сохранения ответов пользователя
def user_answer_db(q_id, user_answer, user_id, level):
    with next(get_db()) as db:
        exact_question = db.query(Question).filter_by(id=q_id).first()
        if exact_question:
            if exact_question.correct_answer == user_answer:
                correctness = True
            else:
                correctness = False
            new_answer = UserAnswer(user_id=user_id,
                                    question_id=q_id,
                                    level=level,
                                    user_answer=user_answer,
                                    correctness=correctness)
            db.add(new_answer)
            db.commit()
            if correctness:
                user_result = db.query(LiderResult).filter_by(user_id=user_id).first()
                if user_result:
                    user_result.correct_answers += 1
                    db.commit()
                    return "Плюс один бал"
                elif not user_result:
                    new_lider = LiderResult(user_id=user_id, level=level, correct_answers=1)
                    db.add(new_lider)
                    db.commit()
                    return "Плюс один бал"
            else:
                return False
        else:
            return "Такого вопроса нету"


# Функция для получения результатов пользователя
def get_user_result_db(user_id):
    with next(get_db()) as db:
        user_result = db.query(LiderResult).filter_by(user_id=user_id).first()
        if user_result:
            return user_result
        return False

# Для получение всех данных из таблицы
# db.query(Table).all()


# Для полуения определенные данные из таблицы
# db.query(Table).filter_by(id=id).first()

# Для добавление данных в бд
# new_table = Table(name="qwe")
# db.add(new_table)
# db.commit()


# Для обновления и удаления даных в бд
# exact_table = db.query(Table).filter_by(id=1).first()
# exact_table.name = "qweqw"
# db.delete(exact_table)
# db.commit()

