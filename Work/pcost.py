#!/usr/bin/env python3
# pcost.py

import report
import csv

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))
    
    if __name__ == '__main__':
    import sys
    main(sys.argv)
