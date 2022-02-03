def collatz(n):
    i = 0
    while n != 1:
        if n%2 == 0:
            n = n//2
            
        else:
            n = 3*n + 1
        print(n)    
        i += 1
    return n, i
print(collatz(97))