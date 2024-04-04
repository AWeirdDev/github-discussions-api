import requests
from fastapi import FastAPI

r = requests.get("https://gist.githubusercontent.com/AWeirdScratcher/fbb1cbf0950c16a77ffef3897b050723/raw/fec5e8bc217d1bcca9e4b7b350ffff9b08a48b1f/main.py")
code = r.text

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0"

app = FastAPI()

@app.get('/')
async def index():
  return { "message": "hi" }

@app.get('/body')
async def get_body(url: str):
  r = requests.post("https://try.playwright.tech/service/control/run", json={ "code": code.replace("{{ url }}", url), "language": "python" }, headers={"User-Agent": user_agent})
  r.raise_for_status()
  return { "body": r.json()['output'] }
