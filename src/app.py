from fastapi import FastAPI
from src.api.user_api.sign_up  import router as sign_up_router
from src.api.user_api.login import router as login_router
import uvicorn

app = FastAPI()

app.include_router(login_router)
app.include_router(sign_up_router)


