# Create a program capable of diplaying questions to the user like KBC.
# Use list type to store their questions and correct answers.
# Display the final amount the person is taking home after playimg the game.

questions_list = ["1. Who was the first Prime Minister of India? ", "2. Who was the first President of India?",
                  "3. Who was the first lady Prime Minister of India? ", "4. Who is the current President of India? ",
                  "5. Who is the current Prime Minister of India? "]

answers_list = ["Pt. Jawaharlal Nehru", "Dr. Rajendra Prasad", "Indira Gandhi", "Draupadi Murmu", "Narendra Modi"]

count = 0

for question in questions_list:
    print(question)
    ans = input("Enter the answer : ")
    ans = ans.title()
    for answer in answers_list:
        if ans == answer:
            count = count + 1

print("Your score is : ", count)

