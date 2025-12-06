# 🔐 Smart Password Validator: A Discrete Math Approach

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?style=for-the-badge&logo=flask)
![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=for-the-badge&logo=vercel)

> **A Cybersecurity application that bridges the gap between Theoretical Discrete Mathematics and practical Defensive Engineering.**

## 📌 Project Overview
Unlike standard password checkers that only look at length or special characters, this tool is **Context-Aware**. It utilizes concepts from **Set Theory** and **Permutations** to detect passwords that are vulnerable to **Social Engineering** and **Dictionary Attacks** based on a user's personal profile.

### Key Features
* **Context-Aware Blacklisting:** Generates a dynamic "blacklist" set based on user input (Name, Year, Partner, Pet) using mathematical permutations.
* **Mathematical Strength Analysis:** Calculates the raw entropy of a password using the Multiplication Rule of Counting.
* **Real-time Feedback:** Visualizes password strength with a reactive UI.
* **Cyber-Themed UI:** A responsive, dark-mode interface built with custom CSS.

---

## 📐 Mathematical Foundation
This project transforms theoretical concepts from a standard Discrete Mathematics curriculum into functional code.

### 1. Permutations (The "Blacklist" Logic)
To detect passwords derived from personal data, we treat user inputs as a set of distinct objects. We calculate the Permutations ($nPr$) of these objects to generate a set of likely password combinations.

$$P(n,r) = \frac{n!}{(n-r)!}$$

* **Application:** If a user inputs `{"John", "1995", "Rocky"}`, the system generates permutations like `John1995`, `RockyJohn`, `1995Rocky`, etc., and adds them to a rejection set.

### 2. Set Theory (The Validator)
* **Concept:** Set Membership ($x \in S$).
* **Application:** The generated permutations form a "Weak Set" ($S$). The validator checks if the Input Password ($x$) exists within $S$. If $x \in S$, the password is instantly rejected regardless of its complexity.

### 3. The Multiplication Rule (Entropy)
To measure the true strength of a password against brute-force attacks, we use the Multiplication Rule of Counting to find the total search space ($N$).

$$N = P^L$$

Where:
* $P$ = **Pool Size** (26 lowercase + 26 uppercase + 10 digits + 32 symbols).
* $L$ = **Length** of the password.

**Entropy (Bits)** is then calculated as: $E = \log_2(N)$

---

## 🚀 Installation & Local Run

### Prerequisites
* Python 3.x
* Pip

### Steps
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/MOHAMADFAWZI-911/smart-password-validator.git
    cd smart-password-validator
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    ```bash
    python app.py
    ```

4.  **Access**
    Open your browser and navigate to: `http://127.0.0.1:5000`

---

## 📂 Project Structure
The project is architected for deployment on Serverless platforms (Vercel) using Flask.

```text
/smart-password-validator
├── static/
│   └── style.css       # Custom Dark Mode Styling
├── templates/
│   └── index.html      # Jinja2 Frontend Template
├── app.py              # Flask Backend (Permutations & Logic)
├── requirements.txt    # Python Dependencies
├── vercel.json         # Vercel Deployment Config
└── README.md           # Documentation

