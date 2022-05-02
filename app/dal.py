from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from init_db import *

engine = create_async_engine(
    f"postgresql+asyncpg://{dbLogin}:{dbPass}@postgres_db_container/{dbName}"
)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def has_question(question_id: int) -> bool:
    async with async_session() as session:
        async with session.begin():
            stmt = select(
                select(Question).where(Question.question_id == question_id).exists()
            )
            result = await session.execute(stmt)
            res = result.scalar()
            return res


async def add_question(question_id: int, question_text: str, answer_text: str) -> None:
    async with async_session() as session:
        async with session.begin():
            session.add(
                Question(
                    question_id=question_id,
                    question_text=question_text,
                    answer_text=answer_text,
                )
            )
        await session.commit()

async def get_last_question() -> Question:
    async with async_session() as session:
        async with session.begin():
            stmt = select(Question).order_by(-Question.id)
            result = await session.execute(stmt)
            return result.scalars().first()