from fastapi import FastAPI
from db import Base, engine
from api.user_api import user_router
from api.question_api import question_router
# создаем бд и делаем миграции
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/", title="Project")
# добавляем роутер в запускаемые компоненты проекта
app.include_router(user_router)
app.include_router(question_router)
# запуск проекта если апи асинхронный
# uvicorn main:app --reload
# запуск проекта если апи синхронное (функции все синхронные)
# gunicorn main:app



