EqnIn = input('Enter the LHS of the equation: ')
EqnRHS = int(input("Enter the RHS of the equation :"))

def powerpull(EqnIn):
    powernum = []
    pr = 0
    while pr<len(EqnIn):
        if EqnIn[pr]== '^':
            powernum.append(int(EqnIn[pr+1]+EqnIn[pr+2]))
            pr = pr + 1
        else:
            pr = pr + 1
    return powernum
def spacefinder(EqnIn,cr):
    sr = 0
    print(cr)
    spaceloc = 0
    coenum = []
    while sr < 20:
        if EqnIn[cr-sr] == ' ' and ((cr-sr)>(-1)):
            spaceloc = (cr-sr)
            while spaceloc+1 < cr:
                coenum.append(EqnIn[spaceloc+1])
                spaceloc +=1
            break
        else:
            sr +=1
            print(sr)
    coefficentcount = 0
    coeffcient = 0
    print(coenum)
    while coefficentcount < len(coenum):
        coeffcient = int(str(coeffcient) + str(coenum[coefficentcount]))
        coefficentcount +=1
    return coeffcient

def coepull(EqnIn):
    cr = 1
    coeffcients = []
    while cr<len(EqnIn):
        if EqnIn[cr] == 'x':
            coeffcients.append(spacefinder(EqnIn,cr))
            cr +=1
        else:
            cr +=1
    return coeffcients


powernum = powerpull(EqnIn)
coeffcients = coepull(EqnIn)
print(coeffcients[0],'x^',powernum[0],' + ',coeffcients[1],'x^',powernum[1],' + ',coeffcients[2],'x^',powernum[2],sep='')
