
# 🔐 D3CRYPT

A simple yet effective **file encryption/decryption** tool using Python's `cryptography` library and `tkinter` for GUI file selection.

## 📦 Features

- Encrypt and decrypt files with a Fernet key
- Option to generate or load your own encryption key
- Brute-force decryption support using a key wordlist
- Cross-platform terminal support (clears screen depending on OS)
- Pretty CLI interface with `colorama` and ASCII art

## 🚀 Requirements

- Python 3.8+
- Packages:
  - `cryptography`
  - `colorama`
  - `tkinter` (comes with standard Python on most OSes)

Install dependencies (recommended in a virtualenv):

```
pip install -r requirements.txt
```

## 🛠 Usage

Run the script:

```
python D3CRYPT.py
```

You will see a menu like:

```
[01] Encrypt
[02] Decrypt
[00] Quit
```

### 🔐 Encrypt

1. Choose to generate a new key or input an existing one.
2. Select the file you want to encrypt.
3. Encrypted content will overwrite the original file.

### 🔓 Decrypt

1. If you have the key, input it and select the file.
2. If not, select a wordlist with one Fernet key per line.
3. The program will try all keys in the list until one works.

## 📁 Wordlist Format

Plain `.txt` file with one key per line:

```
yYBqeqc5GpPPpYwPb0dch6VK4p5-n9TgfjUoEbm26zM=
dLkD9rYOVzHOyIzacT1H_uNsDPAk0EorxJX9PB9zWJY=
...
```

## ⚠️ Warnings

- The tool **overwrites files** after encryption/decryption — make backups if needed.
- Only works with files previously encrypted with Fernet keys.
- Brute force may take time depending on wordlist size.

## 🧠 Credits

Created by a curious mind. Use responsibly. 😈
