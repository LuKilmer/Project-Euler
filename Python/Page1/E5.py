#2520 is the smallest number that can be divided by each of the numbers 
#from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all 
#of the numbers from 1 to 20?
def check_division(num):
    cont=0
    for i in div:
        if num%i==0:
            cont+=1
    if cont==18:print(num)
    if cont==19:
        return False
    else:
        return True
check=True
num=0
div=[2,3,5,7,10,8,9,4,6,11,12,13,14,15,16,17,19,18,20]
while check:
    num+=1
    x=num*3*2*5*7*11*13*17*19
    check=check_division(x)
print(x)
    
