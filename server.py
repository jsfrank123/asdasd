from flask import Flask, render_template
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_video/<video_id>")
def get_video(video_id):
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"
    youtube_video = YouTube(youtube_url)
    video_url = youtube_video.streams.get_highest_resolution().url
    return render_template("index.html", video_url=video_url)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_video/<video_id>")
def get_video(video_id):
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"
    youtube_video = YouTube(youtube_url)
    video_title = youtube_video.title
    video_streams = youtube_video.streams.filter(progressive=True)
    return render_template("index.html", video_title=video_title, video_streams=video_streams)  

if __name__ == "__main__":
    app.run(port=8080)
