questions = [
    ["Which language is frontend?","Html","Python","Java","ASP.NET","None",0],
    ["Which language is frontend?","Html","Python","Java","ASP.NET","None",0],
    ["Which language is frontend?","Html","Python","Java","ASP.NET","None",0],
    ["Which language is frontend?","Html","Python","Java","ASP.NET","None",0],
    ["Which language is frontend?","Html","Python","Java","ASP.NET","None",0],
    ["Which language is frontend?","Html","Python","Java","ASP.NET","None",0],
    ["Which language is frontend?","Html","Python","Java","ASP.NET","None",0]
]

levels = [1000,2000,5000,15000,30000]

money=0
for i in range(0,len(questions)):
    question = questions [i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}       b.  {question[2]}")
    print(f"c. {question[3]}       d.  {question[4]}")
    reply = int(input("Enter your answer (1-4) "))
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i==3):
            money = 5000
        elif(i==4):
            money = 15000
    else:
        print("Wrong answer!")
        break
print("Your take home money is {money}")