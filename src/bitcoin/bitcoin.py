import sys
import requests


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        coins_to_buy = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json"
        ).json()
        bpi = response.get("bpi", None)
        usd = bpi.get("USD", None)
        rate = usd.get("rate_float")
        print(f"${rate*coins_to_buy:,.4f}".replace(",", " ").replace(".", ","))

    except requests.RequestException:
        pass


if __name__ == "__main__":
    main()
