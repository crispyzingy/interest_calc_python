import math as m

# create compound interest function
def cInterest(p, r, n, t):
    cFormula = p * m.pow((1 + r / n), n * t)
    return cFormula


# input values
p = float(input("Enter principal: $"))
r = 0.1  # Enter interest rate, as decimal (for 2%, it's 0.02)
n = int(
    input("Compound no. (1, 2, 4, 365 as yearly, semi-annually, quaterly and daily): ")
)
t = int(input("Duration of saving, in years: "))

# print total, amount rounded to 2 dp
print("Total amount = ${}".format(round(cInterest(p, r, n, t), 2)))
