#necessary modules
#numpy is imported for following reasons: log , sqrt , exp f(x)
#scipy is imported for following reasons: normal graph f(x)
import numpy as np
from scipy.stats import norm

#VARIABLES USED:
# S: Current price of the underlying asset (e.g., stock price).
# K: Strike price of the option.
# T: Time to expiration of the option in years.
# r: Risk-free interest rate.
# σ: Volatility of the underlying asset.
# type: Specifies whether it's a call option ("c") or a put option ("p").
def blackScholes(r, S, K, T, sigma, type="c"):
    "Calculate BS price of call/put"
    try:
        d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        if type == "c":
            price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "p":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        else:
            raise ValueError("Invalid option type. Please specify 'c' for Call or 'p' for Put!")
        return price
    except ValueError as e:
        print(e)

# Example usage:
#print(blackScholes(0.05, 100, 100, 1, 0.6, type="c"))
# print(blackScholes(0.05, 100, 100, 1, 0.2, type="p"))
# print(blackScholes(0.05, 100, 100, 1, 0.2, type="x"))
