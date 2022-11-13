values = input()

# splits the values that the user will provide in one go
x = values.split()

# dict to link the objects to the user input numbers
thisdict = {}

for y in range(0, 4):
    
    if y == 0:
        thisdict["saques"] = (int(x[y]) * 675)/45 # converts the "sake" bottles amount into cups
        
    elif y == 1:
        thisdict["manjus"] = int(x[y])
        
    elif y == 2:
        thisdict["yakitoris"] = int(x[y])
    
    elif y == 3:
        if int(x[y]) >= 4:
            thisdict["pessoas"] = int(x[y])
            
# dict to report missing objects and how much is missing 
thisdict2 = {}
missing = []
            
if  not thisdict["saques"] >= thisdict["pessoas"] * 4: # if the amount is not enough, link the missing amount value to the object key and then add it to the missing list
    thisdict2["saques"] = thisdict["pessoas"] * 4 - thisdict["saques"]
    missing.append("saques")

if  not thisdict["manjus"] >= thisdict["pessoas"] * 5:
    thisdict2["manjus"] = thisdict["pessoas"] * 5 - thisdict["manjus"]
    missing.append("manjus")
    
if  not thisdict["yakitoris"] >= thisdict["pessoas"] * 3:
    thisdict2["yakitoris"] = thisdict["pessoas"] * 3 - thisdict["yakitoris"]
    missing.append("yakitoris")

if len(missing) == 0: # if there's no object missing, then let's go party!!!
    print("Partiu Festa do Japa!")

elif len(missing) == 3: # if every object is missing, then let's back home T-T
    print("Partiu Festa do Japa...Japacama")

elif len(missing) == 1: # if one object is missing, tell the user which one and how much
    print("Faltaram %i %s" % (thisdict2[missing[0]], missing[0]) )

else: # if two objects is missing, tell the user which and how much
    print("Faltaram %i %s e %i %s" % (thisdict2[missing[0]], missing[0], thisdict2[missing[1]], missing[1], ) )
