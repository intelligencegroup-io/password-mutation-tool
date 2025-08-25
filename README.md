# 🔐 Targeted Password List Generator

## Overview

This tool is designed for **red teamers, penetration testers, and security researchers** who need to generate **highly targeted password lists for password hash cracking**. By leveraging **Hashcat rule files**, the tool applies advanced transformations to user-provided keywords, creating **realistic password variations** that align with an organisation's password patterns.

## 🎯 Use Case: Password Hash Cracking in Red Team Engagements

When a red team captures a **password hash**, they can use this tool to generate **context-aware, high-probability password guesses** based on the target organisation’s naming conventions, culture, and password tendencies.

### **Example Scenario**

A penetration tester has captured a hash from an organisation named **"AcmeCorp"**. Instead of relying on generic wordlists, they can generate tailored variations:

```bash
Enter keywords (comma-separated): AcmeCorp
```

The tool applies **real-world password transformations**, generating:

```
AcmeCorp!
Acm3Corp
Acme2024#
Acmecorp2024
AcmeC0rp!
```

This approach **increases password cracking efficiency** by focusing on **high-probability guesses**, reducing the need for broad brute-force attacks.

## 📌 Features

✅ **Supports Compressed Rule Files** – The tool automatically extracts and processes `.7z` compressed Hashcat rules.  
✅ **Highly Targeted Wordlist Generation** – Uses company-specific keywords for **more accurate password guesses**.  
✅ **Optimised for Hash Cracking** – Prioritises **realistic, high-probability mutations** over brute-force approaches.  
✅ **Real-Time Processing** – Runs entirely in **RAM** for maximum speed.  
✅ **Automatic Deduplication** – Ensures a clean and optimised wordlist.  
✅ **Supports Any Hashcat Rule Files** – Works with **custom or pre-existing** `.rule` files.  
✅ **Efficient Large-Scale Processing** – Handles **millions of password variations** efficiently.

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/intelligencegroup-io/password-mutation-tool.git
cd password-mutation-tool
```

### 2️⃣ Set Up a Virtual Environment

```bash
python3 -m venv myenv && source myenv/bin/activate  # On Windows use: myenv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install Hashcat

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
Enter keywords (comma-separated): AcmeCorp,FinanceDept
```

💡 **Tip:** Use company names, department names, and internal project names to generate highly effective password lists.

## 📜 Example Output

```
🔹 Processing keyword: AcmeCorp with rule file: best64.rule
✅ Generated 1,234 variations for AcmeCorp
  ➜ AcmeCorp!
  ➜ Acm3Corp
  ➜ Acme2024#
  ➜ Acmecorp2024...

🔹 Processing keyword: FinanceDept with rule file: toggles3.rule
✅ Generated 3,567 variations for FinanceDept
  ➜ FinanceDept
  ➜ F1nanceDept
  ➜ FinanceD3pt!
  ➜ FinanceDept#1...

Sorting 42,465,809 unique passwords...
✅ Sorted and saved to generated_passwords_2024-06-01_12-30-45.txt
```

## 🔬 Technical Details

### **Optimised for Performance**

- **Python `set` for deduplication**: Ensures only **unique** passwords are stored.
- **Sorting with tqdm**: Provides **real-time progress feedback**.
- **Batch writing**: Reduces disk I/O, improving speed.

### **Why This Beats Traditional Wordlist Generators**

❌ **Traditional wordlists**: Generic and require excessive brute force attempts.  
✅ **This tool**: Uses **targeted mutations** to create **more accurate** guesses, reducing cracking time.

### **Handling Large Datasets**

- Processes **tens of millions** of password variations efficiently.
- For extreme-scale wordlists, a system with **16GB+ RAM** is recommended.

## 🚀 Future Enhancements

- **Parallel Processing** – Multi-threading for **faster password generation**.
- **GPU Acceleration** – Offload computations for **higher speed**.
- **Custom Rule Selection** – Choose specific rule files based on attack scenarios.

## 🏆 Contributing

Want to improve this tool? Fork the repo and submit a PR! Bug reports & feature requests are welcome.

## ⚠️ Disclaimer

This tool is intended for **ethical security testing** only. Unauthorised use against systems without permission is **illegal**. The developers are **not responsible for misuse**.

---

💡 **Designed for red team professionals, optimised for password hash cracking.** Happy cracking! 🚀
