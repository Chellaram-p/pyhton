import os
n = int(input())
a = []
for i in range (0,n):
    m = str(input())
    a.append(m)
print(os.path.commonprefix(a))
