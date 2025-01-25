# This program checks to see if your email is spam or not. It gauges it based on the spam score then tells you the possibility of it being spam.

import re

# All the common spam words.
def get_spam_keywords():
    return [
        "free", "win", "winner", "congratulations", "click here", "urgent",
        "offer", "limited time", "act now", "risk-free", "guarantee", "bonus",
        "buy now", "cash prize", "cheap", "discount", "exclusive deal",
        "money back", "no cost", "amazing", "investment", "lottery", "payout",
        "earn", "fast cash", "refund", "credit card", "income", "online pharmacy",
        "viagra", "luxury"
    ]

# Calculates the spam score for your message.
def calculate_spam_score(message, keywords):
    spam_score = 0
    spam_words_found = []

    for keyword in keywords:
        if re.search(rf"\b{re.escape(keyword)}\b", message, re.IGNORECASE):
            spam_score += 1
            spam_words_found.append(keyword)

    return spam_score, spam_words_found

# Tells you whether the message is spam based on the score you receive.
def determine_spam_likelihood(score):
    if score == 0:
        return "Not Spam"
    elif 1 <= score <= 3:
        return "Low possibility of being spam"
    elif 4 <= score <= 6:
        return "Moderate possibility of being spam"
    elif 7 <= score <= 10:
        return "High possibility of being spam"
    else:
        return "Very high possibility of being spam"

# Function for checking inputs, calculating spam score, and showing the end result.
def main():
    keywords = get_spam_keywords()

    # Needs user to input message.
    email_message = input("Enter email message: ").strip()

    # Calculates the spam score.
    spam_score, spam_words_found = calculate_spam_score(email_message, keywords)

    # Determine the possibility of spam.
    spam_likelihood = determine_spam_likelihood(spam_score)

    # Displays results.
    print("\nSpam Results:")
    print(f"Spam Score: {spam_score}")
    print(f"Possibility of Spam: {spam_likelihood}")
    if spam_words_found:
        print("Spam-causing Words/Phrases Found:", ", ".join(spam_words_found))
    else:
        print("No spam words found in the message.")

if __name__ == "__main__":
    main()
