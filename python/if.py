#if statement = do some code if some condition is true
#        else do something else


height = int(input("Enter your height(in ft): "))

if height >= 6:
    print("You are very tall")
elif height < 6 :                  #you can add many else if(elif) statements
    print("You are short")
else:
    print("Enter a number !")