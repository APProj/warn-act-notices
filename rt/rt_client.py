#!/usr/bin/env python3
"""WARN Feed paid-tier client — no account, no login, just your Gumroad license key.

    pip install cryptography
    WARN_LICENSE_KEY=XXXXXXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX python3 rt_client.py realtime > held_back.csv
    WARN_LICENSE_KEY=...                                  python3 rt_client.py archive  > warn-archive.zip

'realtime' = CSV of every notice the free files are still holding back (48h delay),
regenerated on every refresh. 'archive' = the latest monthly archive ZIP.
Everything is fetched from the public site and decrypted locally with your key.
Exit 2 = no active licence for that key (typo, refunded, or purchase not yet
processed — new purchases activate at the next refresh, within 24h).
"""
import base64, hashlib, json, os, sys, urllib.request
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

BASE = os.environ.get("WARN_FEED_BASE", "https://apventureengine.github.io/warn-act-notices/rt/")


def get(path):
    with urllib.request.urlopen(BASE + path, timeout=60) as r:
        return r.read()


def open_(key, data):
    assert data[:4] == b"WFE1", "unexpected file format"
    return AESGCM(key).decrypt(data[4:16], data[16:], None)


def main():
    lk = os.environ.get("WARN_LICENSE_KEY", "").strip()
    want = sys.argv[1] if len(sys.argv) > 1 else "realtime"
    if not lk:
        sys.exit("set WARN_LICENSE_KEY (it is on your Gumroad receipt)")
    try:
        w = json.loads(get("k/" + hashlib.sha256(lk.encode()).hexdigest() + ".json"))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            sys.stderr.write("no active licence for that key\n"); sys.exit(2)
        raise
    if w["product"] != want:
        sys.exit(f"this key unlocks '{w['product']}', not '{want}'")
    kek = hashlib.pbkdf2_hmac("sha256", lk.encode(), base64.b64decode(w["salt"]), int(w["iter"]), 32)
    mk = open_(kek, b"WFE1" + base64.b64decode(w["iv"]) + base64.b64decode(w["ct"]))
    sys.stdout.buffer.write(open_(mk, get(w["product"] + ".enc")))


if __name__ == "__main__":
    main()
