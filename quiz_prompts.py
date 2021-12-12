from Question import Question

question_prompts = [
    "How many months have 28 days? \n(a) 2\n(b) 1\n(c)all of them\n(d)depends if leap year or not.\n>>>",
    "The answer given is really big.\n(a)THE ANSWER\n(b)really big\n(c)an elephant\n(d)the data given is "
    "insufficient.\n>>>",
    "If a leaf falls to the ground in a forest and no one hears it, does it make a sound? \n(a)yes\n(b)no\n(c)depends "
    "on how heavy the leaf was\n(d)depends on where it landed \n>>>",
]

questions = [
    Question(question_prompts[0], "d"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    print("How Odd Are you?")
    print("*" * 30)
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("*" * 30)
    print("You are " + str(score) + "/" + str(len(questions))+ " Odd.")

run_test(questions)