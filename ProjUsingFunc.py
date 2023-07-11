#Love Calculator

def names(Name1,Name2):
    print("Hello ", Name1,"and", Name2,"!")
names(input("Enter your name: \n"),input("Enter your partner's name: \n"))
Truth = ["It's just pick a random number as your love percentage, so if your percentage is low, don't get upset. "
          "Love can't be predicted or defined by numbers or words, you should always give your best and should not expect anything in return"
          "Best Wishes for you and your partner. "]
            
import random

for _ in range(1):
    random_percentage = random.randint(10, 99)
    if(random_percentage<60):
        print("Oops You have tp work on your Relationship! ")
    elif(random_percentage>60):
        print("Not bad but you should put more effort into it !")
    elif(random_percentage>80):
        print("You two are a very good match for each other! ")
    elif(random_percentage>90):
        print("You two are perfect for each other! ")
    elif(random_percentage>95):
        print("You two are made for each other! ")
    print("Your love percentage is: ",random_percentage,"%")
    print(Truth)

