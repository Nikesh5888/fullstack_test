from fastapi import APIRouter, Query, Request
from fastapi.responses import HTMLResponse
from app.flight_data_generator import flight_data
from fastapi.templating import Jinja2Templates
from datetime import date

router = APIRouter()
templates = Jinja2Templates(directory="frontend/templates")

@router.get("/flights", response_class=HTMLResponse)
async def get_flights(
    request: Request,
    source: str = Query(...), 
    sink: str = Query(...), 
    departure_date: date = Query(...), 
    return_date: date = Query(...)
):
    flights = flight_data(source, sink, departure_date, return_date)
    return templates.TemplateResponse("flight_results.html", {"request": request, "flights": flights})


# from fastapi import APIRouter
# from datetime import date
# from app.flight_data_generator import flight_data

# router = APIRouter()

# @router.get("/flights")
# async def get_flights(source: str, sink: str, departure_date: date, return_date: date):
#     flights = flight_data(source, sink, departure_date, return_date)
#     return flights
