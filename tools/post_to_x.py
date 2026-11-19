#!/usr/bin/env python3
"""Post the meme to X from @Didinska0610 — the single entry post for
make.fun's gta6-meme-x-01 bounty.

Auth: the owner's session cookies, read at run time from
~/workspace/x-session/x_cookies.json (keys: auth_token, ct0). Values are
never printed, logged or written anywhere.

Media upload uses the proven chunked flow against the API host
(https://upload.twitter.com/1.1/media/upload.json):
  INIT     form fields  {command, total_bytes, media_type, media_category}
  APPEND   multipart    {command, media_id, segment_index, media=<bytes>}
  FINALIZE form fields  {command, media_id}
with the web bearer + x-csrf-token (ct0) headers. The /i/media/upload.json
path refuses this session (403), so it is not used.

The tweet itself is created with the GraphQL CreateTweet call implemented
in ~/workspace/superteam/x_api.py (gql_post), reusing its cached feature
flags. If CreateTweet returns no tweet id (a silent drop), the script
waits about two minutes and retries exactly once with the same media_id.

    python3 tools/post_to_x.py
"""
import json
import os
import sys
import time
import urllib.parse

sys.path.insert(0, os.path.expanduser("~/workspace/superteam"))

COOKIES_PATH = os.path.expanduser("~/workspace/x-session/x_cookies.json")
IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "..", "meme", "final.png")
UPLOAD_URL = "https://upload.twitter.com/1.1/media/upload.json"

POST_TEXT = (
    "Waited 13 years for GTA VI. My AI agent didn't wait at all \u2014 it "
    "earns real money entering @makefunai bounties (this meme is one of "
    "them). \U0001F47B\n"
    "https://make.fun/bounty/gta6-meme-x-01\n"
    "makefun-beach-ballroom-statue"
)


def load_cookies():
    with open(COOKIES_PATH) as f:
        c = json.load(f)
    os.environ["X_AUTH_TOKEN"] = c["auth_token"]
    os.environ["X_CT0"] = c["ct0"]


def upload_media(x_api, path):
    size = os.path.getsize(path)
    form = {"content-type": "application/x-www-form-urlencoded"}
    st, js = x_api.raw(UPLOAD_URL, data=urllib.parse.urlencode({
        "command": "INIT", "total_bytes": size, "media_type": "image/png",
        "media_category": "tweet_image"}).encode(),
        hdrs=x_api.headers(form))
    if st not in (200, 201, 202):
        raise RuntimeError(f"INIT failed: HTTP {st} {str(js)[:200]}")
    mid = js["media_id_string"]

    with open(path, "rb") as f:
        blob = f.read()
    boundary = "----memeboundary42"
    parts = []
    for name, val in (("command", "APPEND"), ("media_id", mid),
                      ("segment_index", "0")):
        parts.append(f"--{boundary}\r\nContent-Disposition: form-data; "
                     f"name=\"{name}\"\r\n\r\n{val}\r\n".encode())
    parts.append(f"--{boundary}\r\nContent-Disposition: form-data; "
                 f"name=\"media\"; filename=\"final.png\"\r\n"
                 f"Content-Type: image/png\r\n\r\n".encode() + blob + b"\r\n")
    parts.append(f"--{boundary}--\r\n".encode())
    st, js = x_api.raw(UPLOAD_URL, data=b"".join(parts),
                       hdrs=x_api.headers(
                           {"content-type":
                            f"multipart/form-data; boundary={boundary}"}))
    if st not in (200, 204):
        raise RuntimeError(f"APPEND failed: HTTP {st} {str(js)[:200]}")

    st, js = x_api.raw(UPLOAD_URL, data=urllib.parse.urlencode({
        "command": "FINALIZE", "media_id": mid}).encode(),
        hdrs=x_api.headers(form))
    if st not in (200, 201):
        raise RuntimeError(f"FINALIZE failed: HTTP {st} {str(js)[:200]}")
    return mid


def main():
    load_cookies()
    import x_api  # reads X_AUTH_TOKEN / X_CT0 from the environment

    media_id = upload_media(x_api, IMAGE_PATH)
    print("media uploaded:", media_id)

    st, rid, js = x_api.gql_post(POST_TEXT, media_id=media_id)
    print("CreateTweet HTTP", st, "tweet id:", rid)
    if not rid:
        print("no tweet id (silent drop?) — waiting ~2 min, one retry")
        time.sleep(120)
        st, rid, js = x_api.gql_post(POST_TEXT, media_id=media_id)
        print("retry CreateTweet HTTP", st, "tweet id:", rid)
    if not rid:
        print("FAILED: no tweet id after one retry")
        print("errors:", json.dumps(js.get("errors", ""))[:300])
        return 1
    print("POST_URL https://x.com/Didinska0610/status/" + rid)
    return 0


if __name__ == "__main__":
    sys.exit(main())
