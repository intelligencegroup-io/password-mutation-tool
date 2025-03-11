# 🔐 Password Mutation & Generation Tool

## Overview

This tool is designed for **penetration testers, security researchers, and ethical hackers** who need to generate **custom password lists for targeted penetration tests**. By leveraging **Hashcat rule files**, the tool applies advanced transformations to user-provided keywords, creating **highly realistic password variations** that match an organisation’s or individual’s likely password choices.

Unlike traditional wordlist generators, this tool:

- 🚀 **Runs entirely in memory** for maximum speed.
- 🎯 **Optimised for targeted attacks** by using real-world password mutation rules.
- 🔄 **Automatically removes duplicates** during processing.
- 📊 **Provides real-time progress updates** for both rule processing and sorting.
- 💾 **Saves a final sorted wordlist**, optimised for password cracking and security assessments.

## 🔧 How It Works

### 1️⃣ Input

- The user provides **targeted keywords** (e.g., company names, usernames, common passwords).
- The script scans the `rules/` directory for **Hashcat rule files** (`.rule`), which contain **real-world password mutation patterns**.

### 2️⃣ Processing

- Each keyword is **transformed using Hashcat rules**, mimicking how real users create passwords.
- The generated variations are stored **in memory** to ensure high-speed execution.
- Invalid or unsupported rules are automatically skipped.

### 3️⃣ Sorting & Output

- The tool **deduplicates** passwords and sorts them efficiently with a **progress bar**.
- The final **sorted and unique** password list is saved as `generated_passwords_YYYY-MM-DD_HH-MM-SS.txt`.
- The tool estimates **file size and total unique passwords** before exiting.

## 📌 Features

✅ **High-Speed Execution** – Runs entirely in RAM to avoid slow disk writes.\
✅ **Targeted Wordlist Generation** – Uses real-world mutation rules for **maximum effectiveness**.\
✅ **Real-Time Progress Tracking** – Live feedback during generation, sorting, and saving.\
✅ **Automatic Deduplication** – Eliminates redundant entries **before sorting**.\
✅ **Supports Any Hashcat Rule Files** – Works with custom `.rule` files.\
✅ **Optimised for Large Wordlists** – Handles **millions of passwords efficiently**.

## 🎯 Use Case: Targeted Penetration Testing

This tool is perfect for **red team engagements and security audits**, allowing testers to generate **highly realistic** password lists for specific targets.

### **Example Scenario**

A penetration tester is assessing an organisation named **"AcmeCorp"**. Instead of using a generic wordlist, they can:

```bash
Enter keywords (comma-separated): AcmeCorp
```

The tool applies **real-world password transformations**, generating:

```
AcmeCorp!
Acm3Corp
Acme2024#
Acmecorp2024
```

This makes **password attacks more efficient** by focusing on **high-probability guesses** rather than brute-force methods.

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/intelligencegroup-io/password-mutation-tool.git
cd password-mutation-tool
```

### 2️⃣ Set Up a Virtual Environment

To avoid conflicts with system packages, set up a virtual environment:

```bash
python3 -m venv myenv && source myenv/bin/activate  # On Windows use: myenv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install Hashcat

Ensure Hashcat is installed:

```bash
sudo apt install hashcat  # Linux
brew install hashcat  # macOS
choco install hashcat  # Windows (Chocolatey)
```

## 📥 Usage

### Run the Script

```bash
python3 generate_passwords.py
```

### Example Usage

```bash
Enter keywords (comma-separated): password
```

💡 **Tip:** The more **context-aware** your keywords, the better the results!

## 📜 Example Output

```
🔹 Processing keyword: password with rule file: best64.rule
✅ Generated 1,234 variations for password
  ➜ Password!
  ➜ p@ssword
  ➜ P@ssw0rd
  ➜ passw0rd123
  ➜ password2024...

🔹 Processing keyword: password with rule file: toggles3.rule
✅ Generated 3,567 variations for password
  ➜ Password
  ➜ pAsSwOrD
  ➜ PassWord!
  ➜ PASSWORD123
  ➜ password#1...

Sorting 42,465,809 unique passwords...
✅ Sorted and saved to generated_passwords_2024-06-01_12-30-45.txt
```

## 🔬 Technical Details

### **Efficiency Optimisations**

- **Python `set` for deduplication**: Ensures **only unique passwords** are stored.  
- **Sorting with tqdm**: Provides a **real-time progress bar** during sorting.  
- **Batch writing**: Reduces disk I/O for faster performance.  

### **Why This is Faster Than Traditional Methods**

❌ **Inefficient Approach**: Writing results to a file and sorting later is **slow & disk-heavy**.\
✅ **Optimised Approach**: Store in **memory (`set`)**, then sort **only unique values** at the end.

### **Handling Large Datasets**

- This tool efficiently processes **tens of millions of entries** in RAM.
- For **extreme-scale wordlists**, use a machine with **16GB+ RAM**.

## 🚀 Future Enhancements

- Multi-threading for **parallel Hashcat execution**.
- GPU acceleration for **even faster password generation**.
- **Custom rule selection** based on **targeted attack profiles**.

## 🏆 Contributing

Want to improve this tool? Fork the repo and submit a PR! Bug reports & feature requests are welcome.

## ⚠️ Disclaimer

This tool is for **ethical hacking & security research** only. Unauthorised use against systems without permission is illegal. The developers are **not responsible for misuse**.

---

💡 **Built for targeted penetration testing, optimised for speed.** Happy cracking! 🚀
