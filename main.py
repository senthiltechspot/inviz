import logging
from fastapi import FastAPI
from routers import property

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(property.router)

@app.get("/")
async def home_route():
    logger.info("Home route accessed")
    return {"message": "API is Working"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
