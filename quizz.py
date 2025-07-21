import requests


url = "https://gist.githubusercontent.com/sriya0217/49216831c67192d55cc1f5f64104e1b8/raw/33fa9baed73b5c593a6ef0996f7382da450d7112/quiz_questions.json"

try:
    response = requests.get(url)
    questions = response.json()
except Exception as e:
    print("❌ Error fetching questions from URL:", e)
    questions = []

score = 0

print("\n Welcome to the CLI Quiz Game!")
print("----------------------------------")


for index, q in enumerate(questions, 1):
    print(f"\nQ{index}: {q['question']}")
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}.")

# Final result
print("\n🎯 Quiz Complete!")
print(f"Your final score is: {score} out of {len(questions)}")


name = input("\nPlease enter your name: ").strip()
feedback = input("How was the quiz experience? (Your feedback): ").strip()


try:
    with open("feedback.txt", "a") as file:
        file.write(f"Name: {name}\nScore: {score}/{len(questions)}\nFeedback: {feedback}\n---\n")
    print(" Thank you! Your feedback has been saved.")
except Exception as e:
    print("❌ Error saving feedback:", e)
