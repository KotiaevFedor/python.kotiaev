#homework first
def power_numbers(*prime):
        squared = [odd ** 2 for odd in prime]
        return squared

print(power_numbers(34534534,543534,2,3,43,423,5456,243,123,12,4234,23,2222))

#homework second

ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):

    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def filter_numbers(arq, order):

        if order == ODD:
            result = filter(lambda x: x % 2 != 0 ,arq)
        elif order == EVEN:
            result = [num for num in arq if num % 2 == 0]
        elif order == PRIME :
            result =filter(is_prime , arq)
        else:
            print("You type unknown order")
            return []

        return list(result)

print(filter_numbers([534543,32,234,23,423], PRIME))





