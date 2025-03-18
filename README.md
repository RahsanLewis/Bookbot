# 📚 BookBot

## Overview
BookBot is a Python script designed to analyze text files (such as books) and provide a detailed report of the total word count and a sorted list of character frequencies (letters only).

---

## Features
- Calculates the total number of words in a text file.
- Generates a character frequency report (alphabetical characters only).
- Sorts the character frequency report from greatest to least.

---

## Requirements
- Python 3.7 or higher

---

## File Structure
```
BookBot
├── main.py
├── stats.py
└── books
    └── frankenstein.txt (example book file)
```

---

## How to Use

### Step 1: Clone or download the project.

```bash
git clone <your_repository_url>
cd BookBot
```

### Step 2: Place your book file in the `books` directory or use the provided example.

### Step 3: Run the program

```bash
python3 main.py books/frankenstein.txt
```

Replace `books/frankenstein.txt` with the path to your desired text file.

---

## Example Output

```
============== BOOKBOT ==============
Analyzing book found at books/frankenstein.txt...
------------- Word Count ------------
Found 75767 total words
---------- Character Count ----------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
...
```

---

## Files and Functions Explanation
- **`main.py`**: The entry point of the application; handles user input and printing the report.
- **`stats.py`**: Contains helper functions:
    - `get_num_words(file)`: Returns the total word count.
    - `num_dict(file)`: Returns a dictionary of character frequencies.
    - `sort_dict(nums_dict)`: Converts and sorts the character frequency dictionary into a list.

---

## Notes
- Ensure that the text file used is properly formatted and readable.
- Non-alphabetical characters are automatically ignored when generating the character frequency report.

Enjoy analyzing your books with BookBot! 📖✨

