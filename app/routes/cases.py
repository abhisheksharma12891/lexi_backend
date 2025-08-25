from fastapi import APIRouter, Depends
from app.models.requests import CaseSearchRequest
from app.models.responses import CasesResponse
from app.services.jagriti_service import search_cases

router = APIRouter()

@router.post("/by-case-number", response_model=CasesResponse)
def search_by_case_number(request: CaseSearchRequest):
    return search_cases("case_number", request)

@router.post("/by-complainant", response_model=CasesResponse)
def search_by_complainant(request: CaseSearchRequest):
    return search_cases("complainant", request)

@router.post("/by-respondent", response_model=CasesResponse)
def search_by_respondent(request: CaseSearchRequest):
    return search_cases("respondent", request)

@router.post("/by-complainant-advocate", response_model=CasesResponse)
def search_by_complainant_advocate(request: CaseSearchRequest):
    return search_cases("complainant_advocate", request)

@router.post("/by-respondent-advocate", response_model=CasesResponse)
def search_by_respondent_advocate(request: CaseSearchRequest):
    return search_cases("respondent_advocate", request)

@router.post("/by-industry-type", response_model=CasesResponse)
def search_by_industry_type(request: CaseSearchRequest):
    return search_cases("industry_type", request)

@router.post("/by-judge", response_model=CasesResponse)
def search_by_judge(request: CaseSearchRequest):
    return search_cases("judge", request)
