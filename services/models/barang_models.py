from sqlalchemy import Column, String, BigInteger, Text, DateTime, Integer, Numeric
from datetime import datetime
from utils import Base

class barang(Base):
    __tablename__ = 'barang'
    id = Column(BigInteger, primary_key=True)
    nama_barang = Column(String(50))
    jenis_barang = Column(String(50))
    stok_barang = Column(Integer)
    transaksi_in = Column(Numeric(28, 2))
    transaksi_out = Column(Numeric(28, 2))
    user_otorisasi = Column(String(100)) 
    create_date = Column(DateTime, default=datetime.now())
    update_data = Column(DateTime, onupdate=datetime.now())