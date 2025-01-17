from fastapi import FastAPI
from app.api.user import router as user_router

app = FastAPI()

# 라우터 등록
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
