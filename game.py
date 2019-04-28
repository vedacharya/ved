import ramdom
#GET GUESS
def get_guess():
    return input("What is your guess:")

#GENERATE COMPUTER CODE 123
def generate_code():
    digits = [str(num) for num in range(10)]
    #suffle and grab any random 3
    random.suffle(digits)
    return digits[:3]


# GENERATE THE CLUES

def generate_clues(code,user_guess):
    if user_guess==code:
        return "code cracked!"

        clues=[]
for ind,num in enumerate(user_guess):
    if num ==code[ind]:
        clues.append("match")
    elif num in code:
        clues.append("close")
    if clues ==[]:
        return ["Nope"]
    else:
        return clues

#RUN GAME LOGIC
print("Welcome code breaker!")

comp_code =generate_code()
clues_report =[]

while clues_report != "code cracked!":
    guess=get_guess()

    clues_report=generate_clues(guess,comp_code)

    print("Here is the result:")

    for clue in clues_report:
         print(clue)
