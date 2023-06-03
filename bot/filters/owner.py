from aiogram.filters import Filter
from aiogram.types import Message

from ..config import Settings


class IsOwnerFilter(Filter):
    def __init__(self, is_owner: bool) -> None:
        self.is_owner = is_owner

    async def __call__(self, message: Message, config: Settings) -> bool:
        return (message.from_user.id == config.owner_id) == self.is_owner
