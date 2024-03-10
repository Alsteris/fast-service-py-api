from sqlalchemy.ext.asyncio import AsyncSession
from datastore import barang_datastore
from schema import regisBarang

async def regis_barang(data: regisBarang, db_session:AsyncSession):
    async with db_session as session:
        try:  
            if data.nama_barang == "" :
                raise Exception("Nama Transaksi harus di isi")
            
            if data.jenis_barang == "" :
                raise Exception("Nama Transaksi harus di isi")
            
            if data.stok_barang == "" :
                raise Exception("Jenis Transaksi harus di isi")
        
            if data.transaksi_in == "" :
                raise Exception("Transaksi in harus di isi")

            if data.transaksi_out == "" :
                raise Exception("Transkasi out harus di isi")

            if data.user_otorisasi == "" :
                raise Exception("User otorisasi harus di isi")
            
            resvalidasibarang,e = await barang_datastore.GetListNamaBarang(data.nama_barang, session)
            if resvalidasibarang not in (None,{}):
                raise Exception("Nama Barang sudah digunakan! silahkan masukkan nama yang lain")

            resBarang, e = await barang_datastore.regisBarang(data, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resBarang, None


        except Exception as e:
            return data, e
        

async def get_list_barang(page: int, limit:int, keyword:str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resgetBarang, e = await barang_datastore.getListBarang(page, limit, keyword, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resgetBarang, None


        except Exception as e:
            return resgetBarang, e
        
async def get_list_nama_barang(Nama_Barang:str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resgetNamaBarang, e = await barang_datastore.GetListNamaBarang(Nama_Barang, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resgetNamaBarang, None
        
        except Exception as e:
            return None, e
        
async def update_stok_barang(Nama_Barang:str, Stok_Barang:int, db_session:AsyncSession):
    async with db_session as session:
        try:  

            updateStokBrg, e = await barang_datastore.UpdateStokBarang(Nama_Barang, Stok_Barang, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return updateStokBrg, None


        except Exception as e:
            return None, e
        
async def Delete_Barang(Nama_Barang:str,  db_session:AsyncSession):
    async with db_session as session:
        try:  

            DelBarang, e = await barang_datastore.DeleteBarang(Nama_Barang,  session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return DelBarang, None


        except Exception as e:
            return None, e