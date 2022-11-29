def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    while True:
        try:
            dval = input("Date: ").strip()
            try:
                slashes = dval.count("/")
                if slashes == 0:
                    m, d, y = dval.split(" ")
                    if m in months:
                        m = months.index(m) + 1
                    if d[-1] != ",":
                        continue
                    d = d[:-1]
                else:
                    m, d, y = dval.split("/")
                day = int(d)
                month = int(m)
                year = int(y)
            except ValueError:
                continue

            if day < 1 or day > 31 or month < 1 or month > 12:
                continue
            print(f"{year}-{month:02}-{day:02}")
            break
        except EOFError:
            break


if __name__ == "__main__":
    main()
