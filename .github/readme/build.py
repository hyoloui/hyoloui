# template.md의 기간 자리표시자를 오늘(한국 시간) 기준으로 계산해 README.md를 만든다.
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LAUNCH = (2024, 8, 9)         # 어시스트핏 CRM 웹 정식 출시


def months_since(start, today):
    y, m, d = start
    n = (today.year - y) * 12 + today.month - m
    return n - 1 if today.day < d else n


def ko_period(n):
    y, m = divmod(n, 12)
    return " ".join(s for s in (f"{y}년" if y else "", f"{m}개월" if m else "") if s) or "1개월 미만"


today = datetime.now(timezone(timedelta(hours=9))).date()
text = (ROOT / ".github/readme/template.md").read_text(encoding="utf-8")
text = text.replace("{{OPERATING}}", ko_period(months_since(LAUNCH, today)))
(ROOT / "README.md").write_text(text, encoding="utf-8")
