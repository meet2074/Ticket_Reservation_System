from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from src.schemas.user_schemas.login import Login
from functions.user_functions.sign_up import access_token_create_login, create_refresh_token
from database import database
from functions.user_functions.login import login_user
import src.schemas.user_schemas.sign_up as schemas


router = APIRouter()


@router.get("/login")
def login(login_data:Login,db:Session = Depends(database.get_db) ):
    login = login_user(db,login_data)
    if login:
        access_token = access_token_create_login(login_data.email, db)
        refresh_token = create_refresh_token(login_data.email,db)
    return {"access token": access_token, "Refresh token": refresh_token}
    