principle_amount,Rate_of_Intrest,Time=map(int,input("Enter the principle amount,Rate of Intrest,Time: ").split())

simple_intrest = (principle_amount*Rate_of_Intrest*Time)/100
print(f"Simple Intrest is: {simple_intrest} , the amount in the hand is {simple_intrest+principle_amount}")