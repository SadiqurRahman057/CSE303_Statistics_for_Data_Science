def compound_interest_2019_2_60_057(P,R,T):
    A= P*(pow((1+R/100),T))
    compound_interest= A-P
    return compound_interest

x= float(input("Principle amount: "))
y= float(input("Interest rate: "))
z= float(input("Time: "))

print(compound_interest_2019_2_60_057(x,y,z))
