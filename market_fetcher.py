import yfinance as yf
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

TARGETS = ["AAPL", "GOOGL", "BEL.NS", "HAL.NS", "RVNL.NS"]

def fetch_live_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        price = ticker.fast_info.last_price
        return price
    except Exception as e:
        return None

def activate_argus():
    print(f"\n{Fore.CYAN}--- PROJECT ARGUS: SECTOR WATCH [{datetime.now().strftime('%H:%M:%S')}] ---{Style.RESET_ALL}\n")

    print(f"{Fore.WHITE}{'ASSET':<10} | {'PRICE':<15} | {'SIGNAL'}")
    print("-" * 50)

    for symbol in TARGETS:
        price = fetch_live_price(symbol)

        if price:
            currency = "Rs." if " .NS" in symbol else "$"
            print(f"{Fore.GREEN}{symbol:<10} | {currency} {price:,.2f}{'':<6} | Tracking")
        else:
            print(f"{Fore.RED}{symbol:<10} | {'N/A':<15} | Lost Connection")

    print(f"\n{Fore.CYAN}----------------------------------{Style.RESET_ALL}")

if __name__ == "__main__":
    activate_argus()