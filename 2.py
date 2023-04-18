def CountPalindromes(number1,number2):  
    
    #this is default OUTPUT. You can change it.
    result=0
      
    #Write your Logic here: 
    for i in range(number1, number2 + 1):
        if str(i) == str(i)[::-1]:
            result += 1
      
    return result  
  
#INPUT [uncomment & modify if required]  
X=int(input())  
Y=int(input())  
  
#OUTPUT [uncomment & modify if required]  
print(CountPalindromes(X,Y))