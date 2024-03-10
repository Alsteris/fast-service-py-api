from pydantic import BaseModel

class account(BaseModel):
    username : str = "muhalibalhtiar@gmail.com"
    password : str = "1234zzxx"
    secretKey : str = "xxxx"

class regisAccount(BaseModel):
    email : str = "lewishamilton44@gmail.com"
    password : str = "mercedesamg44"
    role : str = "racer"

class regisUserDetail(BaseModel):
    email : str = "maxverstappen01@gmail.com"
    nomor_identitas : str = "012390"
    nama_lengkap : str = "Max Verstappen"
    tanggal_lahir : str = " 1 Januari 1995"
    alamat : str = "Netherland"
    nomor_telepon: str = "08213819379" 



