x = -10
if x < 0:
    print("The negative number ",  x, " is not valid here.")
print("This is always printed")


x = 0
a = 6
b = 6
if a > 0:
    if b < 0:
        x = x + 6
    elif a > 6:
        x = x + 5
    else:
        x = x + 4
else:
    x = x + 3

print(x)






if 4 + 5 == 10:
    print("TRUE")
else:
    print("FALSE")
print("TRUE")




a = 5
b = 10
if b < a:
  print("a is greater than b")
elif a == b:
  b = 5
  print("a and b are equal")
else:
  print("b is greater than a")
