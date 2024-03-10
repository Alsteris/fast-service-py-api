from models import barang_models
from sqlalchemy import select, or_, and_, update, delete

async def regisBarang(data, session):
    try:
        paramsInsert = barang_models.barang(
            nama_barang = data.nama_barang,
            jenis_barang = data.jenis_barang,
            stok_barang = data.stok_barang,
            transaksi_in = data.transaksi_in,
            transaksi_out = data.transaksi_out,
            user_otorisasi = data.user_otorisasi,
        )

        session.add(paramsInsert)
        return data, None
    except Exception as e:
        return data, e
    
async def getListBarang(page, limit, keyword, session):
    try:
        terms = []
        if keyword not in (None, ""):
            terms.append(
                or_(
                    (barang_models.barang.nama_barang.ilike(f"%{keyword.lower()}%")),
                    (barang_models.barang.jenis_barang.ilike(f"%{keyword.lower()}%")),

                )
            )

        offset = (page*limit)
        sql = select(barang_models.barang).filter(and_(*(terms))).offset(offset).limit(limit)
        proxy_rows = await session.execute(sql)
        data = proxy_rows.scalars().all()
        
        return data, None
    except Exception as e:
        return data, e

async def GetListNamaBarang(nama_barang, session):
    try:
        sql = select(barang_models.barang).where(barang_models.barang.nama_barang == nama_barang)
        proxy_rows = await session.execute(sql)
        data = proxy_rows.scalars().first()
        
        return data, None
    except Exception as e:
        return None, e
    
async def UpdateStokBarang(nama_barang, stok_barang, session) :
    try:
        terms = []
        if nama_barang not in (None, ""):
            terms.append(
                or_(
                    (barang_models.barang.nama_barang.ilike(f"%{nama_barang.lower()}%")),
                )
            )

        sql =(
            update(barang_models.barang)
            .where(barang_models.barang.nama_barang == nama_barang)
            .values(stok_barang = stok_barang)
        )
        await session.execute(sql)
        await session.commit()
        
        return nama_barang, None
    except Exception as e:
        return None, e
    
async def DeleteBarang(nama_barang, session) :
    try:
        sql =(
        delete(barang_models.barang)
        .where(barang_models.barang.nama_barang == nama_barang)
        )
        await session.execute(sql)
        await session.commit()
        
        return nama_barang, None
    except Exception as e:
        return None, e
    
