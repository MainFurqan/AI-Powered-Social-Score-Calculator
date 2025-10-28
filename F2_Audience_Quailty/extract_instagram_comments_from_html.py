from bs4 import BeautifulSoup
import csv

# === CONFIGURATION ===
INPUT_HTML = "index.html"             # Path to your downloaded Instagram HTML file
OUTPUT_CSV = "instagram_comments.csv" # Output CSV file name

# === STEP 1: LOAD HTML ===
with open(INPUT_HTML, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# === STEP 2: EXTRACT USERNAMES AND COMMENTS ===
comments_data = []

# Find all user blocks that seem like top-level comments
for block in soup.find_all("div", class_="x1lliihq"):
    username_tag = block.find("a", href=True)
    if not username_tag:
        continue

    href = username_tag.get("href")
    if not href or not href.startswith("/") or href.count("/") != 2:
        continue  # Skip invalid or nested links

    username = href.strip("/")
    comment_span = block.find_next("span")
    comment_text = comment_span.get_text(strip=True) if comment_span else ""

    # Basic filtering
    if username and comment_text and not comment_text.lower().startswith("reply"):
        comments_data.append((username, comment_text))

# === STEP 3: SAVE TO CSV ===
with open(OUTPUT_CSV, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Username", "Comment"])
    writer.writerows(comments_data)

print(f"✅ Extracted {len(comments_data)} comments and saved to {OUTPUT_CSV}")
