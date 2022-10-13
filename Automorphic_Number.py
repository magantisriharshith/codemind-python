n = int(input())
s = n*n
p  = s%10
p1 = s%100
p2 = s%1000
if n==p or n==p1 or n==p2:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")