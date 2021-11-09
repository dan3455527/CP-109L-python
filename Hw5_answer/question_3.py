# question 3
# quadratic formula

print("enter the equation of ax^2 + bx + c = 0")
a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))

discriminant = (b**2 - 4*a*c)**0.5

if (a==0 and b==0 and c==0):
    print("x can be any number")
elif(a==0 and b!=0):
    x = (-c)/b
    print("this is linear equation")
    print("x = ", x)
elif(discriminant > 0): # two different root, discriminant > 0
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    print("the equation have two different real roots")
    print("root1 = ", root1, "root2 = ", root2)
elif(discriminant == 0): # two same root, discriminant = 0
    root = (-b)/(2*a)
    print("the equation have one real root (repeated root)")
    print("root = ", root) 
elif(discriminant < 0): # no real root, discriminant < 0
    print("the equation have no real root (conjugate complex root)")

