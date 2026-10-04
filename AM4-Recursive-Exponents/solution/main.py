def exponent(base, power):
    if power == 0:
        return 1
    return base * exponent(base, power - 1)


if __name__ == "__main__":
    print(exponent(3, 4))
