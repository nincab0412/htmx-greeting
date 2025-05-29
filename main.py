from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn
import yt_dlp

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


def get_audio_url(video_url):
    try:
        ydl_opts = {"format": "bestaudio", "quiet": True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            return info["url"]
    except Exception as e:
        return f"Error fetching audio: {str(e)}"


@app.get("/get-audio", response_class=HTMLResponse)
async def get_audio():
    video_url = "https://www.youtube.com/watch?v=3BFTio5296w"
    audio_url = get_audio_url(video_url)
    return HTMLResponse(
        f'<audio autoplay loop><source src="{audio_url}" type="audio/mpeg"></audio>'
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
