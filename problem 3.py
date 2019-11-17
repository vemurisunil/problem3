num = int(input("number"))
sqsu=0
su=0
for i in range(num+1):
    sqsu+=i*i
    su+=i
print(abs(sqsu-su*su))