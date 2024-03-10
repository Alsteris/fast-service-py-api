from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import user_crud
from utils import RespApp, get_async_session
from schema import account, regisAccount, regisUserDetail



router = APIRouter()

@router.post("/regis-new-account")
async def RegistNewAccount(
    request: regisAccount,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.create_new_account(request, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/get-list-new-account")
async def GetListNewAccount(
    page: int = 0,
    limit: int = 10,
    keyword: str = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.get_list_new_account(page, limit, keyword, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.post("/regis-user-detail")
async def regisUsersDetail(
    request: regisUserDetail,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.create_user_detail(request, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/get-list-user-detail")
async def GetListUserDetail(
    page: int = 0,
    limit: int = 10,
    keyword: str = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.get_list_user_detail(page, limit, keyword, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/get-list-user-detail-by-email")
async def GetListUserDetailByEmail(
    params: str = "masukkan email",
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.get_list_user_detail_by_email(params, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.put("/update-user-detail-by-email")
async def UpdateUserDetailByEmail(
    email: str = None,
    nomor_telepon: str = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.update_user_detail_by_email(email, nomor_telepon, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.delete("/Delete-Account")
async def DeleteAccount(
    email: str = "masukkan email akun yang akan dihapus",
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await user_crud.Delete_Account(email, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data = None)
    
    return RespApp(status="00", message="success", data=out_resp)


