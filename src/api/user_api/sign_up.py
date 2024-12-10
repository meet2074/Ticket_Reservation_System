from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import database
import src.schemas.user_schemas.sign_up as schemas
from functions.user_functions.sign_up import create_user,verify_otp,delete_otp,access_token_create_login,create_refresh_token


router = APIRouter()

@router.post("/sign-up")
async def user_create(user: schemas.SignUp, db: Session = Depends(database.get_db)):
    await create_user(db,user)
    return f"Otp sent successfully on {user.email}!"

@router.post("/verify-otp")
def check_otp(data: schemas.Create_User_Otp, db: Session = Depends(database.get_db)):
    is_correct = verify_otp(data, db)   
    if is_correct:
        delete_otp(db, is_correct)
        # payload = get_user_by_id(db, is_correct)
        token = access_token_create_login(data.email,db)
        # breakpoint()
        refresh_token = create_refresh_token(data.email,db)
        return {"message": "Account created Successfully!! ", "access token": token,"refresh token":refresh_token}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect Otp!")
    
     