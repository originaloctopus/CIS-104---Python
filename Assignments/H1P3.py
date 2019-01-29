#
#HH: get_shortened_integer(2300) returns: 2.3k
#HH: get_shortened_integer(1300000) returns: 1.3M
#Questions:
#what is a Bitwise Operation
#unexpected EOF while parsing

from decimal import *
pennies=int(input(print("How many pennies do you have?")))
penniesVal=float(pennies*.01)
nickels=int(input(print("How many nickels do you have?")))
nickelsVal=float(nickels*.05)
dimes=int(input(print("How many dimes do you have?")))
dimesVal=float(dimes*.1) 
quarters=int(input(print("How many quaters do you have?")))
quartersVal=float(quarters*.25)
halfDollars=int(input(print("How many half dollars do you have?")))
halfDollarsVal=float(halfDollars*.5)
oneDollars=int(input(print("How many one dollar do you have?")))
oneDollarsVal=float(oneDollars)
if pennies==1:
  print ("You only have 1 penny.")
else:
    print ("You have ",(pennies)," pennies.")

if (nickels==1):
  print ("You only have 1 nickel.")
else:
    print ("You have ",nickels," nickels.")

if dimes ==1:
  print ("You only have 1 dime.")
else:
    print ("You have ",dimes," dimes.")

if quarters==1:
  print ("You only have 1 quarter.")
else:
    print ("You have ",(quarters)," quarters.")

if halfDollars==1:
  print ("You only have 1 half dollar.")
else:
    print ("You have ",halfDollars," half dollars.")

if oneDollars==1:
  print ("You only have 1 one dollar.")
else:
    print ("You have ",oneDollars," dollars.")

print("The value of all your coin is $")
totalMonies=input (penniesVal+nickelsVal+dimesVal+quartersVal+halfDollarsVal+oneDollarsVal)
print(totalMonies)
#totalMonies=Decimal()
#totalMonies.quantize(Decimal(0.01))
#print("The total of all your monies is:",totalMonies)