import random

print("🎱 Welcome to the Magic 8-Ball! Press Ctrl+C to stop.\n")

answers = [
    "Yes",
    "No",
    "Maybe",
    "Definitely",
    "Absolutely not",
    "Ask again later",
    "I have no idea",
    "It seems likely",
    "Very doubtful",
    "i dont know🤷‍♂️",
    "maybe i guess"
]

while True:
    question = input("Ask your question: ")
    magic_answer = random.choice(answers)
    print("Magic 8-Ball says:", magic_answer, "\n")