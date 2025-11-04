# 🧮 Python Data Types — Complete Overview and Examples

**File:** `2_data_types.py`  
**Author:** [shafiq73](https://github.com/shafiq73)  

---

## 📘 Overview
This script is part of the **Python fundamentals** series.  
It explains and demonstrates all major **Python data types** with practical examples, helping beginners clearly understand how data is stored, represented, and manipulated in Python.

The code examples cover **immutable** and **mutable** data types with print outputs and type checks.

---

## 🧠 Objective
To provide a clear understanding of Python’s **core data types**, their properties, and usage in real programs.

---

## ⚙️ Topics Covered

| Category | Description | Example |
|-----------|--------------|----------|
| **Numeric Types** | Integer, Float, Complex numbers | `x = 5`, `y = 3.14`, `z = 2 + 3j` |
| **String Type** | Text or sequence of characters | `"Hello, Python!"` |
| **Boolean Type** | True/False values | `is_active = True` |
| **Sequence Types** | Ordered collections | `list`, `tuple`, `range` |
| **Mapping Type** | Key-value pairs | `dict = {"name": "Ali", "age": 25}` |
| **Set Types** | Unordered unique collections | `{1, 2, 3}` |
| **None Type** | Represents absence of value | `value = None` |

---

## 🧩 Example Code

```python
# Numeric types
a = 10
b = 3.5
c = 2 + 5j
print(type(a), type(b), type(c))

# String
name = "Python"
print(name.upper())

# Boolean
is_valid = True
print(is_valid)

# List
fruits = ["apple", "banana", "mango"]
print(fruits[1])

# Tuple
coordinates = (12.5, 23.8)
print(coordinates)

# Dictionary
student = {"name": "Ali", "age": 20}
print(student["name"])

# Set
unique_numbers = {1, 2, 3, 2, 1}
print(unique_numbers)
