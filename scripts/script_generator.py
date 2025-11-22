# scripts/script_generator.py

import random
from datetime import datetime

CHESS_TEMPLATES = [
    "In this position, it looks like White is under pressure, but a quiet move changes everything. "
    "Just like in life, sometimes the strongest move is the one nobody expects.",

    "This pawn looks small and weak, but it controls key squares. "
    "In chess and in life, the smallest step can block the biggest threat.",

    "Here, Black sacrifices a piece to open lines to the king. "
    "Sometimes you must give up something now to gain a winning attack later.",

    "Notice how all the pieces work together here. "
    "A single strong piece cannot win alone, just like one person cannot fight every battle alone.",

    "Instead of rushing to attack, White improves the worst placed piece first. "
    "In life, fixing your weakest point is often more important than showing your strengths."
]

def generate_chess_script() -> str:
    """Generate a short chess 'wisdom' script (10–20s)."""
    base = random.choice(CHESS_TEMPLATES)
    return base


if __name__ == "__main__":
    print(generate_chess_script())
