from src.config import Env
from sqlalchemy.orm import Session
from models.user_models.sign_up_model import User,OTP
from src.schemas.user_schemas.login import Login
from src.utils.hash import hash_password, verify_password
from fastapi import HTTPException, Depends, status

def login_user(db:Session,login_data:Login):
    # breakpoint()
    data = db.query(User).filter(User.email == login_data.email).one_or_none()
    
    if data is None or data.is_deleted:
        raise HTTPException(status_code=404, detail="Invalid Email id!")
    is_otp = db.query(OTP).filter(OTP.user_id==data.id).one_or_none()
    if is_otp:
        raise HTTPException(status_code=401,detail="Please verify the otp")   
    hashed_pass = data.password
    if verify_password(login_data.password, hashed_pass):
        data.is_active = True
        return True
    else:
        raise HTTPException(status_code=401, detail="Incorrect password!!")
    
            
