import csv

# Load data
data = []
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

print("📊 Data Chatbot Started (type 'exit' to quit)")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("AI: Bye! 👋")
        break

    elif "average" in user_input:
        total = sum(int(d["marks"]) for d in data)
        avg = total / len(data)
        print("AI: Average marks =", avg)

    elif "highest" in user_input:
        max_marks = max(int(d["marks"]) for d in data)
        print("AI: Highest marks =", max_marks)

    elif "names" in user_input:
        names = [d["name"] for d in data]
        print("AI: Students =", ", ".join(names))

    else:
        print("AI: Sorry, samajh nahi aaya.")
