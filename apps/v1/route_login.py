import json

from fastapi import APIRouter, Request, Form, Depends, responses, status
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from sqlalchemy.orm import Session

from core.security import create_access_token
from db.repository.user import create_new_user, get_user_by_email
from db.session import get_db
from schema.user import UserCreate

from api.v1.route_login import authenticate_user

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})

@router.post("/register")
def register(request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    errors = []
    try:
        user = UserCreate(email=email, password=password)
        if get_user_by_email(email=user.email, db=db):
            errors.append("User already registered")
            return templates.TemplateResponse("auth/register.html", {"request": request, "errors": errors})
        create_new_user(user, db)
        return responses.RedirectResponse(url="/?alert=Account created successfully", status_code=status.HTTP_302_FOUND)
    except ValidationError as e:
        errors_list = json.loads(e.json())
        for error in errors_list:
            errors.append(error['loc'][0] + ": " + error['msg'])
        return templates.TemplateResponse("auth/register.html", {"request": request, "errors": errors})

@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})

@router.post("/login")
def login(request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    errors = []
    if not authenticate_user(email, password, db):
        errors.append("Invalid credentials")
        return templates.TemplateResponse("auth/login.html", {"request": request, "errors": errors, "email": email})
    response = responses.RedirectResponse(url="/?alert=Logged in successfully", status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="access_token", value=f"Bearer {create_access_token(data={'sub': email})}")
    return response