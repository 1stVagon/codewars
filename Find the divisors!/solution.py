def divisors(integer):
    divisors = []
    i = 1

    while i < integer:
        i += 1
        if integer % i == 0:
            divisors.append(i)

    return divisors[:-1] if divisors[0] != integer else f'{integer} is prime'
