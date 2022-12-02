#A palindromic number reads the same both ways. The largest palindrome made 
#from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
maior =0
for i in range(100,1000):
    for j in range(100,1000):
        x=j*i
        if str(x)==str(x)[::-1]:
            if x > maior:maior=x
print(maior)