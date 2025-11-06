# 🧷 Python Indentation — Understanding Code Blocks & Structure

**File:** `3_indentation.py`  
**Author:** [shafiq73](https://github.com/shafiq73)

---

## 📘 Overview  
This script is designed as part of the Python fundamentals series, focusing on the concept of **indentation** in Python. It demonstrates how proper indentation defines code blocks, controls flow, and avoids syntax errors.

---

## 🧠 Objective  
By studying and running this file, you will gain a solid understanding of how indentation:
- Determines the start and end of code blocks.  
- Affects conditional statements, loops, functions, and nested structures.  
- Must follow consistent rules to avoid errors and maintain readability.  
  :contentReference[oaicite:0]{index=0}

---

## ⚙️ Topics Covered  
- Why indentation is syntax-critical in Python (not just style)  
- How to indent `if`, `for`, `while`, `def`, `class` correctly  
- Difference between indenting with spaces vs tabs, and consistent usage  
- Nested code blocks and how each level increases indentation  
- Common indentation errors and how to resolve them  

---

## 🧩 Example Snippet  

```python
def greet_user(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, Stranger!")

for i in range(3):
    greet_user(f"User{i+1}")
