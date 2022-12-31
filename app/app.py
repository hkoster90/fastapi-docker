from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/loaderio-683235867f40e8be022f38e69fd4ce93")
async def loaderio_683235867f40e8be022f38e69fd4ce93():
    return "loaderio-683235867f40e8be022f38e69fd4ce93"