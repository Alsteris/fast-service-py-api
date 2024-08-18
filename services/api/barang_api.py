from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from security.auth import JWTBearer
from security import token_blacklist

from app import barang_crud
from utils import RespApp, get_async_session
from schema import regisBarang


router = APIRouter()

@router.post("/regis-barang")
async def regisBarang(
    request: regisBarang,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await barang_crud.regis_barang(request, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/get-list-barang", tags=["posts"])
async def get_list_barang(
    token: str = Depends(JWTBearer()),
    page: int = 0,
    limit: int = 10,
    keyword: str = None,
    db: AsyncSession = Depends(get_async_session)
):
    try:
        # Check if token is in blacklist
        if token in token_blacklist:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has been invalidated. Please log in again.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Proceed with fetching barang data
        out_resp, e = await barang_crud.get_list_barang(page, limit, keyword, db)
        if e:
            return RespApp(status="02", message=f"{e}", data=None)
        
        return RespApp(status="00", message="success", data=out_resp)
    except Exception as e:
        return RespApp(status="02", message=f"{e}", data=None)

@router.get("/get-list-nama-barang")
async def GetListNamaBarang(
    token: str = Depends(JWTBearer()),
    Nama_Barang: str = "masukkan nama barang",
    db: AsyncSession = Depends(get_async_session)
    ):
    try:
        if token in token_blacklist:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has been invalidated. Please log in again.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        out_resp, e = await barang_crud.get_list_nama_barang(Nama_Barang, db)
        if e != None:
            return RespApp(status="02", message=f"{e}", data=None)
        
        return RespApp(status="00", message="success", data=out_resp)
    
    except Exception as e:
        return RespApp(status="02", message=f"{e}", data=None)


@router.put("/update-stok-barang")
async def UpdateStokBarang(
    Nama_Barang: str = "masukkan nama barang",
    Stok_Barang : int = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await barang_crud.update_stok_barang(Nama_Barang, Stok_Barang, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.delete("/Delete-Barang")
async def DeleteBarang(
    Nama_Barang: str = "masukkan nama barang yang akan dihapus",
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await barang_crud.Delete_Barang(Nama_Barang, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data = None)
    
    return RespApp(status="00", message="success", data=out_resp)