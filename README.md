# Mini Compiler in Python

## 📌 Description
This project is a simple Mini Compiler that performs:
- Lexical Analysis
- Syntax Parsing
- Intermediate Code Generation (Three Address Code)

## 🚀 Features
- Supports arithmetic expressions
- Operator precedence handling
- Temporary variable generation (t1, t2, ...)
- Error handling (basic)
- Multiple expression support

## 🧠 Example

Input:
a = b + c * d

Output:
t1 = c * d  
t2 = b + t1  
a = t2  

## ▶️ How to Run

```bash
python3 main.py