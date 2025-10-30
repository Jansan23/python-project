import random
name = input("What is your Name  ")
print("Good Luck !",name)

words = ['rainbow','computer','sciece', 'programming','phython','mathematics',
        'player','condition', 'reverse','water','board','geeks'  ]

word = random.choice(words)

print("guess the characters")

guesses = ''
turns = 12

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses :
            print(char,end="")
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You win")
        print("The word is :" , word)

        break
    print()

    guess = input ("guess a characte :")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("wrong")
        print("you have", + turns,'more guesses')

        if turns == 0:
            print("you Loose")

    



