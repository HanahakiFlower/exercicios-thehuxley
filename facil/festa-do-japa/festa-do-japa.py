valores = input()

x = valores.split()

thisdict = {}

for y in range(0, 4):
    
    if y == 0:
        thisdict["saques"] = (int(x[y]) * 675)/45
        
    elif y == 1:
        thisdict["manjus"] = int(x[y])
        
    elif y == 2:
        thisdict["yakitoris"] = int(x[y])
    
    elif y == 3:
        if int(x[y]) >= 4:
            thisdict["pessoas"] = int(x[y])
            
thisdict2 = {}
missing = []
            
if  not thisdict["saques"] >= thisdict["pessoas"] * 4:
    thisdict2["saques"] = thisdict["pessoas"] * 4 - thisdict["saques"]
    missing.append("saques")

if  not thisdict["manjus"] >= thisdict["pessoas"] * 5:
    thisdict2["manjus"] = thisdict["pessoas"] * 5 - thisdict["manjus"]
    missing.append("manjus")
    
if  not thisdict["yakitoris"] >= thisdict["pessoas"] * 3:
    thisdict2["yakitoris"] = thisdict["pessoas"] * 3 - thisdict["yakitoris"]
    missing.append("yakitoris")

if len(missing) == 0:
    print("Partiu Festa do Japa!")

elif len(missing) == 3:
    print("Partiu Festa do Japa...Japacama")

elif len(missing) == 1:
    print("Faltaram %i %s" % (thisdict2[missing[0]], missing[0]) )

else:
    print("Faltaram %i %s e %i %s" % (thisdict2[missing[0]], missing[0], thisdict2[missing[1]], missing[1], ) )
