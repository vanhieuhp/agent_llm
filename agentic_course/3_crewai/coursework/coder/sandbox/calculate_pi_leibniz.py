from decimal import Decimal, getcontext


def approximate_pi(terms: int = 1_000_000) -> Decimal:
    getcontext().prec = 50
    total = Decimal(0)
    sign = 1

    for i in range(terms):
        denominator = 2 * i + 1
        term = Decimal(sign) / Decimal(denominator)
        total += term
        sign *= -1

    return total * 4


if __name__ == "__main__":
    pi_estimate = approximate_pi()
    print(pi_estimate)
