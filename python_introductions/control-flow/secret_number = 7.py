secret_number = 7 
guess_count = 0
guess = 0
while guess != secret_number :
    guess_count += 1
guess= int(input("guess a number from1 - 10 "))
print(f"you guessed it in {guess_count} tries")