import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    """
    validate IP format

    Args:
        ip (str): Str composing IP4 value

    Returns:
        bool: True if valid
    """
    nums = re.split(r"\.", ip, 4)
    if len(nums) != 4:
        return False
    try:
        s1, s2, s3, s4 = nums
        n1 = int(s1)
        n2 = int(s2)
        n3 = int(s3)
        n4 = int(s4)
    except ValueError:
        return False
    if not (0 <= n1 <= 255):
        return False
    if not (0 <= n2 <= 255):
        return False
    if not (0 <= n3 <= 255):
        return False
    if not (0 <= n4 <= 255):
        return False
    return True


if __name__ == "__main__":
    main()
