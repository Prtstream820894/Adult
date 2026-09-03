from datetime import datetime
import urllib.request

URL_1 = "https://bitter-recipe-3d25.poonamchouhan076.workers.dev/"
URL_2 = "https://icy-pond-60ea.poonamchouhan076.workers.dev/"

OUTPUT_FILE = "merged_playlist.m3u"


def fetch_playlist(url):
  try:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
      return response.read().decode("utf-8", errors="ignore")
  except Exception as e:
    print(f"Error fetching {url}: {e}")
    return ""


def main():
  print("Fetching playlists...")
  content_1 = fetch_playlist(URL_1)
  content_2 = fetch_playlist(URL_2)

  merged_lines = []
  merged_lines.append("#EXTM3U\n")
  merged_lines.append(
      f"#EXTINF:-1, Last Updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC\n"
  )

  for line in content_1.splitlines():
    if line.strip() and not line.startswith("#EXTM3U"):
      merged_lines.append(line + "\n")

  for line in content_2.splitlines():
    if line.strip() and not line.startswith("#EXTM3U"):
      merged_lines.append(line + "\n")

  with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.writelines(merged_lines)

  print(f"Playlist successfully merged and saved to {OUTPUT_FILE}")


if __name__ == "__main__":
  main()
