import json
from datetime import datetime
import random
import os

file_path = os.path.join(os.path.dirname(__file__), "tips.json")

with open(file_path, "r") as file:
    data = json.load(file)

name = input("Enter your name: ")

print(f"\nHello, {name}! Welcome to Smart Student Assistant.\n")

print("1. Generate Study Tip")
print("2. Generate Motivation Quote")
print("3. Display Current Date & Time")

choice = input("\nEnter your choice (1-3): ")

result = ""

if choice == "1":
    result = random.choice(data["study_tips"])
    print("\nStudy Tip:")
    print(result)

elif choice == "2":
    result = random.choice(data["motivation_quotes"])
    print("\nMotivation Quote:")
    print(result)

elif choice == "3":
    result = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print("\nCurrent Date & Time:")
    print(result)

else:
    result = "Invalid Choice"
    print(result)

output_path = os.path.join(os.path.dirname(__file__), "output.txt")

with open(output_path, "a") as file:
    file.write(f"\n{name}: {result}")

print("\nResult saved to output.txt")