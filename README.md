# 🐂 Cows and Bulls - Python Game

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-CLI-green)
![Git](https://img.shields.io/badge/Git-Version_Control-orange?logo=git)

## 📌 Project Overview

A command-line number guessing game developed using Python.
The player must guess a randomly generated three-digit
number within 10 valid attempts using Bulls and Cows hints.

## 🚀 Features

- Random secret number generation
- Unique digit validation
- Bulls and Cows scoring system
- Limited attempts
- User input validation
- Winning and losing conditions
- Replay functionality

## 🎮 Game Rules

- Bull: Correct digit in the correct position.
- Cow: Correct digit in the wrong position.
- The secret number contains three unique digits.
- The player has 10 valid attempts.
- Invalid guesses do not consume attempts.

### Example

Secret number: 604

| Guess | Bulls | Cows |
|-------|-------|------|
| 123   | 0     | 0    |
| 640   | 1     | 2    |
| 624   | 2     | 0    |
| 604   | 3     | 0    |

## 🛠️ Technologies Used

- Python 3
- Git and GitHub
- AWS EC2
- MobaXterm
- Linux

## ⚙️ How to Run

Clone the repository:

```bash
git clone https://github.com/Ajoy8688/Cows-and-Bulls-Python-game.git
```

Navigate to the project directory:

```bash
cd Cows-and-Bulls-Python-game
```

Run the application:

```bash
python3 cows_and_bulls.py
```

## 👨‍💻 Author

Developed by [Ajoy8688](https://github.com/Ajoy8688)

This project is part of my Python and DevOps learning journey.
