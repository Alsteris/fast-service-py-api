from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, date
from datastore import transaksi_datastore, barang_datastore
from schema import regisDataTransaksi, transaksipembelian

async def regis_data_transaksi(data: regisDataTransaksi, db_session:AsyncSession):
    async with db_session as session:
        try:  
            if data.nama_transaksi == "" :
                raise Exception("Nama Transaksi harus di isi")
            
            if data.nama_barang == "" :
                raise Exception("Nama Transaksi harus di isi")
            
            if data.jumlah_barang == "" :
                raise Exception("Nama Transaksi harus di isi")

            if data.jenis_transaksi == "" :
                raise Exception("Jenis Transaksi harus di isi")
        
            if data.transaksi_in == "" :
                raise Exception("Transaksi in harus di isi")

            if data.transaksi_out == "" :
                raise Exception("Transkasi out harus di isi")

            if data.user_otorisasi == "" :
                raise Exception("User otorisasi harus di isi")
            

            resNewtransaksi, e = await transaksi_datastore.regisDataTransaksi(data, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resNewtransaksi, None


        except Exception as e:
            return data, e
        
async def get_list_data_transaksi(page: int, limit:int, keyword:str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resgetDataTransaksi, e = await transaksi_datastore.getListDataTransaksi(page, limit, keyword, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resgetDataTransaksi, None
        

        except Exception as e:
            return resgetDataTransaksi, e
        
async def get_detail_transaksi(id_transaksi:int, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resgetDetailTransaksi, e = await transaksi_datastore.GetDetailTransaksi(id_transaksi, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resgetDetailTransaksi, None


        except Exception as e:
            return resgetDetailTransaksi, e


async def update_otorisasi_user(params:int, otorisasi:str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            updateotorisasi, e = await transaksi_datastore.UpdateOtorisasiUser(params, otorisasi, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return updateotorisasi, None


        except Exception as e:
            return None, e

async def Delete_Transaksi(Id_Transaksi:int,  db_session:AsyncSession):
    async with db_session as session:
        try:  

            DelTransaksi, e = await transaksi_datastore.DeleteTransaksi(Id_Transaksi,  session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return DelTransaksi, None


        except Exception as e:
            return None, e
        
# asnyc def transaksi_penjualan(nama_barang: str, jumlah_jual: int, db_session:AsyncSession):
#     async with db_session as session:
#         try:

#             TrPenjualan, e = await transaksi_datastore.TransaksiPenjualan(nama_barang, jumlah_jual, session)
#             if e != None:
#                 raise Exception(f"{e}")
            
#             await session.commit()

#             return TrPenjualan, None

#         except Exception as e:
#             return None, e


async def transaksi_penjualan(nama_barang:str, jumlah_jual: int,  db_session:AsyncSession):
    async with db_session as session:
        try:  

            TrPenjualan, e = await transaksi_datastore.TransaksiPenjualan(nama_barang, jumlah_jual,  session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return TrPenjualan, None


        except Exception as e:
            return None, e
        
async def transaksi_pembelian(data:transaksipembelian, db_session:AsyncSession):
    async with db_session as session:
        try:  
            print(data)  
            if data.nama_transaksi == "" :
                raise Exception("Nama transaksi harus di isi !")
            
            if data.jenis_transaksi == "" :
                raise Exception("Jenis transaksi harus di isi")
        
            if data.transaksi_in == "":
                raise Exception("Tranksasi in (harga beli)")
            
            if data.transaksi_out == "":
                raise Exception("Tranksasi out (harga jual)")
            
            if data.jumlah_barang == "" :
                raise Exception("jumlah barang harus di isi !")
            
            
            CreateNewTr, e = await transaksi_datastore.transaksipem(data, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return CreateNewTr, None


        except Exception as e:
            return data, e
        
async def get_transaksi_by_tgl(keyword: str, start_date: str, end_date: str, db_session:AsyncSession):
    async with db_session as session:
        try:
            datedetail, error = await transaksi_datastore.getTransaksiByTgl(keyword, start_date, end_date, session)
            if error:
                raise Exception(f"{error}")
        
            return datedetail, None  # Mengembalikan nilai datedetail dan None jika tidak ada kesalahan

        except Exception as e:
            return None, f"Terjadi kesalahan saat memperoleh data: {e}"
        
async def get_detail_transaksi2(keyword:str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resgetDetailTransaksi, e = await transaksi_datastore.GetDetailTransaksi2(keyword, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resgetDetailTransaksi, None


        except Exception as e:
            return resgetDetailTransaksi, e