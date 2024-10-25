import os
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import jwt
from datetime import datetime, timedelta
import bcrypt
import requests

# Configura do JWT
SECRET_KEY = os.getenv("SECRET_KEY", "SENHA_MUITO_BOA_UAU@!@#$")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Configurações do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db/dbname")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo de dados para a requisição
class User(BaseModel):
    nome: str
    email: str
    senha: str

# Modelo de dados para a requisição de login
class Login(BaseModel):
    email: str
    senha: str

# Modelo de dados para o banco de dados
class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    nome = Column(String(50))
    email = Column(String(50), unique=True)
    hashed_password = Column(String(100))

# Inicializar a aplicação FastAPI
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Função para criar um token JWT
def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"iat": datetime.utcnow()})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Função para verificar o token JWT
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Token inválido")

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para registrar o usuário
@app.post("/registrar")
def registrar(user: User, db: Session = Depends(get_db)):
    # Verificar se o email já existe no banco de dados
    db_user = db.query(UserDB).filter(UserDB.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=409, detail="Email já registrado")

    # Hashear a senha do usuário
    hashed_password = bcrypt.hashpw(user.senha.encode('utf-8'), bcrypt.gensalt())

    # Criar um novo usuário no banco de dados
    new_user = UserDB(nome=user.nome, email=user.email, hashed_password=hashed_password.decode('utf-8'))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Dados para o token JWT
    token_data = {
        "email": user.email,
        "nome": user.nome
    }

    # Criar o token JWT
    jwt_token = create_access_token(token_data)

    # Retornar a resposta com o token JWT
    return {"jwt": jwt_token}

# Endpoint para autenticar o usuário
@app.post("/login")
def login(login: Login, db: Session = Depends(get_db)):
    # Verificar se o email existe no banco de dados
    db_user = db.query(UserDB).filter(UserDB.email == login.email).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")

    # Verificar se a senha está correta
    if not bcrypt.checkpw(login.senha.encode('utf-8'), db_user.hashed_password.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")

    # Dados para o token JWT
    token_data = {
        "email": login.email,
        "nome": db_user.nome
    }

    # Criar o token JWT
    jwt_token = create_access_token(token_data)

    # Retornar a resposta com o token JWT
    return {"jwt": jwt_token}

# Endpoint para consultar dados
@app.get("/consultar")
def consultar(request: Request, token: str = Depends(oauth2_scheme)):
    # Verificar o token JWT
    payload = verify_token(token)

    # Realizar a requisição à API do Open-Meteo
    url = "https://api.open-meteo.com/v1/forecast?latitude=-46.67&longitude=-23.59&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Erro ao consultar a API de dados")

    try:
        # Extrair os dados desejados
        data = response.json()
    except ValueError:
        raise HTTPException(status_code=500, detail="Erro ao decodificar a resposta JSON")

    # Reformatar os dados
    hourly_data = data["hourly"]
    formatted_data = {
        "latitude": data.get("latitude"),
        "longitude": data.get("longitude"),
        "timezone": data.get("timezone"),
        "current": {
            "time": data["current"].get("time"),
            "temperature_2m": data["current"].get("temperature_2m"),
            "wind_speed_10m": data["current"].get("wind_speed_10m")
        },
        "hourly": [
            {
                "time": time,
                "temperature_2m": temp,
                "relative_humidity_2m": humidity,
                "wind_speed_10m": wind_speed
            }
            for time, temp, humidity, wind_speed in zip(
                hourly_data["time"],
                hourly_data["temperature_2m"],
                hourly_data["relative_humidity_2m"],
                hourly_data["wind_speed_10m"]
            )
        ]
    }

    # Retornar os dados formatados
    return formatted_data

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)