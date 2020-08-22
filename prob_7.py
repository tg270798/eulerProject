def prime_checker(num):
    counter = 0
    for i in range(2,int(num**(1/2)+1)):
        if(num%i == 0):
            counter+=1
            break
    if(counter ==0):
        return True
    return False


prime_count = 1
num = 2
while(prime_count!=10001):
    num+=1
    if(prime_checker(num)):
        prime_count+=1
    if(prime_count == 10001):
        print(num)
