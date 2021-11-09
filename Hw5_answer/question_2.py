# question 2
# rank score

score = float(input("enter your score: "))
if score >= 80:
    print("your grade is A")
elif (score < 80) and (score >= 70):
    print("your grade is B")
elif (score < 70) and (score >= 60):
    print("your grade is C")
else:
    print("your score is D")
