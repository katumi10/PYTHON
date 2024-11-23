# logical operators = evaluate multiple conditions(or, and,not)
#                  or = at least one condition must be true
#                  and = both conditiond must be true
#                  not = inverts the condition(not false, not true)

#OR
temp =  25
hot_weather = False

if temp < 30 or temp > 30 or hot_weather: #if one cndition is true the whole statement is true
    print("The weather is hot")
else:
    print("The weather is cold")    


#AND 
age = 12
isa_teenager = True
is_nota_teenager  = False

if age <= 19 and age > 12 and isa_teenager:
    print("You are a teenager")
    print("And you are young")
elif age > 0 <= 12 and isa_teenager:
    print("You are not a teenager")

else:
    print("You are an adult")    

#NOT

