from fastapi import FastAPI
from app.routers import posts, users, login, analytics

app = FastAPI()


@app.get("/")
async def health_check():
    return {"Hello": "World"}

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
app.include_router(login.router, tags=["login"])
