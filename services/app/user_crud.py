from sqlalchemy.ext.asyncio import AsyncSession
from datastore import user_datastore
from schema import regisAccount, regisUserDetail, regisDataTransaksi, regisBarang, user_schema
from fastapi import FastAPI, Depends, HTTPException, status
from models import user_models
from security import verify_password, create_access_token
from datetime import timedelta

async def create_new_account(data: regisAccount, db_session:AsyncSession):
    async with db_session as session:
        try:  
            if data.email == "" :
                raise Exception("email harus di isi")
            
            if data.password == "" :
                raise Exception("password harus di isi")
        
            if data.role == "" :
                raise Exception("role harus di isi")
            
            resvalidatecreateacc,e = await user_datastore.GetUserDetailByEmail(data.email, session)
            if resvalidatecreateacc not in (None,{}):
                raise Exception("Email sudah digunakan! silahkan masukkan email yang baru")

            resCreateAccount, e = await user_datastore.registNewAccount(data, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()
            

            return resCreateAccount, None


        except Exception as e:
            return data, e
        
async def login_user(data: user_schema.login, db_session: AsyncSession):
    async with db_session as session:
        try:
            # Fetch user by email
            user, e = await user_datastore.GetUserDetailByEmail(data.email, session)
            if user is None or not verify_password(data.password, user.password):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect email or password",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            # Create JWT token
            access_token_expires = timedelta(minutes=30)
            access_token = create_access_token(
                data={"sub": user.email, "user_role": user.role}, expires_delta=access_token_expires
            )

            return {"access_token": access_token, "token_type": "bearer"}, None

        except Exception as e:
            return None, e



async def get_list_new_account(page: int, limit:int, keyword:str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resgetListNewAccount, e = await user_datastore.getListNewAccount(page, limit, keyword, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resgetListNewAccount, None


        except Exception as e:
            return resgetListNewAccount, e


async def create_user_detail(data: regisUserDetail, db_session:AsyncSession):
    async with db_session as session:
        try:  
            if data.email == "" :
                raise Exception("email harus di isi")
            
            if data.nomor_identitas == "" :
                raise Exception("password harus di isi")
        
            if data.nama_lengkap == "" :
                raise Exception("role harus di isi")

            if data.tanggal_lahir == "" :
                raise Exception("role harus di isi")

            if data.alamat == "" :
                raise Exception("role harus di isi")
            
            if data.nomor_telepon == "" :
                raise Exception("role harus di isi")
            
            resvalidasicreateacc,e = await user_datastore.GetUserDetailByEmail(data.email, session)
            if resvalidasicreateacc not in (None,{}):
                raise Exception("Email sudah digunakan! silahkan masukkan email yang baru")

            resCreateAccount, e = await user_datastore.regisUserDetail(data, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resCreateAccount, None


        except Exception as e:
            return data, e
        
async def get_list_user_detail(page: int, limit:int, keyword:str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resgetUserDetail, e = await user_datastore.getListUserDetail(page, limit, keyword, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resgetUserDetail, None


        except Exception as e:
            return resgetUserDetail, e

async def get_list_user_detail_by_email(keyword:str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            resgetUserDetailByEmail, e = await user_datastore.GetUserDetailByEmail(keyword, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return resgetUserDetailByEmail, None


        except Exception as e:
            return None, e
        
async def update_user_detail_by_email(email:str, nomor_telepon: str, db_session:AsyncSession):
    async with db_session as session:
        try:  

            updateUserDetail, e = await user_datastore.UpdateUserDetailByEmail(email, nomor_telepon, session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return updateUserDetail, None


        except Exception as e:
            return None, e
        
async def Delete_Account(email:str,  db_session:AsyncSession):
    async with db_session as session:
        try:  

            DeleteAccount, e = await user_datastore.DeleteAccount(email,  session)
            if e != None:
                raise Exception(f"{e}")
            
            await session.commit()

            return DeleteAccount, None


        except Exception as e:
            return None, e




