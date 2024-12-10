from pydantic import BaseModel,EmailStr


class SignUp(BaseModel):
    first_name: str
    middle_name: str = None
    last_name: str
    mobile_number: int
    email: EmailStr
    birthdate: str
    password: str
    
class Create_User_Otp(BaseModel):
    email: EmailStr
    otp: int


class Token_Schema(BaseModel):
    first_name: str
    userid: int