from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import note_router

app = FastAPI()

# CORS (cho frontend gọi API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Test endpoints
@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

# Include router
app.include_router(note_router.router)