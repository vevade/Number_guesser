import random

print("Choose difficulty: easy / medium / hard")
print("Easy = 1 to 20, Medium = 1 to 70, Hard = 1 to 200")
choice = input().lower()
if choice == "easy":
    x = random.randint(1,20)
elif choice == "medium":
    x = random.randint(1,70)
else:
    x = random.randint(1,200)

print("Guess the number!")
attempts = 0
while True:
    n = int(input("Your guess: "))
    attempts +=1
    if n < x:
        print("Higher!")
    elif n > x:
        print("Lower!")
    else:
        print(f"Yay! Your number is {x}")
        break
print(f"Your attempts: {attempts}")



