from fastapi import APIRouter, HTTPException, Request, Form, Depends, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from deta import Deta
from pydantic.dataclasses import dataclass

deta = Deta()

home_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@home_router.get("/")
async def home(request: Request):

    context = {"request": request}
    return templates.TemplateResponse("general_pages/homepage.html", context)


@dataclass
class GetName:
    BaseName: str = Form(...)


@home_router.post("/")
async def generate(request: Request, form_data: GetName = Depends()):

    dbname = form_data.BaseName.split()[0]
    db = deta.Base(dbname)
    fetchdb = db.fetch()
    all_items = fetchdb.items

    if len(all_items) > 0:
        context = {"request": request, "all_items": all_items, "dbname": dbname}
        return templates.TemplateResponse("general_pages/table.html", context)

    else:
        # raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
        # detail="DOESNT EXIST")
        context = {"request": request, "db": dbname}
        return templates.TemplateResponse("general_pages/NOK.html", context)
