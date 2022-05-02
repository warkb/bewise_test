from fastapi import FastAPI, Form

import dal
import services

app = FastAPI()

@app.post("/add-questions/")
async def addQuestions(questions_num: int = Form(...)):
    last_question = await dal.get_last_question()
    await services.add_questions_to_db(questions_num)
    return services.serialize_question(last_question)

