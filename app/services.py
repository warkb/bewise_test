import aiohttp
import json

from dal import *

def serialize_question(question: Question) -> dict:
    if not question:
        return {}
    return {
        'id': question.id,
        'question_id': question.question_id,
        'question_text': question.question_text,
        'answer_text': question.answer_text,
        'pub_date': question.pub_date
    }

async def get_questions_from_api(questions_num: int = 1) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://jservice.io/api/random", params={"count": questions_num}
        ) as resp:
            return json.loads(await resp.text())[0]

async def get_unique_question() -> dict:
    question = await get_questions_from_api()
    if await has_question(question["id"]):
        return get_unique_question()
    return question

async def add_questions_to_db(questions_num: int) -> None:
    for _ in range(questions_num):
        question = await get_unique_question()
        await add_question(question["id"], question["question"], question["answer"])