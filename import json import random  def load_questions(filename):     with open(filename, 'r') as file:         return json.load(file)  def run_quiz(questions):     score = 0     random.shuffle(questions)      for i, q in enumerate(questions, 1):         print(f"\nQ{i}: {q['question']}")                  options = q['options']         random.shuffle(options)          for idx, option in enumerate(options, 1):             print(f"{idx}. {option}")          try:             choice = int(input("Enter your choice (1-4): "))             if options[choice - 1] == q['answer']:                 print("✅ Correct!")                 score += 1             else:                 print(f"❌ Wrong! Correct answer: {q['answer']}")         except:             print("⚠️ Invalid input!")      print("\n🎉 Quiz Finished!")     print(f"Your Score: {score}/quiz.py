import json
import random

def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def run_quiz(questions):
    score = 0
    random.shuffle(questions)

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        
        options = q['options']
        random.shuffle(options)

        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if options[choice - 1] == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}")
        except:
            print("⚠️ Invalid input!")

    print("\n🎉 Quiz Finished!")
    print(f"Your Score: {score}/{len(questions)}")

def main():
    print("🔥 Welcome to Quiz Generator 🔥")
    questions = load_questions("questions.json")
    run_quiz(questions)

if __name__ == "__main__":
    main()
