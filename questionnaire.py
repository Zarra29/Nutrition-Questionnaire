

def run_quiz():
    questions = [
        {
            "question": "1. Which nutrient is the body's main source of energy?",
            "options": ["a) Protein", "b) Carbohydrate", "c) Fat", "d) Vitamin"],
            "answer": "b"
        },
        {
            "question": "2. Which vitamin is produced in the skin with sunlight?",
            "options": ["a) Vitamin A", "b) Vitamin C", "c) Vitamin D", "d) Vitamin K"],
            "answer": "c"
        },
        {
            "question": "3. Which food group is the richest source of dietary fiber?",
            "options": ["a) Meat", "b) Vegetables", "c) Milk", "d) Fish"],
            "answer": "b"
        },
        {
            "question": "4. What is the normal BMI range for adults?",
            "options": ["a) 10-15", "b) 16-18", "c) 18.5-24.9", "d) 25-30"],
            "answer": "c"
        },
        {
            "question": "5. Which mineral is essential for strong bones and teeth?",
            "options": ["a) Iron", "b) Calcium", "c) Sodium", "d) Iodine"],
            "answer": "b"
        },
        {
            "question": "6. Kwashiorkor is caused by deficiency of:",
            "options": ["a) Protein", "b) Vitamin A", "c) Vitamin C", "d) Iodine"],
            "answer": "a"
        },
        {
            "question": "7. Which nutrient is needed to build and repair tissues?",
            "options": ["a) Fat", "b) Protein", "c) Carbohydrate", "d) Vitamin"],
            "answer": "b"
        },
        {
            "question": "8. Which vitamin prevents night blindness?",
            "options": ["a) Vitamin A", "b) Vitamin B12", "c) Vitamin C", "d) Vitamin D"],
            "answer": "a"
        },
        {
            "question": "9. Which food is the best source of omega-3 fatty acids?",
            "options": ["a) Fish", "b) Rice", "c) Bread", "d) Milk"],
            "answer": "a"
        },
        {
            "question": "10. Which vitamin helps in blood clotting?",
            "options": ["a) Vitamin A", "b) Vitamin C", "c) Vitamin D", "d) Vitamin K"],
            "answer": "d"
        },
        {
            "question": "11. Which mineral is needed for making hemoglobin?",
            "options": ["a) Calcium", "b) Iron", "c) Zinc", "d) Iodine"],
            "answer": "b"
        },
        {
            "question": "12. What is the main function of carbohydrates?",
            "options": ["a) Build muscle", "b) Provide energy", "c) Make hormones", "d) Absorb vitamins"],
            "answer": "b"
        },
        {
            "question": "13. Pellagra is caused by deficiency of which vitamin?",
            "options": ["a) Vitamin B3 (Niacin)", "b) Vitamin C", "c) Vitamin B12", "d) Vitamin K"],
            "answer": "a"
        },
        {
            "question": "14. Which part of digestion starts in the mouth?",
            "options": ["a) Fat digestion", "b) Protein digestion", "c) Carbohydrate digestion", "d) Vitamin absorption"],
            "answer": "c"
        },
        {
            "question": "15. Which vitamin prevents scurvy?",
            "options": ["a) Vitamin A", "b) Vitamin B1", "c) Vitamin C", "d) Vitamin D"],
            "answer": "c"
        },
        {
            "question": "16. Which mineral is needed for thyroid function?",
            "options": ["a) Calcium", "b) Zinc", "c) Iodine", "d) Iron"],
            "answer": "c"
        },
        {
            "question": "17. Which nutrient gives 9 kcal per gram?",
            "options": ["a) Protein", "b) Carbohydrate", "c) Fat", "d) Alcohol"],
            "answer": "c"
        },
        {
            "question": "18. Which vitamin helps absorb calcium?",
            "options": ["a) Vitamin A", "b) Vitamin C", "c) Vitamin D", "d) Vitamin K"],
            "answer": "c"
        },
        {
            "question": "19. Marasmus is caused by deficiency of:",
            "options": ["a) Fat only", "b) Carbohydrate only", "c) Protein and energy", "d) Vitamin B12"],
            "answer": "c"
        },
        {
            "question": "20. Which food is the best source of probiotics?",
            "options": ["a) Rice", "b) Yogurt", "c) Fish", "d) Egg"],
            "answer": "b"
        }
    ]

    score = 0
    wrong_answers = []

    print("\n Nutrition Quiz \n")
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)


        while True:
            user_answer = input("Your answer (a/b/c/d): ").lower()
            if user_answer in ['a', 'b', 'c', 'd']:
                break
            else:
                print("Invalid input! Please enter only a, b, c, or d.")

        if user_answer == q["answer"]:
            score += 1
        else:
            wrong_answers.append({
                "question": q["question"],
                "your_answer": user_answer,
                "correct_answer": q["answer"]
            })
        print()


    total = len(questions)
    percentage = (score / total) * 100

    print("\n--- Quiz Completed ---")
    print(f"Your Score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%\n")

    if wrong_answers:
        print("Review of Wrong Answers:")
        for wa in wrong_answers:
            print(f"{wa['question']}")
            print(f"   Your answer: {wa['your_answer']}")
            print(f"   Correct answer: {wa['correct_answer']}\n")
    else:
        print("Excellent! All answers are correct.")


run_quiz()
