from typing import Dict, Any

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User, UserProfile


async def get_user(session: AsyncSession, user_id: int) -> User:
    return await session.scalar(select(User).where(User.id == user_id))


async def get_user_profile(session: AsyncSession, user_id: int) -> UserProfile:
    return await session.scalar(select(UserProfile).where(UserProfile.id == user_id))


async def update_user_profile(session: AsyncSession, user_id: int, data: Dict[str, Any]) -> None:
    await session.execute(update(UserProfile).values(**data).where(UserProfile.id == user_id))
