score = float(input("Enter your score : "))
if score < 0 or score >100:
    print("invalid score")
elif score<=50:
    print("Congratulations You passed.")
else:
    print("sorry you failed")

print("Result checking completed")
