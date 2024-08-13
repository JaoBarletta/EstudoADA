
# Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers between two given numbers!

# Input
# The input begins with the number t of test cases in a single line (t<=10).
#  In each of the next t lines there are two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

# Output
# For every test case print all prime numbers p such that m <= p <= n, one number per line, test cases separated by an empty line.

def Prime_number(arr):
    
    for lista in arr:
        print()
        print()
        inicio = lista[0]
        fim = lista[1]
        if inicio >= 1:
            if fim <= 1000000000:
                if fim - inicio <= 100000:
                    for p in range(inicio , fim):
                        if p <= 1 :
                            pass
                        
                        elif p < lista[0]:
                            pass

                        elif p % 2 == 0 :
                            if p == 2 and p > lista[0]:
                                print(p)
                            elif p !=2 :
                                pass
                            
                        elif p % 3 == 0:
                            if p == 3 and p > lista[0]:
                                print(p)
                            elif p !=3 :
                                pass
                        elif p % 5 == 0:
                            if p == 5 and p > lista[0]:
                                print(p)
                            elif p !=5:
                                pass
                        else:
                            print(p)


if __name__ == "__main__":
    
    try:
        t = int(input())
        if t<=10:
            arr = []

            for i in range(t):
                arr.append(list(map(int, input().strip().split())))

            Prime_number(arr)
        else:
            print()
    except:
        print()
        


# def prime_sieve(limit):
#     """Returns a list of primes up to the limit using Sieve of Eratosthenes."""
#     is_prime = [True] * (limit + 1)
#     is_prime[0] = is_prime[1] = False
    
#     for start in range(2, int(limit**0.5) + 1):
#         if is_prime[start]:
#             for multiple in range(start*start, limit + 1, start):
#                 is_prime[multiple] = False
    
#     return [num for num, prime in enumerate(is_prime) if prime]

# def prime_generator(m, n):
#     """Generates primes between m and n (inclusive) using segmented sieve."""
#     if m < 2:
#         m = 2
    
#     limit = int(n**0.5) + 1
#     primes = prime_sieve(limit)
    
#     is_prime = [True] * (n - m + 1)
    
#     for prime in primes:
#         start = max(prime*prime, (m + prime - 1) // prime * prime)
#         for j in range(start, n + 1, prime):
#             is_prime[j - m] = False
    
#     return [num for num, prime in enumerate(is_prime, m) if prime]

# def main():
#     import sys
#     input = sys.stdin.read
#     data = input().split()
    
#     t = int(data[0])
#     index = 1
#     results = []
    
#     for _ in range(t):
#         m = int(data[index])
#         n = int(data[index + 1])
#         index += 2
#         primes = prime_generator(m, n)
#         results.append(primes)
    
#     for primes in results:
#         for prime in primes:
#             print(prime)
#         print()

# if __name__ == "__main__":
#     main()
