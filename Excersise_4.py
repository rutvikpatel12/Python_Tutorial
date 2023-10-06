st = input("Enter Message: ")
words = st.split(" ")
coding = True
if(coding):
    nwords = []
    for word in words:    
        if(len(word)>=3):
            r1 = "abc"
            r2 = "xyz"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
    print(" ".join(nwords))
else:
    pass