def main() -> None:
    inp: str = input("What time is it? ")
    time: float = convert(inp)
    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")
    
def convert(time: str) -> float:
    hourss: str, mins: str = time.split(":")
    hours: int = int(hourss)
    # chec for 12h clock
    pm: str = ""
    if mins.endswith(".m."):
        mins: str, pm: str = mins.split(" ")
    if pm == "p.m.":
        hours += 12
    return round(hours + int(mins)/60, 2)


if __name__ == "__main__":
    main()
