import Optimizer


def main():
    tickers = "GOOGL TSLA"
    minr, maxr = Optimizer.optimize(tickers)
    
    print(minr.to_json())
    print(maxr.to_json())
    

main()