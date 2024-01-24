# We want to ask the user a couple of questions
# Based on these questions we add one with each passing question
# We also want to be able to tell how many questions our users answered correctly

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0


# Ask the user their first question


answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + "questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
