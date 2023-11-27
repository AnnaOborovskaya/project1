from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def func_1():
    return {"Фамилия": "Оборовская", "Имя": "Анна", "Отчество": "Сергеевна"}

@app.get('/tools')
async def func_2():
    return {"телефон": "+7-983-546-47-04"}

@app.get('/users')
async def func_3():
    return "Создаю телеграм-ботов на Python любой сложности :)"
