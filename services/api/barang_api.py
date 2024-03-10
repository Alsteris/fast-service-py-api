from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

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

@router.get("/get-list-barang")
async def GetListBarang(
    page: int = 0,
    limit: int = 10,
    keyword: str = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await barang_crud.get_list_barang(page, limit, keyword, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/get-list-nama-barang")
async def GetListNamaBarang(
    Nama_Barang: str = "masukkan nama barang",
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await barang_crud.get_list_nama_barang(Nama_Barang, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
        
    return RespApp(status="00", message="success", data=out_resp)

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