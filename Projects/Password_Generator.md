🔐 Password Generator Project

Cross-platform Password & Passphrase Generator with installers for Linux (.deb) and Windows (.exe).

password-gen/
├── password_gen.py   # Main password generator script
├── build.py          # Installer builder script
├── README.md         # Documentation
└── setup/            # (Optional) Packaging configs

1️⃣ password_gen.py — Main Program

This is the core tool that generates secure passwords or passphrases.

🔹 Full Code
#!/usr/bin/env python3
import argparse
import secrets
import string
import math
import sys
import subprocess

def generate_password(length, use_upper, use_lower, use_digits, use_symbols, exclude_ambiguous, require_each):
    # Character pools
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    if exclude_ambiguous:
        upper = upper.replace("O", "").replace("I", "")
        lower = lower.replace("l", "")
        digits = digits.replace("0", "").replace("1", "")

    pool = ""
    if use_upper: pool += upper
    if use_lower: pool += lower
    if use_digits: pool += digits
    if use_symbols: pool += symbols

    if not pool:
        raise ValueError("No character sets selected!")

    # Enforce at least one of each type
    password = []
    if require_each:
        if use_upper: password.append(secrets.choice(upper))
        if use_lower: password.append(secrets.choice(lower))
        if use_digits: password.append(secrets.choice(digits))
        if use_symbols: password.append(secrets.choice(symbols))

    # Fill rest randomly
    while len(password) < length:
        password.append(secrets.choice(pool))

    # Shuffle to remove predictability
    secrets.SystemRandom().shuffle(password)

    return "".join(password)

def generate_passphrase(num_words, wordlist_file="/usr/share/dict/words"):
    try:
        with open(wordlist_file, "r") as f:
            words = [w.strip() for w in f.readlines() if w.strip().isalpha()]
    except FileNotFoundError:
        raise ValueError("Wordlist not found! Install a dictionary file.")

    return " ".join(secrets.choice(words) for _ in range(num_words))

def calculate_entropy(pool_size, length):
    return round(math.log2(pool_size ** length), 2)

def copy_to_clipboard(text):
    if sys.platform.startswith("linux"):
        subprocess.run("xclip -selection clipboard", input=text.encode(), shell=True)
    elif sys.platform == "darwin":
        subprocess.run("pbcopy", input=text.encode(), shell=True)
    elif sys.platform == "win32":
        subprocess.run("clip", input=text.encode(), shell=True)

def main():
    parser = argparse.ArgumentParser(description="Secure Password & Passphrase Generator")
    parser.add_argument("-l", "--length", type=int, default=16, help="Password length")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("--exclude-ambiguous", action="store_true", help="Exclude ambiguous characters")
    parser.add_argument("--require-each", action="store_true", help="Require at least one of each selected type")
    parser.add_argument("--passphrase", type=int, help="Generate passphrase with N words")
    parser.add_argument("--show-entropy", action="store_true", help="Show entropy of password")
    parser.add_argument("--copy", action="store_true", help="Copy to clipboard")

    args = parser.parse_args()

    if args.passphrase:
        result = generate_passphrase(args.passphrase)
        print(result)
    else:
        result = generate_password(
            args.length,
            not args.no_upper,
            not args.no_lower,
            not args.no_digits,
            not args.no_symbols,
            args.exclude_ambiguous,
            args.require_each
        )
        print(result)
        if args.show_entropy:
            pool_size = 0
            if not args.no_upper: pool_size += len(string.ascii_uppercase)
            if not args.no_lower: pool_size += len(string.ascii_lowercase)
            if not args.no_digits: pool_size += len(string.digits)
            if not args.no_symbols: pool_size += len("!@#$%^&*()-_=+[]{}|;:,.<>?/")
            entropy = calculate_entropy(pool_size, args.length)
            print(f"Entropy: {entropy} bits")

    if args.copy:
        copy_to_clipboard(result)
        print("✅ Copied to clipboard")

if __name__ == "__main__":
    main()

🔹 Example Usage
# Generate a 20-character password
python password_gen.py -l 20 --require-each

# Generate a passphrase with 6 words
python password_gen.py --passphrase 6 --show-entropy

# Copy result to clipboard
python password_gen.py -l 16 --copy

2️⃣ build.py — Installer Builder

This script builds installers for Linux and Windows.

🔹 Full Code
import os
import platform
import subprocess
import shutil

APP_NAME = "password-gen"
VERSION = "1.0"

def build_linux():
    print("🔨 Building .deb package for Linux...")

    os.makedirs("dist/DEBIAN", exist_ok=True)
    os.makedirs("dist/usr/local/bin", exist_ok=True)

    # Control file
    control_content = f"""Package: {APP_NAME}
Version: {VERSION}
Section: utils
Priority: optional
Architecture: all
Maintainer: You <you@example.com>
Description: Secure Password & Passphrase Generator
"""
    with open("dist/DEBIAN/control", "w") as f:
        f.write(control_content)

    shutil.copy("password_gen.py", f"dist/usr/local/bin/{APP_NAME}")
    os.chmod(f"dist/usr/local/bin/{APP_NAME}", 0o755)

    subprocess.run(["dpkg-deb", "--build", "dist", f"{APP_NAME}_{VERSION}.deb"])
    print("✅ Linux .deb built!")

def build_windows():
    print("🔨 Building .exe installer for Windows...")

    subprocess.run(["pyinstaller", "--onefile", "--name", APP_NAME, "password_gen.py"])

    print("✅ Windows .exe built! Check dist/ folder")

def main():
    system = platform.system().lower()
    if "linux" in system:
        build_linux()
    elif "windows" in system:
        build_windows()
    else:
        print("❌ Unsupported OS")

if __name__ == "__main__":
    main()

    3️⃣ Linux Workflow
    # Build the installer
python build.py

# Install the .deb package
sudo dpkg -i password-gen_1.0.deb

# Run the program
password-gen -l 20 --require-each

4️⃣ Windows Workflow
# Build the installer
python build.py

# Run generated setup.exe
dist\password-gen.exe

# Then use it like:
password-gen.exe -l 20 --require-each

5️⃣ Future Improvements

GUI mode (Tkinter or PyQt)

Custom wordlists for passphrases

Password strength meter

Config file for defaults
