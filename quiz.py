print("--------------------------------------")
print("    MY PYTHON TECH QUIZ")
print("--------------------------------------")

score = 0

questions = [
  {
    "question": "What does CPU stand for?",
    "options": ["A. Central Processing Unit",
                "B. Computer Personal Unit",
                "C. Central Program Utility"],
    "answer": "A"
  },
  {
    "question": "What does AI stand for?",
    "options": ["A. Automated Internet",
                "B. Artificial Intelligence",
                "C. Advanced Input"],
    "answer": "B"
  }
]

for item in questions:
  print("\n" + item["question"])
  
  for option in item["options"]:
    print(option)

  answer = input("Your answer (A, B or C): ").upper()

  if answer == item["answer"]:
    print("Correct! 🎉")
    score += 1

  else:
    print("Not quite. Keep learning!")

print("\nQuiz finished!")
print("Your score:", score, "out of", len(questions))

while True:
  answer = input("Your answer (A, B, or C): ").strip().upper()

  if answer in ["A", "B", "C"]:
    break
  else:
    print("Invalid choice. Please enter A, B or C.")

                 

        

    

  
