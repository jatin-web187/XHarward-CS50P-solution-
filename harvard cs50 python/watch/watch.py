import re

def parse(s):
    # Only match <iframe src="https://www.youtube.com/embed/...">
    pattern = re.search(
        r'<iframe[^>]+src="https?://(?:www\.)?youtube\.com/embed/([\w-]+)"',
        s
    )
    if pattern:
        video_id = pattern.group(1)
        return f"https://youtu.be/{video_id}"
    return None

def main():
    html = input("HTML: ")
    print(parse(html))

if __name__ == "__main__":
    main()
    

