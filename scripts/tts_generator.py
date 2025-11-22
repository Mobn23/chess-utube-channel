# scripts/tts_generator.py

from pathlib import Path
from gtts import gTTS


def text_to_speech(text: str, output_path: str, lang: str = "en"):
    """
    Convert text to speech using gTTS (Google Text-to-Speech)
    and save as MP3.

    - text: النص اللي بدك تحوّله لصوت.
    - output_path: مسار ملف الـ mp3 اللي بدك تحفظه.
    - lang: لغة الصوت (افتراضياً إنكليزي "en").
    """
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    # important: slow=False عشان يحكي طبيعي أسرع
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(str(out))
    print(f"[TTS] Saved audio to {out}")


if __name__ == "__main__":
    sample_text = (
        "In chess, just like in life, a quiet move can sometimes be the strongest one. "
        "This is a test of the free chess wisdom voice using gTTS."
    )
    text_to_speech(sample_text, "output/test_voice.mp3")
    print("Done.")
