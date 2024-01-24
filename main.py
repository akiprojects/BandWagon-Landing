from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 정적 파일 경로 설정
app.mount("/css", StaticFiles(directory="templates/css"), name="css")
app.mount("/fonts", StaticFiles(directory="templates/fonts"), name="fonts")
app.mount("/images", StaticFiles(directory="templates/images"), name="images")
app.mount("/js", StaticFiles(directory="templates/js"), name="js")

# 템플릿 파일 경로 설정
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/service", response_class=HTMLResponse)
async def read_service(request: Request):
    return templates.TemplateResponse("service.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def read_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
