with open("input.txt", "r") as f:
    content = f.read()


groups = content.split("\n\n")

count = 0

for group in groups:
    answered_questions = set()
    for line in group.split("\n"):
        for char in line:
            answered_questions.add(char)
    
    group_questionscount = len(answered_questions)
    print(f"Group answered {group_questionscount}")
    count += group_questionscount

print(f"Total count: {count}")