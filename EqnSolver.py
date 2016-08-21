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
    coefficentcount = 0
    coeffcient = 0
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


def accuracy(sol,EqnRHS):
    if abs(EqnRHS-sol) <= 0.001:
        return EqnRHS
    else:
        return sol


def calculation(coeffcients,powernum,x):
    calcount = 0
    psol = 0
    while calcount < len(coeffcients):
        psol = psol +coeffcients[calcount] * pow(x, powernum[calcount])
        calcount += 1
    return psol


EqnIn = input('Enter the LHS of the equation: ')
EqnRHS = int(input("Enter the RHS of the equation: "))
powernum = powerpull(EqnIn)
coeffcients = coepull(EqnIn)
solutions = []
x = -10000
while x<10000:
    sol = calculation(coeffcients,powernum,x)
    fsol = accuracy(sol,EqnRHS)
    if fsol == EqnRHS:
        print(round(x,2),'is a solution')
        solutions.append(x)
        x += 0.005
    else:
        x += 0.005
print(solutions)
