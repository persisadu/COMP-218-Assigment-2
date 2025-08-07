import random

def load_questions(filename):
    with open(filename, 'r') as file:
        content = file.read().strip().split('\n\n')

    questions = []
    for block in content:
        lines = block.strip().split('\n')
        question_text = lines[0][len("Question:"):]
        options = lines[1:5]
        answer_line = lines[5]
        correct_answer = answer_line.split(": ")[1].strip()
        questions.append((question_text, options, correct_answer))
    return questions

def get_user_input(max_questions):
    while True:
        try:
            num = int(input(f"Enter the number of question (1 to {max_questions}): "))
            if 1 <= num <= max_questions:
                return num
            else:
                print("Number not in range.")
        except ValueError:
            print("Please enter a valid number.")

def run_quiz(questions, num_questions):
    selected = random.sample(questions, num_questions)
    score = 0
    incorrect = []

    for i, (question, options, correct) in enumerate(selected, 1):
        print(f"\nQuestion {i}: {question}")
        for option in options:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        while user_answer not in ['A', 'B', 'C', 'D']:
            user_answer = input("Invalid choice. Enter A, B, C, or D: ").strip().upper()
        
        if user_answer == correct:
            score += 1
        else:
            incorrect.append({
                'question': question,
                'options': options,
                'correct': correct,
                'user': user_answer
            })

        return score, num_questions, incorrect
    
def show_results(score, total, incorrect):
    print("\n Quiz Completed!")
    print(f"Your Score: {score}/{total} → {round(score / total *100, 2)}%")

    if incorrect:
        print("\n Questions you got wrong:")
        for item in incorrect:
            print(f"\nQuestion: {item['question']}")
            for opt in item['options']:
                print(opt)
            print(f"Your Answer: {item['user']}")
            print(f"Correct Answer: {item['correct']}")
        else:
            print("\n Perfect Score! Well done!")

def main():
    filename = "mc questions.txt"
    all_questions = load_questions(filename)
    num = get_user_input(len(all_questions))
    score, total, incorrect = run_quiz(all_questions, num)
    show_results(score, total, incorrect)

if __name__ == "__main__":
    main()