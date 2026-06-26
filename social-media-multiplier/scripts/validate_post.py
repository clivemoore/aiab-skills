#!/usr/bin/env python3
"""
validate_post.py — platform constraint checker for the social-media-multiplier skill.

Enforces the skill's hard rules so character limits and hashtag bans are caught
mechanically instead of by eye:

  - X/Twitter:  <= 280 chars
  - Bluesky:    <= 300 chars per post (flags need-to-thread)
  - Threads / Bluesky / eh.social: NO hashtags
  - LinkedIn:   no hashtags in body, no raw URLs in body

Usage:
    python3 validate_post.py --platform x --file post.txt
    echo "my post text" | python3 validate_post.py --platform bluesky
    python3 validate_post.py --platform threads --text "lowercase thought here"

Exit code 0 = all checks pass, 1 = one or more violations.
"""
import argparse
import re
import sys

LIMITS = {"x": 280, "twitter": 280, "bluesky": 300}
NO_HASHTAG = {"threads", "bluesky", "eh.social", "ehsocial", "eh"}
URL_RE = re.compile(r"https?://\S+")
HASHTAG_RE = re.compile(r"(?:^|\s)#\w+")


def check(platform: str, text: str):
    platform = platform.lower()
    violations = []
    n = len(text)

    limit = LIMITS.get(platform)
    if limit and n > limit:
        violations.append(f"length {n} > {limit} hard limit")
    if platform in ("bluesky",) and n > 300:
        violations.append("exceeds 300 — split into a thread")

    if platform in NO_HASHTAG and HASHTAG_RE.search(text):
        violations.append("hashtags are not allowed on this platform")

    if platform == "linkedin":
        if HASHTAG_RE.search(text):
            violations.append("no hashtags in LinkedIn body — first comment only")
        if URL_RE.search(text):
            violations.append('no raw URLs in LinkedIn body — use "link in comments"')

    if platform in ("threads", "bluesky", "eh.social", "ehsocial", "eh"):
        letters = [c for c in text if c.isalpha()]
        if letters and sum(c.isupper() for c in letters) / len(letters) > 0.3:
            violations.append("should be lowercase/conversational for this platform")

    return n, limit, violations


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--platform", required=True)
    ap.add_argument("--file")
    ap.add_argument("--text")
    args = ap.parse_args()

    if args.text is not None:
        text = args.text
    elif args.file:
        with open(args.file, encoding="utf-8") as f:
            text = f.read().strip()
    else:
        text = sys.stdin.read().strip()

    n, limit, violations = check(args.platform, text)
    cap = f"/{limit}" if limit else ""
    print(f"[{args.platform}] {n}{cap} chars")
    if violations:
        for v in violations:
            print(f"  ✗ {v}")
        sys.exit(1)
    print("  ✓ passes")
    sys.exit(0)


if __name__ == "__main__":
    main()
