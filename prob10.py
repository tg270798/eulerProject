import time

def primeChecker(num):
    counter = 0
    for i in range(2,int(num**(1/2)) + 1):
        if(num%i == 0):
            counter+=1
            break
    if(counter==0):
        return True
    return False
                

def primeList():
    pList = [2]
    for i in range(3,2000000,2):
        if(primeChecker(i)):
            pList.append(i)
    
    return pList

def sumPrime():
    sumP = 0
    lst = primeList()
    #print(lst)
    for z in lst:
        sumP+=z;
    
    print(sumP)
    
start = time.time()
sumPrime()
end = time.time()

print("runtime", end-start)



#output ---> 142913828922 runtime 15.764654397964478

