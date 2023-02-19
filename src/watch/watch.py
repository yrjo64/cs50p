import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(s: str) -> str:
    """
    parse
    1. First, it checks if the source attribute is present in the video tag.
    2. If it is present, it checks if the source attribute is a valid youtube URL.
    3. If it is, it extracts the video ID from the URL and returns the URL to the youtube video.
    4. If the source attribute is not present or is not a valid youtube URL, it returns None.

    Args:
        s (str): A HTML fragment  containg src atribute

    Returns:
        str: URL to youtube video
    """
    if source_match := re.search(r'src="(.+?)"', s, re.IGNORECASE):
        source = source_match.group(1)
        if matches := re.search(
            r"^https?://(?:www\.)?youtube\.com/embed/(.+)$", source, re.IGNORECASE
        ):
            vid = matches.group(1)
            tube: str = f"https://youtu.be/{vid}"
            return tube


if __name__ == "__main__":
    main()
