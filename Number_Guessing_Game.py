import random
start = input("Start Point: ")
end = input("End Point: ")
secret_number = random.randint(int(start), int(end))
random_chance = random.randint(1,10)

print(f"Guess a number between {start} to {end}\nYou will get {random_chance} chances. ")


for i in range(random_chance):
    track = i
    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Your guess is too high")

    elif guess < secret_number :
        print("Your guess is too low")

    else:
        break

if guess == secret_number:
    print(f"congo! you won. it took {i+1} tires")
else:
    print("Better luck next time")
