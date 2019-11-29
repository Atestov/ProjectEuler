def IsPrime(n):
    if n % 2 == 0 or n % 3 == 0: return False
    for x in range(11, int(n**(1/2)+1),2):
        if n % x == 0:
            return False
    return True

for i in range(int(600851475143**(1/2)+1), 2, -1):
    if IsPrime(i) and 600851475143 % i == 0:
        print(i)
        break
