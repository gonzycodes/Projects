import random

questions = {
    "How do i run as administrator? (Super user do)": "sudo",
    "How do i show the current path/directory?": "pwd",
    "Whats the command for changing directory?": "cd",
    "Whats the command for showing all files in current directory?": "ls",
    "How do i create a directory?": "mkdir",
    "How do i create a file?": "touch",
    "What the command for moving or changing file names?": "mv",
    "Command for printing a file?": "cat",
    "How do i clear the terminal?": "clear"
}

score = 0

while True:
    question, answer = random.choice(list(questions.items()))
    print(question)
    user_input = input("> ")

    if user_input.strip().lower() == "exit":
        break

    if user_input.strip() == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {answer}\n")

print(f"Final score: {score}")