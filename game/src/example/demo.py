def demo_question_print_function():
    print("Q1: 1 + 1 = ?")
    print("a. 2")
    print("b. 4")
    print("c. 3")
    print("d. 1")

def demo_question_answer_function():
    ans = input("What is your answer for the question: ")
    if ans == 'b' or ans == 'B':
        print("Correct")
    else:
        print("Incorrect")
