
def get_divisors_partial(n):
    divisors = []
    i = 1
    while (i*i <= n):
        if(n%i == 0):
            divisors.append(n//i)
        i += 1
    return  divisors


n = int(input())

divisors = get_divisors_partial(n)

result = 0

for x in divisors:
    y = n//x
    total = x+y
    if total%2 == 0:
        result += 1

print(result)