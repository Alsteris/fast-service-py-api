from fastapi import APIRouter

from app import testing_crud
from utils import RespApp
from schema import account


router = APIRouter()

@router.get("/")
async def greeting():
    out_resp = await testing_crud.Greeting()
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/greeting-for-all")
async def GreetingForAll(request: str):
    out_resp = await testing_crud.GreetingForAll(request)
    return RespApp(status="00", message="success", data=out_resp)

@router.post("/login")
async def Login(request: account):
    out_resp = await testing_crud.login(request)
    return RespApp(status="00", message="success", data=out_resp)