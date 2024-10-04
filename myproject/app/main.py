from fastapi import FastAPI
from model import generate_blog_titles

app = FastAPI()

@app.post("/generate-titles/")
async def generate_titles(content: str):
    try:
        suggested_titles = generate_blog_titles(content)
        return {"suggested_titles": suggested_titles}
    except Exception as e:
        return {"error": str(e)}