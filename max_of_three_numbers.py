def max_of_three(a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    if c>b and c>a:
        return c
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))
sum=max_of_three(a,b,c)
print(sum)