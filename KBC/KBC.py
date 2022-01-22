print("Welcome to KBC (Kaun Banega Crorepati)")
print()
question_list = [
    "Q1 How many continents are there?",              # pehla question
    "Q2 What is the capital of India?",            # doosra question
    "Q3 NG mei kaun se course padhaya jaata hai?"    # teesra question
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counselling", "Tourism", "Agriculture"]]
solution_list = [3, 4, 1] 
lifeline_list=[["(3)Seven","(1)Four"],["(2)Bhopal","(4)Delhi"],["(3)Tourism","(1)Software Engineering"]]
i=0
count=0
while i<len(question_list):
    print(question_list[i])
    j=0
    while j<len(options_list[i]):
        print(j+1,".",options_list[i][j])
        j+=1
    lifeline_choice=input("Do you want 5050 lifeline? Say Y/N :")
    if lifeline_choice=="Y":
        if count<1:
            k=0
            while k<len(lifeline_list[i]):
                print(lifeline_list[i][k])
                k+=1
            user_input=int(input("enter the answer :"))
            if user_input==solution_list[i]:
                print("Congrats your answer is correct")
            else :
                print("Opps your answer is wrong")
                break
        else:
            print("You already used 5050 lifeline")
            user_input=int(input("enter the answer :"))
            if user_input==solution_list[i]:
                print("Congrats your answer is correct")
            else :
                print("Opps your answer is wrong")
                break
        count+=1

    else:
        lifeline_choice=="N"
        user_input=int(input("enter the answer :"))
        if user_input==solution_list[i]:
            print("Congrats your answer is correct")
        else :
            print("Opps your answer is wrong")
            break
    i+=1


    