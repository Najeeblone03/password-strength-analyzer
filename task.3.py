import re
import math

common_passwords = [
    "password", "123456", "12345678", "qwerty",
    "admin", "welcome", "letmein", "abc123"
]

def calculate_entropy(password):
    charset = 0

    if re.search(r'[a-z]', password):
        charset += 26
    if re.search(r'[A-Z]', password):
        charset += 26
    if re.search(r'[0-9]', password):
        charset += 10
    if re.search(r'[^A-Za-z0-9]', password):
        charset += 32

    if charset == 0:
        return 0

    return round(len(password) * math.log2(charset), 2)

def estimate_crack_time(entropy):
    guesses_per_second = 1e9
    seconds = (2 ** entropy) / guesses_per_second

    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    else:
        return f"{seconds/31536000:.2f} years"

def password_checker(password):

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 10
    else:
        suggestions.append("Increase length to at least 8 characters")

    if len(password) >= 12:
        score += 10

    if re.search(r'[A-Z]', password):
        score += 15
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r'[a-z]', password):
        score += 15
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r'[0-9]', password):
        score += 15
    else:
        suggestions.append("Add numbers")

    if re.search(r'[^A-Za-z0-9]', password):
        score += 20
    else:
        suggestions.append("Add special characters")

    if password.lower() in common_passwords:
        score -= 40
        suggestions.append("Password found in common password database")

    if re.search(r'(.)\1{2,}', password):
        score -= 10
        suggestions.append("Avoid repeated characters")

    sequences = [
        "123456789",
        "abcdefghijklmnopqrstuvwxyz",
        "qwertyuiop"
    ]

    for seq in sequences:
        if password.lower() in seq:
            score -= 20
            suggestions.append("Avoid sequential patterns")
            break

    entropy = calculate_entropy(password)

    if entropy >= 80:
        score += 15
    elif entropy >= 60:
        score += 10
    elif entropy >= 40:
        score += 5

    score = max(0, min(score, 100))

    if score < 30:
        strength = "Very Weak"
    elif score < 50:
        strength = "Weak"
    elif score < 70:
        strength = "Medium"
    elif score < 85:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, strength, entropy, suggestions

password = input("Enter Password: ")

score, strength, entropy, suggestions = password_checker(password)

print("\n" + "="*40)
print("      PASSWORD SECURITY REPORT")
print("="*40)

print(f"Password Strength : {strength}")
print(f"Security Score    : {score}/100")
print(f"Entropy           : {entropy} bits")
print(f"Estimated Crack Time : {estimate_crack_time(entropy)}")

if suggestions:
    print("\nSecurity Recommendations:")
    for i, item in enumerate(suggestions, 1):
        print(f"{i}. {item}")
else:
    print("\nExcellent Password! No issues detected.")

print("\nPassword Policy:")
print("- Minimum 12 characters")
print("- Use uppercase and lowercase letters")
print("- Include numbers")
print("- Include special symbols")
print("- Avoid common passwords")
print("- Avoid predictable patterns")