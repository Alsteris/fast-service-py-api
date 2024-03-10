from sqlalchemy import Column, String, BigInteger, Text, DateTime, Integer, Numeric
from datetime import datetime
from utils import Base

class transaksi(Base):
    __tablename__ = 'transaksi'
    id = Column(BigInteger, primary_key=True)
    nama_transaksi = Column(String(50))
    nama_barang = Column(String(50))
    jumlah_barang = Column(Integer)
    jenis_transaksi = Column(String(100))
    transaksi_in = Column(String(1))
    transaksi_out = Column(String(1))
    status = Column(String(10))
    user_otorisasi = Column(String(100))
    create_date = Column(DateTime, default=datetime.now())
    update_data = Column(DateTime, onupdate=datetime.now())