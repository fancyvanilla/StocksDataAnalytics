#!/usr/bin/env python3

import sys
import math

returns = []

for line in sys.stdin:
    key, value = line.strip().split("\t")
    
    if key == "VOLATILITY":
        returns.append(float(value))

# Calculate volatility (standard deviation of returns)
if returns:
    mean_return = sum(returns) / len(returns)
    variance = sum((r - mean_return) ** 2 for r in returns) / len(returns)
    volatility = math.sqrt(variance)
    print(f"VOLATILITY\t{volatility}")
