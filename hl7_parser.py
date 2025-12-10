# hl7_parser.py
from pathlib import Path

def load_hl7_from_file(path: str) -> str:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"HL7 file not found: {file_path}")
    return file_path.read_text(encoding="utf-8")

def split_segments(hl7_text: str):
    hl7_text = hl7_text.replace("\r\n", "\n").replace("\r", "\n")
    segments = [line for line in hl7_text.split("\n") if line.strip()]
    return segments

def parse_segment(segment_line: str):
    parts = segment_line.split("|")
    seg_name = parts[0]
    fields = parts[1:]
    return seg_name, fields
