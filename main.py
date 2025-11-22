# main.py

from pathlib import Path

from scripts.script_generator import generate_chess_script
from scripts.tts_generator import text_to_speech
from scripts.video_maker import create_video_with_audio
from scripts.image_utils import create_captioned_image


def main():
    # 1) Generate script (نص جديد كل مرة)
    script = generate_chess_script()
    print("Generated script:\n", script)

    # 2) Generate audio from script
    audio_path = Path("output/daily_chess_voice.mp3")
    text_to_speech(script, str(audio_path))
    print(f"Audio saved to: {audio_path}")

    # 3) Create captioned image (نكتب النص على الصورة)
    base_image = "data/images/chess_bg.jpg"
    captioned_image_path = "output/daily_chess_image.jpg"
    create_captioned_image(
        base_image_path=base_image,
        text=script,
        output_path=captioned_image_path,
        max_chars=180,   # تحكم بطول النص المكتوب على الصورة
    )
    print(f"Captioned image saved to: {captioned_image_path}")

    # 4) Generate video (صورة عليها النص + صوت)
    video_path = Path("output/daily_chess_video.mp4")
    create_video_with_audio(
        image_path=captioned_image_path,
        audio_path=str(audio_path),
        output_path=str(video_path),
    )
    print(f"Video saved to: {video_path}")


if __name__ == "__main__":
    main()
