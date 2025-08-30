📂 Project Layout
password-gen/
├── password_gen.py        # main password generator program
├── build.py               # packaging automation script
├── requirements.txt       # Python dependencies
├── setup.cfg              # metadata for packaging
├── LICENSE
└── README.md

1. password_gen.py
#!/usr/bin/env python3
import argparse, secrets, string, math, pyperclip

def generate_password(length=16, use_upper=True, use_digits=True, use_symbols=True, require_each=False, exclude_ambiguous=False):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/`~" if use_symbols else ""
    if exclude_ambiguous:
        lower = lower.replace("l", "").replace("o", "")
        upper = upper.replace("I", "").replace("O", "")
        digits = digits.replace("0", "").replace("1", "")
    all_chars = lower + upper + digits + symbols
    if not all_chars:
        raise ValueError("No characters available for password generation.")
    password = ""
    if require_each:
        if use_upper: password += secrets.choice(upper)
        if use_digits: password += secrets.choice(digits)
        if use_symbols: password += secrets.choice(symbols)
        password += "".join(secrets.choice(lower) for _ in range(length - len(password)))
    else:
        password = "".join(secrets.choice(all_chars) for _ in range(length))
    return "".join(secrets.choice(password) for _ in range(len(password)))

def generate_passphrase(num_words=4):
    with open("/usr/share/dict/words", "r", errors="ignore") as f:
        words = [w.strip() for w in f if w.isalpha() and w.islower()]
    return " ".join(secrets.choice(words) for _ in range(num_words))

def entropy(length, charset_size):
    return round(length * math.log2(charset_size), 2)

def main():
    parser = argparse.ArgumentParser(description="Password & Passphrase Generator")
    parser.add_argument("-l", "--length", type=int, default=16, help="Password length")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("--require-each", action="store_true", help="Require at least one of each type")
    parser.add_argument("--exclude-ambiguous", action="store_true", help="Exclude ambiguous characters")
    parser.add_argument("--passphrase", type=int, help="Generate a passphrase with N words")
    parser.add_argument("--copy", action="store_true", help="Copy output to clipboard")
    parser.add_argument("--show-entropy", action="store_true", help="Show entropy")
    args = parser.parse_args()

    if args.passphrase:
        pwd = generate_passphrase(args.passphrase)
        charset_size = 7776  # diceware dictionary size
        bits = entropy(args.passphrase, charset_size)
    else:
        pwd = generate_password(
            length=args.length,
            use_upper=not args.no_upper,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
            require_each=args.require_each,
            exclude_ambiguous=args.exclude_ambiguous
        )
        charset_size = len(string.ascii_lowercase)
        if not args.no_upper: charset_size += len(string.ascii_uppercase)
        if not args.no_digits: charset_size += len(string.digits)
        if not args.no_symbols: charset_size += len("!@#$%^&*()-_=+[]{}|;:,.<>?/`~")
        bits = entropy(len(pwd), charset_size)

    print(pwd)
    if args.show_entropy:
        print(f"Entropy: {bits} bits")
    if args.copy:
        pyperclip.copy(pwd)
        print("(Copied to clipboard)")

if __name__ == "__main__":
    main()

2. build.py
import os, platform, subprocess, shutil

def build_linux():
    print("[*] Building Linux .deb package...")
    os.makedirs("dist", exist_ok=True)
    shutil.copy("password_gen.py", "dist/password-gen")
    subprocess.run(["chmod", "+x", "dist/password-gen"])
    subprocess.run(["dpkg-deb", "--build", "dist", "password-gen_1.0.deb"])
    print("[+] Built password-gen_1.0.deb")

def build_windows():
    print("[*] Building Windows EXE with PyInstaller...")
    subprocess.run(["pyinstaller", "--onefile", "password_gen.py"])
    print("[+] Built dist/password_gen.exe")
    # Optional: call Inno Setup compiler here if installed
    # subprocess.run(["iscc", "installer.iss"])

if __name__ == "__main__":
    if platform.system() == "Linux":
        build_linux()
    elif platform.system() == "Windows":
        build_windows()
    else:
        print("Unsupported OS")

3. requirements.txt
pyperclip

4. setup.cfg
[metadata]
name = password-gen
version = 1.0
description = A secure cross-platform password and passphrase generator
author = Your Name
license = MIT

[options]
packages = find:
install_requires =
    pyperclip

5. README.md
# 🔑 Password Generator

A secure cross-platform password & passphrase generator written in Python.

## Features
- Random passwords (letters, numbers, symbols, optional ambiguous exclusion)
- Passphrases (Diceware style)
- Entropy calculation
- Clipboard support
- Cross-platform: Linux, Windows, macOS

## Usage
```bash
python password_gen.py -l 20 --require-each
python password_gen.py --passphrase 6 --show-entropy

Install

Linux:

sudo dpkg -i password-gen_1.0.deb


Windows:
Run the password-gen-setup.exe installer.
