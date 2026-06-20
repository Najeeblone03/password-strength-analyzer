# Password Strength Analyzer

## Project Description

Password Strength Analyzer is a Python-based security assessment tool designed to evaluate password robustness using industry-standard metrics. The application analyzes password composition, calculates entropy, estimates brute-force crack time, and generates actionable recommendations to enhance password security.

This project demonstrates fundamental cybersecurity concepts, including password policy enforcement, entropy analysis, pattern recognition, and secure authentication practices.

## Key Features

* Comprehensive password strength evaluation
* Security scoring system (0–100)
* Entropy calculation for randomness assessment
* Brute-force crack time estimation
* Detection of commonly used passwords
* Identification of repeated characters
* Detection of sequential and predictable patterns
* Automated security recommendations
* Password policy validation

## Technologies Used

* Python 3
* Regular Expressions (re)
* Math Library (math)

## Evaluation Criteria

The analyzer assesses passwords based on:

* Password length
* Uppercase characters
* Lowercase characters
* Numeric characters
* Special characters
* Entropy level
* Common password exposure
* Repeated character patterns
* Sequential keyboard and numeric patterns

## Sample Output

```text
========================================
      PASSWORD SECURITY REPORT
========================================

Password Strength : Strong
Security Score    : 85/100
Entropy           : 78.65 bits
Estimated Crack Time : 12.34 years
```

## Installation and Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/password-strength-analyzer.git
```

2. Navigate to the project directory:

```bash
cd password-strength-analyzer
```

3. Execute the program:

```bash
python password_strength_analyzer.py
```

4. Enter a password when prompted to receive a detailed security analysis.

## Security Recommendations

The tool encourages the following password best practices:

* Use a minimum of 12 characters
* Combine uppercase and lowercase letters
* Include numbers and special symbols
* Avoid common passwords
* Avoid repeated characters
* Avoid predictable sequences and keyboard patterns

## Learning Outcomes

This project highlights practical applications of:

* Cybersecurity fundamentals
* Password security analysis
* Entropy-based strength measurement
* Pattern detection techniques
* Python programming

## Author

Najeeb Lone


