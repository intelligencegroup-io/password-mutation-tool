# 🔐 Password Mutation & Generation Tool

## Overview

This tool is designed for **penetration testers, security researchers, and ethical hackers** who need to generate large wordlists by mutating given keywords using **Hashcat rule files**. It efficiently applies multiple transformation rules to input words, producing **millions of password variations** while ensuring **deduplication and optimised sorting**.

Unlike traditional wordlist generators, this tool:

- 🚀 **Runs entirely in memory** for maximum speed.
- 🔄 **Automatically removes duplicates** during processing.
- 📊 **Provides real-time progress updates** for both rule processing and sorting.
- 💾 **Saves a final sorted wordlist** optimised for security testing.

## 🔧 How It Works

### 1️⃣ Input

- The user provides a **comma-separated list of keywords** (e.g., `companyname, admin, password123`).
- The script scans the `rules/` directory for **Hashcat rule files** (`.rule`).

### 2️⃣ Processing

- For each keyword, Hashcat is run with **each rule file** to generate password variations.
- The output is stored in a **Python `set`** to ensure **uniqueness**.
- Invalid or unsupported rules are ignored (handled natively by Hashcat).

### 3️⃣ Sorting & Output

- Once all rules are processed, **the unique passwords are sorted with a live progress bar**.
- The final **sorted** wordlist is saved as `generated_passwords_YYYY-MM-DD_HH-MM-SS.txt`.
- The tool estimates **file size and total unique passwords** before exiting.

## 📌 Features

✅ **High-Speed Execution** – Everything runs in RAM to avoid slow disk writes.  
✅ **Real-Time Progress Tracking** – Live feedback during generation, sorting, and saving.  
✅ **Automatic Deduplication** – Eliminates redundant entries before sorting.  
✅ **Supports Any Hashcat Rule Files** – Works with custom `.rule` files.  
✅ **Optimised for Large Wordlists** – Handles **millions of passwords efficiently**.  

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/intelligencegroup-io/password-mutation-tool.git
cd password-mutation-tool
```

### 2️⃣ Set Up a Virtual Environment

It is recommended to use a virtual environment to avoid conflicts with system packages:

```bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows use: myenv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install Hashcat

Ensure Hashcat is installed on your system:

```bash
sudo apt install hashcat  # Linux
brew install hashcat  # macOS
choco install hashcat  # Windows (using Chocolatey)
```

## 📥 Usage

### Run the Script

```bash
python3 generate_passwords.py
```

### Example Usage

```bash
Enter keywords (comma-separated): secure,password123,admin
```

💡 **Tip:** The more keywords you enter, the larger the output wordlist will be!

## 📜 Example Output

```
🔹 Processing keyword: password with rule file: best64.rule
✅ Generated 1,234 variations for password
  ➜ Password
  ➜ p@ssword
  ➜ P@ssw0rd
  ➜ passw0rd
  ➜ password123...

🔹 Processing keyword: password with rule file: toggles3.rule
✅ Generated 3,567 variations for password
  ➜ Password
  ➜ pAsSwOrD
  ➜ PassWord
  ➜ passWORD
  ➜ PASSWORD...

Sorting 42,465,809 unique passwords...
✅ Sorted and saved to generated_passwords_2024-06-01_12-30-45.txt
```

## 🔬 Technical Details

### **Efficiency Optimisations**

- **Python `set` for deduplication**: Avoids duplicate entries **before sorting**.
- **Sorting with tqdm**: Provides a **visual progress bar** during sorting.
- **Batch writing**: Avoids frequent disk I/O by writing in large chunks.

### **Why This is Faster Than Traditional Methods**

❌ **Inefficient Approach**: Writing all results to a file first and sorting later = **slow & disk-heavy**.  
✅ **Optimised Approach**: Store in memory (`set`), then sort **only unique values** at the end.

### **Handling Large Datasets**

- This tool efficiently processes **tens of millions of entries** in memory.
- For extreme-scale wordlists, consider running on a machine with **sufficient RAM** (16GB+ recommended).

## 🚀 Future Enhancements

- Multi-threading for **parallel Hashcat execution**.
- GPU acceleration for **even faster password generation**.
- Custom wordlist merging & adaptive rule selection.

## 🏆 Contributing

Want to improve this tool? Fork the repo and submit a PR! Bug reports & feature requests are welcome.

## ⚠️ Disclaimer

This tool is for **ethical hacking & security research** only. Unauthorised use against systems without permission is illegal. The developers are **not responsible for misuse**.

---

💡 **Built for speed, optimised for security.** Happy cracking! 🚀
