from fastapi import FastAPI
from .routers.auth_router import auth_router
from .routers.post_router import post_router
from .routers.comment_router import comment_router
from .routers.like_router import like_router
from .routers.follow_router import follow_router


app = FastAPI()
app.include_router(auth_router)
app.include_router(post_router)
app.include_router(comment_router)
app.include_router(like_router)
app.include_router(follow_router)


@app.get("/")
async def root():
    return {"message": "Home Page"}

