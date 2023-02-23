from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

templates = Jinja2Templates(directory="templates")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") 

app = FastAPI()
users = [
    {'username': 'truc', 'password': '123456'},
    {'username': 'test', 'password': '123456'},
]
@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == "truc" and password == "123456":
         return templates.TemplateResponse("Interface.html", {"request": request})
    else:
        return {"message": "Invalid username or password"}

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})
