from models import user_models
from sqlalchemy import select, or_, and_, update, delete
from api import user_api

async def registNewAccount(data, session):
    try:
        paramsInsert = user_models.Users(
            email = data.email,
            password= data.password,
            role = data.role
        )

        session.add(paramsInsert)
        return data, None
    except Exception as e:
        return data, e
    
async def getListNewAccount(page, limit, keyword, session):
    try:
        terms = []
        if keyword not in (None, ""):
            terms.append(
                or_(
                    (user_models.Users.email.ilike(f"%{keyword.lower()}%")),
                    (user_models.Users.role.ilike(f"%{keyword.lower()}%"))
                )
            )

        offset = (page*limit)
        sql = select(user_models.Users).filter(and_(*(terms))).offset(offset).limit(limit)
        proxy_rows = await session.execute(sql)
        data = proxy_rows.scalars().all()
        
        return data, None
    except Exception as e:
        return data, e
    
async def regisUserDetail(data, session):
    try:
        paramsInsert = user_models.UsersDetail(
            email = data.email,
            nomor_identitas = data.nomor_identitas,
            nama_lengkap = data.nama_lengkap,
            tanggal_lahir = data.tanggal_lahir,
            alamat = data.alamat,
            nomor_telepon = data.nomor_telepon

        )

        session.add(paramsInsert)
        return data, None
    except Exception as e:
        return data, e
    
async def getListUserDetail(page, limit, keyword, session):
    try:
        terms = []
        if keyword not in (None, ""):
            terms.append(
                or_(
                    (user_models.UsersDetail.email.ilike(f"%{keyword.lower()}%")),
                    (user_models.UsersDetail.nama_lengkap.ilike(f"%{keyword.lower()}%"))
                )
            )

        offset = (page*limit)
        sql = select(user_models.UsersDetail).filter(and_(*(terms))).offset(offset).limit(limit)
        proxy_rows = await session.execute(sql)
        data = proxy_rows.scalars().all()
        
        return data, None
    except Exception as e:
        return data, e

async def GetUserDetailByEmail(keyword, session):
    try:
        sql = select(user_models.UsersDetail).where(user_models.UsersDetail.email == keyword)
        proxy_rows = await session.execute(sql)
        data = proxy_rows.scalars().first()
        
        return data, None
    except Exception as e:
        return None, e
    
async def UpdateUserDetailByEmail(email, nomor_telepon, session):
    try:
        terms = []
        if email not in (None, ""):
            terms.append(
                or_(
                    (user_models.UsersDetail.email.ilike(f"%{email.lower()}%")),
                )
            )

        sql =(
            update(user_models.UsersDetail)
            .where(user_models.UsersDetail.email == email)
            .values(nomor_telepon = nomor_telepon)
        )
        await session.execute(sql)
        await session.commit()
        
        return nomor_telepon, None
    except Exception as e:
        return None, e
    
async def DeleteAccount(email, session) :
    try:
        sql =(
        delete(user_models.UsersDetail)
        .where(user_models.UsersDetail.email == email)
        )
        await session.execute(sql)
        await session.commit()
        
        return email, None
    except Exception as e:
        return None, e
    

