"""
NAME: 
FILE: 01_logic_lab.py
UNIT: Python Fundamentals
GOAL: [Insert objective here]
"""

# TODO 1: Initialize the list and variables
# === DELETE START ===
numbers = [10, 21, 30, 43, 50]
total = 0
# === DELETE END ===


# TODO 2: Create a loop to filter even numbers and add to total
# === DELETE START ===
for num in numbers:
    if num % 2 == 0:
        total += num
# === DELETE END ===


# TODO 3: Print the final result using an f-string
# === DELETE START ===
print(f"The sum of the even numbers is: {total}")
# === DELETE END ===

# =========================================================
# 🧠 REFLECTION: Why did we use a loop here instead of sum()?
# > 
# =========================================================
