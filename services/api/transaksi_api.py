from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, date

from app import transaksi_crud
from utils import RespApp, get_async_session
from schema import regisDataTransaksi, transaksipembelian

router = APIRouter()

@router.post("/regis-data-transaksi")
async def regisDataTransaksi(
    request: regisDataTransaksi,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await transaksi_crud.regis_data_transaksi(request, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)


@router.get("/get-list-data-transaksi")
async def GetListUserDetail(
    page: int = 0,
    limit: int = 10,
    keyword: str = None,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await transaksi_crud.get_list_data_transaksi(page, limit, keyword, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/get-detail-transaksi")
async def GetDetailTransaksi(
    id_transaksi: int = "masukkan id transaksi",
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await transaksi_crud.get_detail_transaksi(id_transaksi, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.put("/update-user-otorisasi")
async def UpdateUserOtorisasi(
    params: int = "masukkan id transaksi",
    otorisasi : str = "approved",
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await transaksi_crud.update_otorisasi_user(params, otorisasi, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.delete("/Delete-Transaksi")
async def DeleteTransaksi(
    Id_Transaksi: int = "masukkan Id Transaksi yang akan dihapus",
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await transaksi_crud.Delete_Transaksi(Id_Transaksi, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data = None)
    
    return RespApp(status="00", message="success", data=out_resp)


@router.post("/post-transaksi-pembelian")
async def PostDataTransaksi(
    request: transaksipembelian,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp, e = await transaksi_crud.transaksi_pembelian(request, db)
    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)

@router.get("/get-transaksi-by-tanggal")
async def read_items(
    keyword: str = "Masukkan user atau nama barang",
    start_date : str = Query("", description = "Tanggal awal filter", example="2024-01-01"), 
    end_date : str =Query("", description = "Tanggal akhir filter",example="2024-01-10"), 
    db: AsyncSession = Depends(get_async_session)
    ):
    if start_date == "" and end_date == "":
        out_resp, e = await transaksi_crud.get_detail_transaksi2(keyword, db)
    else:
        out_resp, e = await transaksi_crud.get_transaksi_by_tgl(keyword,start_date,end_date, db)

    if e != None:
        return RespApp(status="02", message=f"{e}", data=None)
    
    return RespApp(status="00", message="success", data=out_resp)