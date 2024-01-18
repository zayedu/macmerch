import sys

def parseArguments():
  arguments={
    "price":int(sys.argv[1]),
    "quantity":int(sys.argv[2]),
    "province":sys.argv[3]
  }
  return arguments

def taxRate(province):
  tax={
    "ON":0.13
  }
  return tax[province]

def mcmerchCalculator():
  arguments=parseArguments()
  tax=taxRate(arguments["province"])
  print(round(arguments['price']*arguments["quantity"]*(1+tax),2))
  
mcmerchCalculator()