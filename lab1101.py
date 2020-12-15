#uma maheshwar
#121910313061

#To find the second largest number in the array

a = []
l = []

print("Enter elements: ")
a = list(map(int,input().split()))
print(a)
x = set(a)
for i in x:
	l.append(i)
l.sort()
print("Second smallest is: ",l[1])
