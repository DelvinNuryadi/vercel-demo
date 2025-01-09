from fastapi import fastAPI
app = FastAPI()

@app.get("/")
async def health_check():
    return "the health check is successfull!"