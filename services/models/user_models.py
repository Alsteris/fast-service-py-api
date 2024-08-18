from sqlalchemy import Column, String, BigInteger, Text, DateTime, Integer, Numeric
from datetime import datetime
from utils import Base
from pydantic import BaseModel


class Users(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    email = Column(String(50))
    password = Column(Text)
    role = Column(String(5))
    create_at = Column(DateTime, default=datetime.now())


class UsersDetail(Base):
    __tablename__ = 'users_detail'
    id = Column(BigInteger, primary_key=True)
    email = Column(String(50))
    nomor_identitas = Column(String(50))
    nama_lengkap = Column(String(100))
    tanggal_lahir = Column(String(20))
    alamat = Column(Text)
    nomor_telepon = Column(String(13))
    create_at = Column(DateTime, default=datetime.now())

