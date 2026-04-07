import csv
import secrets

BASE_URL = "https://yorozuya667.github.io/"
INPUT_FILE = "guests.csv"
OUTPUT_FILE = "guests_out.csv"

with open(INPUT_FILE, "r", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

fieldnames = ["guest_name", "token", "link", "status"]

for row in rows:
    token = (row.get("token") or "").strip().upper()
    if not token:
        token = secrets.token_hex(6).upper()  # 12 hex chars
    row["token"] = token
    row["link"] = f"{BASE_URL}?token={token}"
    row["status"] = row.get("status", "")

with open(OUTPUT_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Готово: {OUTPUT_FILE}")