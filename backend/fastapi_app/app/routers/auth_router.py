from fastapi import APIRouter, status, HTTPException
from fastapi_app.app.database import Session, ENGINE
from fastapi_app.app.models import User
from fastapi_app.app.schemas import RegisterSchema,  LoginSchema
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi.encoders import jsonable_encoder

session = Session(bind=ENGINE)
auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.get("/")
async def auth():
    return {"message": "Auth Page"}


@auth_router.post("/login")
async def auth_login_user(request: LoginSchema):
    check_user = session.query(User).filter(
        or_(
            User.username == request.username_or_email,
            User.email == request.username_or_email
        )
    ).first()
    if check_user and check_password_hash(check_user.password, request.password):
        return HTTPException(status_code=status.HTTP_200_OK, detail="User logged in")

    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")


@auth_router.post("/register")
async def register(request: RegisterSchema):
    check_user = session.query(User).filter(
        or_(User.username == request.username, User.email == request.email)).first()
    if check_user:
        return {"message": "username or email already exists"}

    new_user = User(
        username=request.username,
        email=request.email,
        password=generate_password_hash(request.password),
    )
    session.add(new_user)
    session.commit()
    return HTTPException(status_code=status.HTTP_201_CREATED, detail="User registered successfully")


@auth_router.get("/users")
async def users():
    users = session.query(User).all()
    return jsonable_encoder(users)

