🔐 Password Generator Project

A cross-platform Password & Passphrase Generator with setup installers for Linux (.deb) and Windows (.exe).

📂 Project Structure
password-gen/
├── password_gen.py   # Main password generator script
├── build.py          # Packaging/installer builder script
├── README.md         # Documentation
└── setup/            # Packaging configs (Linux/Windows)

1️⃣ password_gen.py — Main Program

This is the actual password generator tool.

Features

Generate random passwords with length control

Options to include/exclude digits, symbols, uppercase, lowercase

Exclude ambiguous characters (0/O, 1/l/I)

Require at least one of each chosen type (--require-each)

Generate passphrases (--passphrase)

Calculate entropy (--show-entropy)

Copy password to clipboard (--copy)

Cross-platform: Linux, Windows, macOS

Code
#!/usr/bin/env python3
import argparse
import random
import secrets
import string
import math
import sys

try:
    import pyperclip
except ImportError:
    pyperclip = None


def calculate_entropy(charset_size, length):
    return round(length * math.log2(charset_size), 2)


def generate_password(length, use_digits, use_symbols, use_upper, use_lower,
                      exclude_ambiguous, require_each):
    digits = "23456789" if exclude_ambiguous else string.digits
    lower = "abcdefghijkmnopqrstuvwxyz" if exclude_ambiguous else string.ascii_lowercase
    upper = "ABCDEFGHJKLMNPQRSTUVWXYZ" if exclude_ambiguous else string.ascii_uppercase
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?" if exclude_ambiguous else string.punctuation

    pool = ""
    if use_digits:
        pool += digits
    if use_symbols:
        pool += symbols
    if use_upper:
        pool += upper
    if use_lower:
        pool += lower

    if not pool:
        raise ValueError("No character sets selected!")

    if require_each:
        password = []
        if use_digits:
            password.append(secrets.choice(digits))
        if use_symbols:
            password.append(secrets.choice(symbols))
        if use_upper:
            password.append(secrets.choice(upper))
        if use_lower:
            password.append(secrets.choice(lower))
        while len(password) < length:
            password.append(secrets.choice(pool))
        random.shuffle(password)
        return "".join(password)
    else:
        return "".join(secrets.choice(pool) for _ in range(length))


def generate_passphrase(num_words):
    wordlist = ["apple", "sky", "river", "stone", "knight", "shadow",
                "flame", "storm", "wolf", "sword", "light", "dark",
                "void", "star", "earth", "wind", "fire", "ice", "time", "dream"]
    return " ".join(secrets.choice(wordlist) for _ in range(num_words))


def main():
    parser = argparse.ArgumentParser(description="Password & Passphrase Generator")
    parser.add_argument("-l", "--length", type=int, default=16,
                        help="Password length (default: 16)")
    parser.add_argument("--digits", action="store_true", help="Include digits")
    parser.add_argument("--symbols", action="store_true", help="Include symbols")
    parser.add_argument("--upper", action="store_true", help="Include uppercase")
    parser.add_argument("--lower", action="store_true", help="Include lowercase")
    parser.add_argument("--exclude-ambiguous", action="store_true", help="Exclude ambiguous chars")
    parser.add_argument("--require-each", action="store_true", help="Require at least one of each type")
    parser.add_argument("--passphrase", type=int, help="Generate a passphrase with N words")
    parser.add_argument("--show-entropy", action="store_true", help="Show entropy estimate")
    parser.add_argument("--copy", action="store_true", help="Copy password to clipboard")

    args = parser.parse_args()

    if args.passphrase:
        result = generate_passphrase(args.passphrase)
        charset_size = 20  # size of the toy wordlist
        entropy = calculate_entropy(charset_size, args.passphrase)
    else:
        # Default sets to True if no options given
        if not (args.digits or args.symbols or args.upper or args.lower):
            args.digits = args.symbols = args.upper = args.lower = True

        result = generate_password(args.length, args.digits, args.symbols,
                                   args.upper, args.lower, args.exclude_ambiguous,
                                   args.require_each)
        pool_size = 0
        if args.digits:
            pool_size += len("23456789" if args.exclude_ambiguous else string.digits)
        if args.symbols:
            pool_size += len("!@#$%^&*()-_=+[]{};:,.<>?" if args.exclude_ambiguous else string.punctuation)
        if args.upper:
            pool_size += len("ABCDEFGHJKLMNPQRSTUVWXYZ" if args.exclude_ambiguous else string.ascii_uppercase)
        if args.lower:
            pool_size += len("abcdefghijkmnopqrstuvwxyz" if args.exclude_ambiguous else string.ascii_lowercase)
        entropy = calculate_entropy(pool_size, args.length)

    print(result)
    if args.show_entropy:
        print(f"Entropy: {entropy} bits")
    if args.copy:
        if pyperclip:
            pyperclip.copy(result)
            print("Copied to clipboard.")
        else:
            print("Pyperclip not installed. Clipboard feature unavailable.")


if __name__ == "__main__":
    main()

2️⃣ build.py — Installer Builder

This script builds cross-platform installers.

On Linux → creates a .deb package

On Windows → creates an .exe installer

Code
#!/usr/bin/env python3
import os
import platform
import subprocess
import shutil

APP_NAME = "password-gen"
VERSION = "1.0"


def build_linux():
    print("[*] Building .deb package for Linux...")
    os.makedirs("dist/DEBIAN", exist_ok=True)
    os.makedirs("dist/usr/local/bin", exist_ok=True)

    # Control file
    control = f"""Package: {APP_NAME}
Version: {VERSION}
Section: utils
Priority: optional
Architecture: all
Maintainer: You <you@example.com>
Description: Cross-platform Password Generator
"""
    with open("dist/DEBIAN/control", "w") as f:
        f.write(control)

    # Copy main script
    shutil.copy("password_gen.py", "dist/usr/local/bin/password-gen")
    os.chmod("dist/usr/local/bin/password-gen", 0o755)

    subprocess.run(["dpkg-deb", "--build", "dist", f"{APP_NAME}_{VERSION}.deb"])
    print(f"[+] Built {APP_NAME}_{VERSION}.deb")


def build_windows():
    print("[*] Building Windows .exe installer...")
    subprocess.run(["pyinstaller", "--onefile", "password_gen.py", "-n", APP_NAME])

    iss_content = f"""
[Setup]
AppName={APP_NAME}
AppVersion={VERSION}
DefaultDirName={{pf}}\\{APP_NAME}
OutputBaseFilename={APP_NAME}-setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\\{APP_NAME}.exe"; DestDir: "{{app}}"; Flags: ignoreversion

[Icons]
Name: "{{group}}\\{APP_NAME}"; Filename: "{{app}}\\{APP_NAME}.exe"
"""
    with open("installer.iss", "w") as f:
        f.write(iss_content)

    subprocess.run(["iscc", "installer.iss"])
    print("[+] Windows installer built.")


if __name__ == "__main__":
    system = platform.system()
    if system == "Linux":
        build_linux()
    elif system == "Windows":
        build_windows()
    else:
        print("Unsupported OS.")

3️⃣ Linux Installation
# Build the installer
python build.py

# Install the .deb package
sudo dpkg -i password-gen_1.0.deb

# Run the program
password-gen -l 20 --require-each

4️⃣ Windows Installation
# Build the installer
python build.py

# Run generated setup.exe
dist\password-gen-setup.exe

# Then use it like:
password_gen.exe -l 20 --require-each
