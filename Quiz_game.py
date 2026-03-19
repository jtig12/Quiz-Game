questions = ("What planet is known as the Red Planet?: ",
             "What gas do plants absorb during photosynthesis?: ",
             "What is the chemical symbol for water?: ",
             "Which organ pumps blood around the human body?: ",
             "What force pulls objects toward Earth?: ",
             "What is the center of an atom called?: ",
             "Which planet is the largest in our solar system?: ",
             "What part of the cell contains genetic material?: ",
             "What state of matter has a fixed volume but no fixed shape?: ",
             "What type of energy is stored in food?: ")

options = (("A. Venus", "B. Mars", "C. Mercury", "D. Saturn"),
           ("A. Oxygen", "B. Nitrogen", "C. Carbon dioxide", "D. Hydrogen"),
           ("A. CO2", "B. O2", "C. H2O", "D. NaCl"),
           ("A. Lungs", "B. Brain", "C. Heart", "D. Liver"),
           ("A. Magnetism", "B. Friction", "C. Gravity", "D. Electricity"),
           ("A. Electron", "B. Nucleaus", "C. Proton", "D. Shell"),
           ("A. Earth", "B. Jupiter", "C. Uranus", "D. Neptune"),
           ("A. Cell membrane", "B. Cytoplasm", "C. Nucleus", "D. Ribosome"),
           ("A. Solid", "B. Liquid", "C. Gas", "D. Plasma"),
           ("A. Heat energy", "B. Chemical energy", "C. Light energy", "D. Mechanical energy"))

answers = (("B"),
           ("C"),
           ("C"),
           ("A"),
           ("C"),
           ("B"),
           ("B"),
           ("C"),
           ("B"),
           ("B"))

guesses = []

score = 0

question_num = 0

for question in questions:
    print("------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
print("------------------------------")
print("          RESULTS             ")
print("------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")


print("\nguesses: ", end="")
for guess in guesses:
    print(guess, end=" ")


score = (score / len(questions)) * 100

print(f"\nYour total score is {score}%")
