# 🔐 Password Generator Project

A cross-platform **secure password & passphrase generator** written in Python, with support for packaging into Linux `.deb` and Windows `.exe` installers.

---

## 📂 Project Layout

password-gen/
│── password_gen.py # Main program (password generator)
│── build.py # Build automation script
│── setup/
│ ├── control # Debian control file template
│ └── password-gen.iss # Inno Setup script template (Windows)

python
Copy code

---

## 🏗️ `build.py` (Automation Script)

```python
#!/usr/bin/env python3
"""
Cross-platform build script for Password Generator

- On Linux: builds a .deb package
- On Windows: builds a standalone .exe + installer
"""
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

APP_NAME = "password-gen"
VERSION = "1.0"

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
SETUP = ROOT / "setup"
DIST.mkdir(exist_ok=True)

def run(cmd, shell=False):
    print(f"[+] Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    subprocess.run(cmd, shell=shell, check=True)

def build_deb():
    pkg_dir = ROOT / f"{APP_NAME}_{VERSION}"
    bin_dir = pkg_dir / "usr/local/bin"
    debian_dir = pkg_dir / "DEBIAN"

    # Clean old build
    if pkg_dir.exists():
        shutil.rmtree(pkg_dir)
    bin_dir.mkdir(parents=True)
    debian_dir.mkdir(parents=True)

    # Copy script
    shutil.copy(ROOT / "password_gen.py", bin_dir / APP_NAME)
    os.chmod(bin_dir / APP_NAME, 0o755)

    # Control file
    control_file = debian_dir / "control"
    with open(SETUP / "control") as f:
        control_file.write_text(f.read().replace("VERSION", VERSION))

    # Build .deb
    run(["dpkg-deb", "--build", str(pkg_dir)])
    shutil.move(f"{pkg_dir}.deb", DIST / f"{APP_NAME}_{VERSION}.deb")
    print(f"[✔] Built {DIST / f'{APP_NAME}_{VERSION}.deb'}")

def build_windows():
    # Ensure pyinstaller
    try:
        import PyInstaller  # noqa
    except ImportError:
        run([sys.executable, "-m", "pip", "install", "pyinstaller"])

    # Build exe
    run(["pyinstaller", "--onefile", "password_gen.py"])
    exe_path = ROOT / "dist" / "password_gen.exe"

    # Inno Setup installer
    iss_template = (SETUP / "password-gen.iss").read_text()
    iss_file = ROOT / "password-gen.iss"
    iss_file.write_text(iss_template.replace("VERSION", VERSION))

    # Compile installer
    iscc = r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
    if not Path(iscc).exists():
        print("[!] Install Inno Setup 6 and update ISCC.exe path in build.py")
        return
    run([iscc, str(iss_file)], shell=True)

    print("[✔] Windows installer built (check Output folder in Inno Setup).")

def main():
    system = platform.system()
    if system == "Linux":
        build_deb()
    elif system == "Windows":
        build_windows()
    else:
        print(f"[!] Unsupported OS: {system}")

if __name__ == "__main__":
    main()
📄 setup/control (Debian Template)
text
Copy code
Package: password-gen
Version: VERSION
Section: utils
Priority: optional
Architecture: all
Depends: python3, python3-pyperclip
Maintainer: Your Name <you@email.com>
Description: Secure Password & Passphrase Generator
 Generates strong passwords or diceware-style passphrases with entropy estimation.
📄 setup/password-gen.iss (Inno Setup Template)
pascal
Copy code
[Setup]
AppName=Password Generator
AppVersion=VERSION
DefaultDirName={autopf}\PasswordGen
DefaultGroupName=PasswordGen
OutputBaseFilename=password-gen-setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\password_gen.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Password Generator"; Filename: "{app}\password_gen.exe"
Name: "{commondesktop}\Password Generator"; Filename: "{app}\password_gen.exe"
🚀 Usage
Linux
bash
Copy code
python3 build.py
Creates:

bash
Copy code
dist/password-gen_1.0.deb
Install with:

bash
Copy code
sudo dpkg -i dist/password-gen_1.0.deb
Windows
powershell
Copy code
python build.py
Creates:

arduino
Copy code
password-gen-setup.exe
🔑 password_gen.py
This is the main program — the password & passphrase generator.

Example usage
bash
Copy code
python password_gen.py -l 20 --require-each
python password_gen.py --passphrase 6 --show-entropy
Features
Generates secure random passwords (letters, digits, symbols, etc.)

Option to exclude ambiguous characters (0/O, 1/l/I, etc.)

Enforce at least one of each selected character type

Supports Diceware-style passphrases

Calculates entropy (strength estimate)

Optional --copy to clipboard

Works on Linux, Windows, and macOS

🏗️ build.py
This is the automation script for packaging (not for end-users).

On Linux: builds .deb → password-gen_1.0.deb

On Windows: builds .exe → password-gen-setup.exe

⚡ Example Developer Workflow
bash
Copy code
# Edit main generator
nano password_gen.py

# Build installers
python build.py
Results:

Linux: dist/password-gen_1.0.deb

Windows: password-gen-setup.exe
