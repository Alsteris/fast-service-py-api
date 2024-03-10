from pydantic import BaseModel

class regisDataTransaksi(BaseModel):
    nama_transaksi : str = "Penjualan Sepeda"
    nama_barang : str = "Sepeda BMX"
    jumlah_barang: int = 5
    jenis_transaksi : str = "Penjualan" 
    transaksi_in : str = "D"
    transaksi_out : str = "K"
    user_otorisasi : str = "SPV"

class transaksipembelian(BaseModel):
    nama_transaksi : str = "Penjualan Sepeda"
    nama_barang : str = "Sepeda BMX"
    jumlah_barang: int = 5
    jenis_transaksi : str = "Penjualan" 
    transaksi_in : float = 5000
    transaksi_out : float = 6000
    user_otorisasi : str = "SPV"