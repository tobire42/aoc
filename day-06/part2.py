import re

with open("input.txt", "r") as f:
    content = f.read()

groups = content.split("\n\n")

count = 0

for group in groups:
    answered_questions = None
    for line in group.split("\n"):
        if not re.match("^[a-z]+$", line):
            print(line)
            continue
        questions_person = set(line)

        if answered_questions is None:
            answered_questions = questions_person
        else:
            answered_questions = answered_questions & questions_person
    
    #print(answered_questions)
    group_questionscount = len(answered_questions)
    #print(f"Group answered {group_questionscount}")
    count += group_questionscount

print(f"Total count: {count}")