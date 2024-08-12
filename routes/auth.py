from fastapi import APIRouter, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from utils.auth import create_jwt_token

router = APIRouter()
security = HTTPBasic()

@router.post("/token")
async def login(credentials: HTTPBasicCredentials):
    correct_username = "admin"
    correct_password = "admin"
    if credentials.username == correct_username and credentials.password == correct_password:
        token = create_jwt_token(credentials.username)
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Incorrect username or password")