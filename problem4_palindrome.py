""""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

listx = []
listy = []
listz = []

for x in range(100,1000):
    listx.append(x)

for y in range(100,1000):
    listy.append(y)
    for z in listx:
        product = y * z
        if product == int(str(product)[::-1]):
            listz.append(product)


print(listx)
print("")
print(listy)
print("")
print(listz)
print("")
print(max(listz))