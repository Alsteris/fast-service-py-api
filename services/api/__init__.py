from fastapi import APIRouter

from .testing import *
from .user_api import *
from .barang_api import *
from .transaksi_api import *

api_router = APIRouter()

api_router.include_router(testing.router, prefix='/greeting', tags=['Greeting'])
api_router.include_router(user_api.router, prefix='/user', tags=['User Management'])
api_router.include_router(barang_api.router, prefix='/barang', tags=['Barang'])
api_router.include_router(transaksi_api.router, prefix='/transaksi', tags=['Transaksi'])