from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User


async def get_user(session: AsyncSession, user_id: int) -> User:
    return await session.scalar(select(User).where(User.id == user_id))
