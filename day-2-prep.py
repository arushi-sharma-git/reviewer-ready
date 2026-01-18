# Security key validator 
print("Enter the security key")
key= input()
if len(key)!=8:
    print("the key must be exactly 8 characters long")
elif not key[0].isalpha() or not key[-1].isdigit(): 
    print("inavlid : key should start with a alphabet and end with a digit ")
elif "z" in key.lower():
    print ("character 'z' is not allowed in the key")
else:
    try:
         totalsum=int(key[3])+int(key[4])
         if totalsum<10:
          print("the sum of fourth and fifth digit should be greater than 10  ")
         else:
          print("Access garnted!!!")
    except:  
        print("value error the fourth and fifth character must be a digit")


