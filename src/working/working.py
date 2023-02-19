import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(input_time: str) -> str:
    check1 = ["AM", "PM", "TO"]
    parts = re.split(r"\s", input_time.upper(), 5)

    if not all(item in parts for item in check1):
        raise ValueError

    start_time: str = parts[0]
    end_time: str = parts[3]
    starting_hour, staring_minutes = get_hm(start_time)
    ending_hour, ending_minutes = get_hm(end_time)
    if (
        starting_hour > 12
        or ending_hour > 12
        or staring_minutes >= 60
        or ending_minutes >= 60
    ):
        raise ValueError

    if parts[1] == "PM" and starting_hour < 12:
        starting_hour += 12

    if parts[1] == "AM" and starting_hour == 12:
        starting_hour = 0

    if parts[4] == "PM" and ending_hour < 12:
        ending_hour += 12

    if parts[4] == "AM" and ending_hour == 12:
        ending_hour = 0

    
      
    return f"{starting_hour:02}:{staring_minutes:02} to {ending_hour:02}:{ending_minutes:02}"


def get_hm(time_str: str) -> (int, int):
    if ":" in time_str:
        hour, minutes = time_str.split(":")
        hour_int = int(hour)
        minutes_int = int(minutes)
    else:
        hour_int = int(time_str)
        minutes_int = 0
    return (hour_int, minutes_int)


if __name__ == "__main__":
    main()
