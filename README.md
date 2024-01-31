# Password Strength Checker

## Overview

This project is a web-based Password Strength Checker built using the Flask framework in Python. It's designed to evaluate the strength of passwords based on various criteria such as length, the inclusion of uppercase and lowercase letters, numbers, and special characters. Additionally, it checks the password against a list of commonly used passwords to ensure enhanced security.

## Features

- **Strength Evaluation**: Analyzes password strength based on multiple criteria.
- **Common Password Check**: Compares against a list of the most common passwords to avoid easily guessable passwords.
- **Web Interface**: User-friendly web interface for easy interaction.

## How It Works

The application uses regular expressions (regex) in Python to assess the complexity of the input password based on several factors:
- Minimum length
- Presence of uppercase and lowercase letters
- Inclusion of numeric digits
- Use of special characters

If a password meets more of these criteria, it's considered stronger. The app also checks the input password against a predefined list of common passwords (`10k-most-common.txt`) and flags it as 'Very Weak' if it matches any of these common passwords.

## Installation and Usage

### Prerequisites

- Python 3.x
- Flask

### Setup

1. Clone the repository:
   ```bash
   git clone [github.com/RebeLegend]

