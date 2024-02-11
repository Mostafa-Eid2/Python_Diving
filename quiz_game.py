print("Welcome to the quiz game")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()
    
print("Okay! Let's play!")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print('correct!')
    score += 1
else:
    print('incorrect')

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print('incorrect')
    
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print('correct!')
    score += 1
else:
    print('incorrect')
    
answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print('correct!')
    score += 1
else:
    print('incorrect')
    
print("your score is:" , score , "out of 4")
print("your score is:" , score/4*100 , "%")