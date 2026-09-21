def load_questions():
    questions = [
        # 1
        {
            "question": "What is the correct file extension for python files?",
            "choices": ["[A].pt", "[B].py", "[C].pyt", "[D].python"],
            "answer": "B",
            "topic": "Python"
        },
        # 2
        {
            "question": "What is the correct keyword to declare a function in Python?",
            "choices": ["[A]func", "[B]define", "[C]def", "[D]function"],
            "answer": "C",
            "topic": "Python"
        },
        # 3
        {
            "question": "Which of the following is used to output data to the screen in python?",
            "choices": ["[A]choices", "[B]count", "[C]print", "[D]cin"],
            "answer": "C",
            "topic": "Python"
        },
        # 4
        {
            "question": "What is the output of type(5) in python?",
            "choices": ["[A]<class 'int'>", "[B]<class 'float'>", "[C]<class 'str'>", "[D]<class 'number'>"],
            "answer": "A",
            "topic": "Python"
        },
        # 5
        {
            "question": "What is the derivative of a constant number like 5?",
            "choices": ["[A]5", "[B]1", "[C]0", "[D]x"],
            "answer": "C",
            "topic": "Calculus"
        },
        # 6
        {
            "question": "What is the derivative of X^2 with respect to X?",
            "choices": ["[A]X", "[B]2X", "[C]X^2", "[D]X"],
            "answer": "B",
            "topic": "Calculus"
        },
        # 14
        {
            "question": "What is the acceleration due to gravity on Earth approx?",
            "choices": ["[A]9.8 m/s^2", "[B]3.14 m/s^2", "[C]3 *10^8 m/s^2", "[D]5.5 m/s^2"],
            "answer": "A",
            "topic": "Physics"
        },
        # 15
        {
            "question": "Which optical device diverges parallel light rays?",
            "choices": ["[A]Concave mirror", "[B]Convex mirror", "[C]Concave lens", "[D]Convex lens"],
            "answer": "C",
            "topic": "Physics"
        }
    ]
    return questions


def select_quiz(questions):
    print("---Welcome to the Quiz System---")
    print("Available Topics: ('Python', 'Calculus', 'Algebra', 'Physics')")
    
    choice = input("Enter the 'topic' you want (or type 'mixed' for all): ").strip().lower()
    
    if choice == "mixed":
        return questions
        
    filtered = []
    for q in questions:
        if q['topic'].lower() == choice:
            filtered.append(q)
            
    if len(filtered) > 0:
        return filtered
    else:
        print("Invalid topic! Loading all questions by default.")
        return questions


def display_question(q):
    print(f"QUESTION->TOPIC:{q['topic']}")
    print(f"\n{q['question']}\n")
    print('Choices: ')
    for choice in q['choices']:
        print("{choice}")


def get_answer():
    while True:
        ans = input("Enter your answer (A,B,C,D): ").strip().upper()
        if ans in ['A', 'B', 'C', 'D']:
            return ans
        else:
            print("Invalid input! Please enter only A,B,C,D")


def calculate_score(user_answers, questions):
    correct = 0
    wrong = 0
    unanswered = 0
    topics = {}

    for i in range(len(questions)):
        q = questions[i]
        topic = q['topic']

        if topic not in topics:
            topics[topic] = [0, 0]

        topics[topic][1] += 1
        user_ans = user_answers[i]

        if user_ans == "" or user_ans is None:
            unanswered += 1
        elif user_ans == q['answer']:
            correct += 1
            topics[topic][0] += 1
        else:
            wrong += 1

    total = len(questions)
    percent = (correct / total * 100) if total > 0 else 0

    print("~" * 50)
    return correct, wrong, unanswered, percent, topics


def topic_report(topics):
    print("\n---Topic Performance Report---")
    for topic, stats in topics.items():
        c = stats[0]
        t = stats[1]
        p = (c / t * 100) if t > 0 else 0
        print(f"{topic}: {c}/{t} ({round(p, 1)}%)")


def show_result(percent):
    if percent >= 90:
        return "Excellent"
    elif percent >= 75:
        return "Very Good"
    elif percent >= 50:
        return "Needs Practice"
    else:
        return "Failed"


def run_quiz():
    print("Welcome to Quiz & Examination Engine")
    all_questions = load_questions()

    while True:
        selected_questions = select_quiz(all_questions)
        user_answers = []

        for q in selected_questions:
            display_question(q)
            ans = get_answer()
            user_answers.append(ans)

        correct, wrong, unanswered, percent, topics = calculate_score(user_answers, selected_questions)
        grade = show_result(percent)
        
        print("\n" + "="*20 + " FINAL RESULTS " + "="*20)
        print(f"Score: {correct} / {len(selected_questions)}")
        print(f"Percentage: {round(percent, 2)}%")
        print(f"Grade: {grade}")
        print(f"Correct: {correct} | Wrong: {wrong} | Unanswered: {unanswered}")

        topic_report(topics)
        print("~" * 40)

        retake = input("\nDo you want to take another quiz (Y/N): ").strip().upper()
        if retake != 'Y':
            print("\nThank you for using Quiz Engine! Goodbye.")
            break

run_quiz() 