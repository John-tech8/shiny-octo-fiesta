def sqrt_newton(n):
    x=n/2
    tolerance=1e-6


    while True:
        root=0.5*(x+n/x)
        if abs (root-x)<tolerance:
            return root
        x=root

num=int(input("Enter a Number:"))
result=sqrt_newton(num)
print(f"Square Root of {num} is {result}")
