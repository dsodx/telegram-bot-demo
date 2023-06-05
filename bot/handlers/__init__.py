from aiogram import Dispatcher
from sqlalchemy.ext.asyncio import async_sessionmaker


def setup_routers(dp: Dispatcher, session_pool: async_sessionmaker) -> None:
    from ..middlewares import DbSessionMiddleware

    from . import common
    dp.include_router(router=common.router)

    from . import filters
    dp.include_router(router=filters.router)

    from . import postgres
    postgres.router.message.middleware(DbSessionMiddleware(session_pool=session_pool))
    dp.include_router(router=postgres.router)

    from . import fsm
    fsm.router.message.middleware(DbSessionMiddleware(session_pool=session_pool))
    dp.include_router(router=fsm.router)
