from pydantic import BaseModel

class regisBarang(BaseModel):
    nama_barang : str = "Sepeda BMX"
    jenis_barang : str = "Sepeda"
    stok_barang : int = 10 
    transaksi_in : float = 1000000
    transaksi_out : float = 1500000
    user_otorisasi : str = "SPV"