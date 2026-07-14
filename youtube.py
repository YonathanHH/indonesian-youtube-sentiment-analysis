import os
import csv
import json
from datetime import datetime
from yt_dlp import YoutubeDL

# =========================
# CONFIG
# =========================
VIDEO_URL = "https://www.youtube.com/watch?v=v-1YabkN-pM"
OUTPUT_DIR = "output"

# Optional proxy
PROXY = ""  # example: "http://USERNAME:PASSWORD@HOST:PORT"

# Comment limit
MAX_COMMENTS = "all"

# Create output folder if it does not exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# =========================
# YT-DLP OPTIONS
# =========================
ydl_opts = {
    "skip_download": True,
    "quiet": True,
    "no_warnings": True,
    "getcomments": True,
    "ignore_no_formats_error": True,
    "extractor_args": {
        "youtube": {
            "max_comments": [str(MAX_COMMENTS)],
            "player_client": ["web_safari"],
        }
    },
    "outtmpl": os.path.join(OUTPUT_DIR, "%(id)s.%(ext)s"),
}

if PROXY:
    ydl_opts["proxy"] = PROXY

# =========================
# HELPERS
# =========================
def normalize_comment(c):
    return {
        "id": c.get("id"),
        "author": c.get("author"),
        "author_id": c.get("author_id"),
        "text": c.get("text"),
        "timestamp": c.get("timestamp"),
        "like_count": c.get("like_count"),
        "is_favorited": c.get("is_favorited"),
        "is_pinned": c.get("is_pinned"),
        "parent": c.get("parent"),
        "video_id": c.get("video_id"),
    }

# =========================
# MAIN
# =========================
with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(VIDEO_URL, download=False)

video_id = info.get("id")
title = info.get("title")
uploader = info.get("uploader")
upload_date = info.get("upload_date")

comments = info.get("comments") or info.get("comment_entries") or []
thread_count = info.get("comment_count") or info.get("n_comments") or len(comments)

rows = []
for c in comments:
    if isinstance(c, dict):
        rows.append(normalize_comment(c))

# =========================
# SAVE METADATA
# =========================
metadata = {
    "video_id": video_id,
    "title": title,
    "uploader": uploader,
    "upload_date": upload_date,
    "comment_count_reported": thread_count,
    "comments_extracted": len(rows),
    "scraped_at": datetime.now().isoformat(timespec="seconds"),
}

metadata_path = os.path.join(OUTPUT_DIR, f"{video_id}_metadata.json")
with open(metadata_path, "w", encoding="utf-8") as f:
    json.dump(metadata, f, ensure_ascii=False, indent=2)

# =========================
# SAVE COMMENTS TO CSV
# =========================
csv_path = os.path.join(OUTPUT_DIR, f"{video_id}_comments.csv")

fieldnames = [
    "id",
    "author",
    "author_id",
    "text",
    "timestamp",
    "like_count",
    "is_favorited",
    "is_pinned",
    "parent",
    "video_id",
]

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Video ID: {video_id}")
print(f"Title: {title}")
print(f"Reported comments: {thread_count}")
print(f"Extracted comments: {len(rows)}")
print(f"Saved metadata: {metadata_path}")
print(f"Saved CSV: {csv_path}")