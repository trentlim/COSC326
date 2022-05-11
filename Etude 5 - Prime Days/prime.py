import math
import sys


def find_primes(num):
    primes = [2]

    if num == 1:
        return
    elif num == 2:
        return primes

    for i in range(3, num + 1, 2):
        if all(i % j != 0 for j in range(3, int(i ** 0.5) + 1, 2)):
            primes.append(i)

    return primes


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False

    return True


def get_day_of_year(month, day):
    if month == 0:
        return day
    else:
        for i in range(month - 1):
            day += months[i]
        return day


# Function to find and return the prime days of each month in the year
def find_prime_days(months):
    primes = []

    # For each month, put the primes of that month in a list, and append that list to primes
    for month in months:
        primes_of_month = find_primes(month)
        primes.append(primes_of_month)

    return primes


# Function to find and return prime days which are in a prime-numbered months
def find_real_primes(months):
    primes = find_prime_days(months)
    prime_months = find_primes(len(months))

    if len(primes) == 1:
        primes = []
        return primes

    for i in range(len(months)):
        if (i + 1) not in prime_months:
            primes[i] = []

    return primes


# Function to find and return prime-numbered days of the year that are really prime
def find_true_primes(months):
    primes = find_real_primes(months)

    # for i in range(1, len(primes)):
    #     for j in range(len(primes[i])):
    #         print(primes[i][j])
    #         day_of_year = get_day_of_year(i, primes[i][j])
    #         day_of_year += months[0]
    #         print(day_of_year)
    #         print(is_prime(day_of_year))
    #         print("\n")

    for month in primes:
        month[:] = [get_day_of_year(primes.index(month) + 1, day) for day in month]
        month[:] = [day for day in month if (is_prime(day))]

    return primes


if __name__ == "__main__":
    months = sys.argv
    months.pop(0)
    months = [int(float(i)) for i in months]

    true_primes = find_true_primes(months)

    for month in true_primes:
        for day in month:
            day_of_month = day
            for i in range(true_primes.index(month)):
                day_of_month -= months[i]
            print(
                str(day)
                + ": "
                + str(true_primes.index(month) + 1)
                + " "
                + str(day_of_month)
            )

