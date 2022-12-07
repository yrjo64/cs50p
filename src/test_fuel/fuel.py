def main():
    prompt: str = "Input: "
    while True:
        try:
            inp = input(prompt).strip()
            persentage = convert(inp)
        except (ValueError, ZeroDivisionError):
            continue

        tank = gauge(persentage)
        print(f"{tank}")


def convert(fraction):
    a, b = fraction.split("/")
    a = int(a)
    b = int(b)
    if a > b:
        raise ValueError
    if b == 0:
        raise ZeroDivisionError
    return round((a / b), 2) * 100


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    return f"{int(percentage)}%"


if __name__ == "__main__":
