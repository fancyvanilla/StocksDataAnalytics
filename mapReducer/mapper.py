#!/usr/bin/env python3

import sys
import csv

reader = csv.DictReader(sys.stdin)

for row in reader:
    try:
        opening_price = float(row["OUVERTURE"])
        closing_price = float(row["CLOTURE"])
    except ValueError:
        print("Error\tError")
        continue

    if opening_price != 0:
        daily_return = (closing_price - opening_price) / opening_price
        print(f"VOLATILITY\t{daily_return}")
