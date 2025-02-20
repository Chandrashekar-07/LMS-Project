from fastapi import FastAPI
from routers import app as api_router

app = FastAPI()

# Include the routers for API endpoints
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="172.10.14.1", port=8000)
