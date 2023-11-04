from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_video_or_audio(url, file_type='mp4'):
    yt = YouTube(url)

    if file_type == 'mp4':
        video = yt.streams.filter(file_extension='mp4', progressive=True).first()
        video.download()
        print("The video download is complete.")
    elif file_type == 'mp3':
        audio = yt.streams.filter(only_audio=True).first()
        audio.download()
        print("Audio (mp3) download complete.")
    else:
        print("Invalid file type")

def load_video_info(url):
    video = VideoFileClip(url)
    print(f"ชื่อวิดีโอ: {video.filename}")
    print(f"ความยาวของวิดีโอ: {video.duration} วินาที")
    print(f"ขนาดของวิดีโอ: {video.size}")

# รับ URL จากผู้ใช้
url = input("Please enter the video or audio URL: ")

# เลือกประเภทไฟล์ที่ต้องการดาวน์โหลด
file_type = input("Select the file type you want to download (mp4 or mp3): ")

# ใช้ฟังก์ชันดาวน์โหลดและแสดงข้อมูลของวิดีโอ
download_video_or_audio(url, file_type)
load_video_info(url)
