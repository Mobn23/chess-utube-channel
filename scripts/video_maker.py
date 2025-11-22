# scripts/video_maker.py

from moviepy.editor import ImageClip, AudioFileClip
from pathlib import Path


def create_video_with_audio(
    image_path: str,
    audio_path: str,
    output_path: str,
):
    """
    Create a simple video: static image + audio.
    """

    image_file = Path(image_path)
    audio_file = Path(audio_path)
    out_file = Path(output_path)

    assert image_file.exists(), f"Background image not found: {image_file}"
    assert audio_file.exists(), f"Audio file not found: {audio_file}"

    audio_clip = AudioFileClip(str(audio_file))
    duration = audio_clip.duration

    img_clip = ImageClip(str(image_file)).set_duration(duration).set_fps(30)
    video = img_clip.set_audio(audio_clip)

    out_file.parent.mkdir(parents=True, exist_ok=True)
    video.write_videofile(
        str(out_file),
        fps=30,
        codec="libx264",
        audio_codec="libmp3lame",
        temp_audiofile=str(out_file.with_suffix(".temp-audio.mp3")),
        remove_temp=True,
    )


if __name__ == "__main__":
    create_video_with_audio(
        image_path="data/images/chess_bg.jpg",
        audio_path="output/test_voice.mp3",
        output_path="output/test_video.mp4",
    )
    print("Video generated at output/test_video.mp4")
