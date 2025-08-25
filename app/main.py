from fastapi import FastAPI
from app.routes import states, commissions, cases

app = FastAPI(title="Lexi DCDRC API", version="1.0")

# Routers
app.include_router(states.router, prefix="/states", tags=["States"])
app.include_router(commissions.router, prefix="/commissions", tags=["Commissions"])
app.include_router(cases.router, prefix="/cases", tags=["Cases"])

@app.get("/")
def root():
    return {"message": "Lexi DCDRC API is running 🚀"}
