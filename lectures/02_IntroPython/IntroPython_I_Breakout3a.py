# http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html

score = float(input("What is your score (x/100)? "))
if score >= 90:
    letter = 'A'
elif score >= 80:
    letter = 'B'
elif score >= 70:
    letter = 'C'
elif score >= 60:
    letter = 'D'
else:
    letter = 'F'

print("Your letter grade is: ", letter)
