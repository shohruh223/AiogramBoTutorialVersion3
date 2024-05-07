from aiogram import Router


def setup_message_routers() -> Router:
    from . import start, help

    router = Router()
    router.include_router(start.router)
    router.include_router(help.router)
    return router