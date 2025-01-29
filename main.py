# Matthew Hall
# January 29, 2025
# Quiz Game

score = 0
questions = [
    {'question': 'How many continents are on planet earth?', 'answer': '7'},
    {'question': 'When did WW2 Start?', 'answer': '1939'},
    {'question': 'who is the first president?', 'answer': 'George Washington'},
]

for question in questions:
    question_text = question.get('question')
    print(question_text)

    user_answer = input("Enter your answer: ")
    correct_answer = question.get('answer')

    if user_answer == correct_answer:
        score = score + 10
print(f"Your score is {score}!")








































































