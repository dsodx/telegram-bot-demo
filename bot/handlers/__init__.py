from aiogram import Dispatcher


def setup_routers(dp: Dispatcher) -> None:
    from . import common
    dp.include_router(router=common.router)

    from . import filters
    dp.include_router(router=filters.router)
