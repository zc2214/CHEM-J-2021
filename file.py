file = open("output.log","r")
list = file.readlines()
temp = []
final = []
for j in list:
    if "Alpha  occ. eigenvalues --" in j:
        temp = temp + [j[31::]]
        for i in temp:
            if len(i) < 11:
                final = final + [i]
print(min(final,key=final.count))
file.close()

            
            
