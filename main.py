import random
outer_count = 0
while outer_count < 5:
    num1 = random.randint (1,10)
    num2 = random.randint (1,10)
    product = num1 * num2
    print(num1,"x",num2)
    inner_count = 0
    while inner_count < 5:
        guess = int(input("What is your guess?"))
        print("You answer: {guess}")
        if guess == product:
            print("Correct!")
            break
        else:
            print("Incorrect. Try again.")
            inner_count += 1
    outer_count += 1