from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return { "message": "Hello, World!", "url": "https://github.com/AWeirdScratcher/github-discussions-api" }
