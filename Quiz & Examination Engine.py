import random

def load_questions():
    questions = [
        {#!
            "question": "What is the correct file extension for python files?",
            "choices": ["A).pt", "B).py", "C).pyt", "D).python"],
            "answer": "B",
            "topic": "Python"
        },
        {#2
            "question": "Which keyword is used to create a function in Python?",
            "choices": ["A)func", "B)define", "C)def", "D)function"],
            "answer": "C",
            "topic": "Python"
        },
        {#3
            "question": "Which of the following is used to output date to the screen in python?",
            "choices": ["A)choices", "B)count", "C)print", "D)cin"],
            "answer": "C",
            "topic": "Python"
        },
        {#4
            "question": "What is the output of type(5)in python?",
            "choices": ["A)<class'int'>", "B)<class'float'>", "C)<class'str'>", "D)<class'number'>"],
            "answer": "A",
            "topic": "Python"
        },
        {#5
            "question": "What is the derivative of a constant number like 5?",
            "choices": ["A)5", "B)1", "C)0", "D)x"],
            "answer": "C",
            "topic": "Calculus"
        },
        {#6
            "question": "What is the derivative of X^2 with respect to X?",
            "choices": ["A)X", "B)2X", "C)X^2", "D)X"],
            "answer": "B",
            "topic": "Calculus"
        },
        {#7
            "question": "What is the derivative of sin(X)?",
            "choices": ["A)-cos(X)", "B)sin(X)", "C)-sin(x)", "D)cos(x)"],
            "answer": "D",
            "topic": "Calculus"
        },
        {#8
            "question": "What is the integral of 2X dx?",
            "choices": ["A) X^2+C", "B) 2X^2+C", "C) X+C", "D)2+C"],
            "answer": "A",
            "topic": "Calculus"
        },
        {#9
            "question": "If a matrix has a determinant equal to zero,it is called a:",
            "choices": ["A)Identity matrix", "B)Singular matrix", "C)Symmetric matrix", "D)Inverse matrix"],
            "answer": "B",
            "topic": "Algebra"
        },
        {#10
            "question": "What is the sum of the roots of the quadratic egution aX^2 + bX + C = 0?",
            "choices": ["A)-b/a", "B)c/a", "C)b/a", "D)-c/a"],
            "answer": "A",
            "topic": "Algebra"
        },
        {#11
            "question": "What is the value of i^2 Where i is the imaginary unit?",
            "choices": ["A)1", "B)0", "C)-1", "D)i"],
            "answer": "C",
            "topic": "Algebra"
        },
        {#12
            "question": "What is the SI unit of force?",
            "choices": ["A)Joule", "B)Watt", "C)Newton", "D)Pascal"],
            "answer": "C",
            "topic": "Physics"
        },
        {#13
            "question": "According to Snell's law, n1*sin(theta1) is equal to:",
            "choices": ["A)n2*cos(theta2)", "B)n2sin(theta2)", "C)n1*sin(theta2)", "D)n2/sin(theta2)"],
            "answer": "B",
            "topic": "Physics"
        },
        {#14
            "question": "What is the acceleration due to gravity on Earth approximately?",
            "choices": ["A)9.8 m/s^2", "B)3.14 m/s^2", "C)3 *10^8 m/s^2", "D)5.5 m/s^2"],
            "answer": "A",
            "topic": "Physics"
        },
        {#15
            "question": "Which optical device diverges parallel light rays?",
            "choices": ["A)Concave mirror", "B)Convex mirror", "C)Concave lens", "D)Plane mirror"],
            "answer": "C",
            "topic": "Physics"
        }
    ]
    return questions


def select_quiz(questions):
    print("\n---Welcome to the Quiz System---")
    print("Available Topics:('Python','Calculus','Algebra','Physics')")

    choice = input("Enter the 'topic' you want (or type 'mixed' for all):").strip().lower()
    
    if choice == 'mixed':
        return questions
        
    filtered = [q for q in questions if q["topic"].strip().lower() == choice]
    
    if len(filtered) > 0:
        return filtered
    else:
        print("Invalid topic selected! Loading all questions by default.")
        return questions


def display_question(index, question):
    print('=' * 50)
    print(f'QUESTION [{index}], TOPIC [{question["topic"]}]')
    print('=' * 50)
    print(f'\n{question["question"]}\n')
    print('Choices:')
    
    for choice in question['choices']:
        print(f'   {choice}')
        
    print("#" * 50)


def get_answer():
    letters = ['A', 'B', 'C', 'D']
    
    for letter in letters:
        choice = input('enter your answer (A, B, C, D): ').strip().upper()
        
        if choice in letters:
            return choice
            
        print('please enter one of these options (A, B, C, D)')


def calculate_score(user_answers, questions):
    correct = 0
    wrong = 0
    unanswered = 0
    topics = {}
    for i in range(len(questions)):
        q = questions[i]
        topic = q["topic"].strip()
        if topic not in topics:
            topics[topic] = [0, 0]
        topics[topic][1] = topics[topic][1] + 1
        user_ans = user_answers[i]
        if user_ans is None or user_ans == "":
            unanswered = unanswered + 1
        elif user_ans == q["answer"]:
            correct = correct + 1
            topics[topic][0] = topics[topic][0] + 1
        else:
            wrong = wrong + 1
    total = len(questions)
    if total > 0:
        percent = (correct / total) * 100
    else:
        percent = 0
    return correct, wrong, unanswered, percent, topics


def topic_report(topics):
    print("\nTopic Performance Report:")
    for topic in topics:
        stats = topics[topic]
        correct = stats[0]
        total = stats[1]
        if total > 0:
            p = (correct / total) * 100
        else:
            p = 0
        print("• " + topic + ": " + str(correct) + "/" + str(total) + " (" + str(round(p, 1)) + "%)")


def show_result(percent):
    if percent >= 90:
        grade = "Excellent"
    elif percent >= 75:
        grade = "Very Good"
    elif percent >= 50:
        grade = "Needs Practice"
    else:
        grade = "Failed"
    return grade


def run_quiz():
    print("Welcome to Quiz & Examination Engine")
    all_questions = load_questions() 
    again = "Y"
    while again == "Y":
        selected_questions = select_quiz(all_questions)
        user_answers = []
        
        for index, q in enumerate(selected_questions, 1):
            display_question(index, q)
            ans = get_answer()
            user_answers.append(ans)
            
        correct, wrong, unanswered, percent, topics = calculate_score(user_answers, selected_questions)
        grade = show_result(percent)
        print("\nFINAL RESULTS:")
        print("Score: " + str(correct) + "/" + str(len(selected_questions)))
        print("Percentage: " + str(round(percent, 2)) + "%")
        print("Grade: " + grade)
        print("Correct Answers: " + str(correct) + " | Wrong: " + str(wrong) + " | Unanswered: " + str(unanswered))
        topic_report(topics)
        
        retake = input("\nDo you want to take another quiz? (Y/N): ").strip().upper()
        if retake == "Y":
            again = "Y"
        else:
            again = "N"
            
    print("\nThank you for using the Quiz Engine! Goodbye.")


run_quiz()
