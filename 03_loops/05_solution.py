#Problem:given a string,find the first non-repeated character
input_str = "teeteracdacd"

for char in input_str:
    print(char)
    if input_str.count(char)==1: #count()method batata hai ki ye jo perticular string hai kitne baar aaya hai or charecter
        print("Char is:",char)
        break