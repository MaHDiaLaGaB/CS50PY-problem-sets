import requests
import sys

LINK = "https://api.coindesk.com/v1/bpi/currentprice.json"

def main():
    if len(sys.argv) > 2 and sys.argv[1] != float:
        sys.exit("error")

    amount = float(sys.argv[1])
    coin_price = get_json()
    print(type(coin_price))
    bitcoins = amount * coin_price
    print(f"${bitcoins:,.4f}")

def get_json():
    try:
        resp = requests.get(LINK)
        usd_price = resp.json()["bpi"]["USD"]["rate_float"]
        return usd_price
    except requests.RequestException:
        pass

if __name__=="__main__":
    main()
