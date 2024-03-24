import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_hotel():
    return {"message": "HOTEL"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
