from aiogram import Router

from handlers.admin import router as admin
from handlers.start import router as start
from handlers.user import router as user
from handlers.callback import router as callback

router = Router()
router.include_routers(start,admin,user,callback)