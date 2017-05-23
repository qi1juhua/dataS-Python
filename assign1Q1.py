import math
def nums_reversed(n):
    newN=0
    while n>0:
        newN=newN*10+n%10
        n=math.floor(n/10)
    return int(newN)

print(nums_reversed(12345))

def string_splosion(x):
    strlen=len(x)+1
    #print(strlen)
    result=""
    for i in range(strlen):
        #print(i)
        result=result+x[0:i]
        #print(result)
    return result

print(string_splosion('Data!'))

def double100(x):
    judge=0
    #listlen=len(x)
    for cur in x:
        if cur==100:
            judge=judge+1
        else:
            judge=0
        if judge==2:
            return True
    return False

print(double100([100,2,3,100]))
print(double100([2,3,100,100,5]))

def median(x):
    lenX = len(x)
    if lenX==0:
        print('Empty!')
        return
    x.sort()
    #print x
    if lenX%2==0:
        return (x[int(lenX/2)-1]+x[int(lenX/2)])/2
    else:
        return x[int(math.floor(lenX/2))]

print(median([5,2,3,1,4]))
print(median([40,30,10,20]))
        
    
    
