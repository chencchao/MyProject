import re
s = "3635404702012211481177"
l = '197	 36 35 40 47 02 01 22 11 32 07 24 00	 34 00	1  /  1  /  1  /  1	-53dBm	916.00	'
li =list(l)
print(li)

ss = list(s)
ss.insert(2," ")
ss.insert(5," ")
ss.insert(8," ")
ss.insert(11," ")
ss.insert(14," ")
ss.insert(17," ")
ss.insert(20," ")
ss.insert(23," ")
ss.insert(26," ")
ss.insert(29," ")

print(ss)
ti = 0
tim = []
for i in range(len(li)-1):
    if li[i]+li[i+1] == r"	 ":
        ti +=1
        tim.append(i)
# print(ti)
# print(tim)

for j in range(len(ss)):
    # print(li[tim[0]+2+j])
    # print(ss[j])
    li[tim[0]+2+j] = ss[j]

print(li)
z=''.join(li)
print(z)