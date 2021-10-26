def makeList(num): 
    list_nums = []
    for i in range(1, num):
        list_nums.append(i)
    return list_nums

def checkPrime(list):
    if len(list) > 0:
        num_checking = list[-1]
        if len(list) > 1: 
            list.remove(1)
            list.pop()
        is_prime = True
        for num in list:
            if (num_checking % num) == 0:
                is_prime = False
        if is_prime == True:
            return num_checking
        else: 
            return False
        
    
        



    
def main():
    max = int(input("Enter the number you want to find all the prime numbers up to: "))
    nums = []
    num_primes = 0
    for i in range(1, max + 2):
        if checkPrime(makeList(i)) != None:
            if checkPrime(makeList(i)) != False :
                print( checkPrime(makeList(i)))
                num_primes += 1
    print(num_primes)

main() 