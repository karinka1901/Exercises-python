sentence = input("enter:")
sentence = " " + sentence
for x in range(len(sentence)):
    if sentence[x-1] ==" " and sentence[x] != "":
        print(sentence[x])
    x +=1