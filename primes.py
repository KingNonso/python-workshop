class Primes:
    def __init__(self):
        self.current = 2
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            current = self.current
            square_root = int(current ** 0.5)
            is_prime = True
            if square_root >= 2:
                for i in range(2, square_root + 1):
                    if current % i == 0:
                        is_prime = False
                        break
            self.current += 1
            if is_prime:
                return current

import cProfile
import itertools
# cProfile.run('[p for p in itertools.takewhile(lambda x: x<10000, Primes())]')

class Primes2:
    def __init__(self):
        self.known_primes=[]
        self.current=2
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            current = self.current
            prime_factors = [p for p in self.known_primes if current % p
== 0]
            self.current += 1
            if len(prime_factors) == 0:
                self.known_primes.append(current)
                return current
# cProfile.run('[p for p in itertools.takewhile(lambda x: x<10000, Primes2())]')


class Primes3:
    def __init__(self):
        self.known_primes=[]
        self.current=2
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            current = self.current
            sqrt_current = int(current**0.5)
            potential_factors = itertools.takewhile(lambda x: x < sqrt_current, self.known_primes)
            prime_factors = [p for p in potential_factors if current % p
== 0]
            self.current += 1
            if len(prime_factors) == 0:
                self.known_primes.append(current)
                return current
# cProfile.run('[p for p in itertools.takewhile(lambda x: x<10000, Primes3())]')


class Primes4:
    def __init__(self):
        self.known_primes=[]
        self.current=2
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            current = self.current
            sqrt_current = int(current**0.5)
            potential_factors = itertools.takewhile(lambda x: x < sqrt_current, self.known_primes)
            is_prime = True
            for p in potential_factors:
                if current % p == 0:
                    is_prime = False
                    break
            self.current += 1
            if is_prime == True:
                self.known_primes.append(current)
                return current
cProfile.run('[p for p in itertools.takewhile(lambda x: x<10000, Primes4())]')


# cProfile.run('[p for p in itertools.takewhile(lambda x: x<10000, Primes())]')