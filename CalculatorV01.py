num1=int(input("ENTER N1: "))
operator=(input("ENTER THE OPERATOR: "))
num2=int(input("ENTER N2: "))

if(operator=="+"):
    print(num1+num2)
elif(operator=="-"):    
      print(num1-num2)     
elif(operator=="*"):
     print(num1*num2)      
elif(operator=="/"):
     if(num1!=0 and num2!=0):
          print(num1/num2)     
     else:
          print("CANNOT DIVIDED BY ZERO")     
else:
     print("OPERATION CANNOT DOABLE!")          

