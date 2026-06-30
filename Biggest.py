# Taking input
n1, n2, n3 = 10, 25, 15
# Logic using and operator
if n1 >= n2 and n1 >= n3:
     print("n1 is largest")
elif n2 >= n1 and n2 >= n3:
   print("n2 is largest")
else:
 n3>= n1 and n3>= n2
 print("n3 is largest")

 # Logic using nested if-else
if n1 >= n2 and n1 >= n3:
    largest = n1
else:
    if n2 >= n3:
        largest = n2
    else:
        largest = n3
print(f"Largest: {largest}")