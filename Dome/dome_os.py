import  os
s =  os.popen("ipconfig")
r = s.read()
print(r)