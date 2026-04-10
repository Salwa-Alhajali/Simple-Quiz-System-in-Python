# 📝 Simple Quiz System in Python

## 🧠 Project Idea

This project is a simple quiz system built using Python.
It allows a user to answer a set of questions and calculates their score based on correct answers.

---

## ⚙️ How It Works

1. The program asks for answers (these represent the **correct answers**).
2. Then, for each answer:

   * The user is asked to input their response.
   * The program compares the user's answer with the correct one.
3. If the answer is correct:

   * The score increases ✅
4. If the answer is incorrect:

   * A message is shown ❌
5. At the end:

   * The total score is displayed 🎯

---

## 📂 Code Structure

* `answer(a)` function:

  * Takes the correct answer as input
  * Asks the user for their answer
  * Compares and updates the score

* `sumw`:

  * A global variable used to count correct answers

* `list`:

  * Stores the correct answers entered at the beginning

---

## ▶️ Example Flow

```
enter the1 answer: A
enter the2 answer: B
...

enter the student answer: A
enter the student answer: C
...
the sum is 5
```

---

## ⚠️ Notes

* The current version:

  * Uses a fixed number of questions (7)
  * Takes correct answers manually
  * Does not validate input type (letters/numbers)

---

## 🚀 Future Improvements

* Allow user to choose:

  * Number of questions 🔢
  * Type of answers (letters, numbers, etc.)
* Add input validation
* Store questions and answers in files
* Improve user interface
* Avoid using global variables
* Rename `list` to avoid conflict with Python built-in

---

## 💡 Concept

> Input → Compare → Score

---

## 👩‍💻 Author

Salwa Alhajali
