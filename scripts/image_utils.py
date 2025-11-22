# scripts/image_utils.py

from pathlib import Path
from typing import Tuple

from PIL import Image, ImageDraw, ImageFont
import textwrap


def _load_font(font_size: int) -> ImageFont.FreeTypeFont:
    """
    Tries to load a TTF font; falls back to default.
    """
    # حاول تستخدم خط معروف، لو ما لقيته نرجع للـ default
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, font_size)
        except Exception:
            continue

    # fallback
    return ImageFont.load_default()


def create_captioned_image(
    base_image_path: str,
    text: str,
    output_path: str,
    max_chars: int = 180,
    margin: int = 40,
    box_opacity: int = 180,
) -> str:
    """
    Draw wrapped text onto a copy of the base image and save it.

    - base_image_path: صورة الخلفية الأصلية
    - text: النص اللي راح ينكتب على الصورة
    - output_path: مكان حفظ الصورة الجديدة
    - max_chars: أقصى عدد أحرف نعرضه على الصورة
    - margin: المسافة من حواف الصورة
    - box_opacity: شفافية الخلفية السوداء خلف النص (0-255)
    """

    base_path = Path(base_image_path)
    out_path = Path(output_path)

    if not base_path.exists():
        raise FileNotFoundError(f"Base image not found: {base_path}")

    # قص النص إذا كان طويل
    if len(text) > max_chars:
        text = text[: max_chars - 3] + "..."

    # افتح الصورة
    img = Image.open(base_path).convert("RGBA")
    width, height = img.size

    # نعمل طبقة شفافة للرسم
    txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)

    # إعداد الخط
    font_size = max(24, width // 25)
    font = _load_font(font_size)

    # نلف النص (wrap) بحسب عرض الصورة
    # التجريب: نخلي كل سطر تقريباً بعرض 40-50 حرف
    wrapped = textwrap.fill(text, width=40)

    # نحسب حجم تكست بلوك
    text_bbox = draw.multiline_textbbox((0, 0), wrapped, font=font)
    text_w = text_bbox[2] - text_bbox[0]
    text_h = text_bbox[3] - text_bbox[1]

    # نخلي الصندوق تحت في الصورة
    x = margin
    y = height - text_h - margin

    # خلفية سوداء شفافة تحت النص
    box_x0 = x - 20
    box_y0 = y - 20
    box_x1 = x + text_w + 20
    box_y1 = y + text_h + 20

    box_color = (0, 0, 0, box_opacity)  # أسود شبه شفاف
    draw.rectangle([box_x0, box_y0, box_x1, box_y1], fill=box_color)

    # نرسم النص بالأبيض
    draw.multiline_text((x, y), wrapped, font=font, fill=(255, 255, 255, 255))

    # دمج الطبقات
    combined = Image.alpha_composite(img, txt_layer).convert("RGB")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    combined.save(out_path, format="JPEG")
    return str(out_path)
