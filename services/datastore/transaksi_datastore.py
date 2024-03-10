from models import transaksi_models, barang_models
from sqlalchemy import select, or_, and_, update, delete, func
from api import user_api
from datetime import datetime

async def regisDataTransaksi(data, session):
    try:
        # cek nama transaksi : 
        cek_tr = select(transaksi_models.transaksi).where(transaksi_models.transaksi.nama_transaksi == data.nama_transaksi)
        proxy_rows = await session.execute(cek_tr)
        transaksilama = proxy_rows.scalars().first()
        if transaksilama != None :
            sql =(
                update(barang_models.barang)
                .where(barang_models.barang.nama_barang == data.nama_barang)
                .values(stok_barang= barang_models.barang.stok_barang + data.jumlah_barang)
            )
            await session.execute(sql)
            await session.commit()
        else :    

            barangbaru = barang_models.barang(
                nama_barang=data.nama_barang,
                stok_barang=data.jumlah_barang,
                transaksi_in=data.harga_beli,
                transaksi_out=data.harga_jual
            )
            session.add(barangbaru)
        paramsInsert = transaksi_models.transaksi(
            nama_transaksi = data.nama_transaksi,
            nama_barang = data.nama_barang,
            jumlah_barang = data.jumlah_barang,
            jenis_transaksi = data.jenis_transaksi,
            transaksi_in = data.transaksi_in,
            transaksi_out = data.transaksi_out,
            status = "unaproved",
            user_otorisasi = data.user_otorisasi 
        )
        
        session.add(paramsInsert)

        
        return data, None
    except Exception as e:
        return data, e


async def getListDataTransaksi(page, limit, keyword, session):
    try:
        terms = []
        if keyword not in (None, ""):
            terms.append(
                or_(
                    (transaksi_models.transaksi.nama_transaksi.ilike(f"%{keyword.lower()}%")),
                    (transaksi_models.transaksi.jenis_transaksi.ilike(f"%{keyword.lower()}%"))
                    #(transaksi_models.transaksi.Transaksi_In.ilike(f"%{keyword.lower()}%"))
                    #(transaksi_models.transaksi.Transaksi_Out.ilike(f"%{keyword.lower()}%"))
                    #(transaksi_models.transaksi.User_otorisasi.ilike(f"%{keyword.lower()}%"))
                )
            )

        offset = (page*limit)
        sql = select(transaksi_models.transaksi).filter(and_(*(terms))).offset(offset).limit(limit)
        proxy_rows = await session.execute(sql)
        data = proxy_rows.scalars().all()
        
        return data, None
    except Exception as e:
        return data, e
    
async def GetDetailTransaksi(id_transaksi, session):
    try:
        sql = select(transaksi_models.transaksi).where(transaksi_models.transaksi.id == id_transaksi)
        proxy_rows = await session.execute(sql)
        data = proxy_rows.scalars().first()
        
        return data, None
    except Exception as e:
        return None, e
    
async def UpdateOtorisasiUser(params, otorisasi, session) :
    try:
        sql =(
            update(transaksi_models.transaksi)
            .where(transaksi_models.transaksi.id == params)
            .values(status = otorisasi)
        )
        await session.execute(sql)
        await session.commit()
        
        return params, None
    except Exception as e:
        return None, e
    
async def DeleteTransaksi(Id_Transaksi, session) :
    try:
        sql =(
        delete(transaksi_models.transaksi)
        .where(transaksi_models.transaksi.id == Id_Transaksi)
        )
        await session.execute(sql)
        await session.commit()
        
        return Id_Transaksi, None
    except Exception as e:
        return None, e

async def transaksipem(data, session):
    try:
        # cek nama transaksi : 
        cek_tr = select(transaksi_models.transaksi).where(transaksi_models.transaksi.nama_transaksi == data.nama_transaksi)
        proxy_rows = await session.execute(cek_tr)
        transaksilama = proxy_rows.scalars().first()
        if transaksilama != None :
            sql =(
                update(barang_models.barang)
                .where(barang_models.barang.nama_barang == data.nama_transaksi)
                .values(stok_barang= barang_models.barang.stok_barang - data.jumlah_barang)
            )
            await session.execute(sql)
            await session.commit()
        else :    

            barangbaru = barang_models.barang(
                nama_barang=data.nama_transaksi,
                stok_barang=data.jumlah_barang,
                transaksi_in=data.harga_beli,
                transaksi_out=data.harga_jual
            )
            session.add(barangbaru)

        transaksiinsert = transaksi_models.transaksi(
            nama_transaksi=data.nama_transaksi,
            jenis_transaksi=data.jenis_transaksi,
            transaksi_in=data.transaksi_in,
            transaksi_out=data.transaksi_out,
            jumlah_barang=data.jumlah_barang,
            status="unapproved",
            user_otorisasi="spv"
        )
        session.add(transaksiinsert)

        await session.commit()  

        return data, None  
    except Exception as e:
        return data, e
    
async def getTransaksiByTgl(keyword, start_date, end_date, session):
    try:
        if start_date is not None and end_date is not None:
            sql = select(transaksi_models.transaksi).where(
                and_(
                    transaksi_models.transaksi.create_date.between(datetime.strptime(start_date, "%Y-%m-%d"), datetime.strptime(end_date, "%Y-%m-%d")),
                    func.lower(transaksi_models.transaksi.user_otorisasi).ilike(f"%{keyword.lower()}%")
                )
            )
            result = await session.execute(sql)
            data = result.scalars().all()
        
        if keyword not in (None, ""):
            sql = select(transaksi_models.transaksi).where(
                    transaksi_models.transaksi.create_date.between(datetime.strptime(start_date, "%Y-%m-%d"), datetime.strptime(end_date, "%Y-%m-%d"))
                )
            result = await session.execute(sql)
            data = result.scalars().all()

        # if start_date == "" and end_date == "":
        #     sql = select(transaksi_models.transaksi).where(
        #             func.lower(transaksi_models.transaksi.user_otorisasi).ilike(f"%{keyword.lower()}%")
        #             )
        #     result = await session.execute(sql)
        #     data = result.scalars().all()


        return data, None
    except Exception as e:
        return None, e
    
async def GetDetailTransaksi2(keyword, session):
    try:
        sql = select(transaksi_models.transaksi).where(func.lower(transaksi_models.transaksi.user_otorisasi).ilike(f"%{keyword.lower()}%"))
        proxy_rows = await session.execute(sql)
        data = proxy_rows.scalars().all()
        
        return data, None
    except Exception as e:
        return None, e