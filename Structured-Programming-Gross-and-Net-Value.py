#################################################################
################ STRUCTURED PROGRAMMING #########################
#################################################################

#To find gross and net value

#da = Dearness Allowance
def da(basic):
    da = basic*80/100
    return da

#hra = House Rent Allowance 
def hra(basic):
    hra = basic*15/100
    return hra

#pf = Provident Fund or (pension fund)
def pf(basic):
    pf = basic*12/100
    return pf

#itax = Income Tax
def itax(gross):
    tax = gross*0.1
    return tax

basic = float(input('enter basic salary:'))

gross = basic + da(basic) + hra(basic)
x = float(round(gross,2))
print('Gross Value is:'+ str(x))

net = gross - pf(basic) - itax(gross)
y = float(round(net,2))
print('Net Value is:'+ str(y))