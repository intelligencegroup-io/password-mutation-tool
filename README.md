# 🔐 Targeted Password List Generator

## Overview

This tool is designed for **red teamers, penetration testers, and security researchers** who need to generate **highly targeted password lists**. By leveraging **rule files**, the tool applies advanced transformations to user-provided keywords, creating **realistic password variations** that align with an organisation's naming patterns, culture, and tendencies.

## 🎯 Use Case: Targeted Wordlist Generation in Security Engagements

Instead of relying on generic wordlists, professionals can generate tailored variations based on company names, departments, projects, or cultural references. This produces **high-probability guesses** aligned with the target organisation’s environment.

### **Example Scenario**

A penetration tester is assessing an organisation named **"AcmeCorp"**. Instead of using a broad wordlist, they can generate customised variations:

```bash
Enter keywords (comma-separated): AcmeCorp
```

The tool applies **real-world transformations**, generating:

```
AcmeCorp!
Acm3Corp
Acme2024#
Acmecorp2024
AcmeC0rp!
```

This approach provides a **focused and context-aware list**, avoiding wasted effort on irrelevant guesses.

## 📌 Features

✅ **Supports Compressed Rule Files** – Automatically extracts and processes `.7z` compressed rule sets  
✅ **Highly Targeted Wordlist Generation** – Uses organisation-specific keywords for **precise variations**  
✅ **Optimised Mutations** – Prioritises **realistic, high-probability patterns** over generic brute-force lists  
✅ **Real-Time Processing** – Runs entirely in **RAM** for maximum speed  
✅ **Automatic Deduplication** – Ensures a clean, unique output  
✅ **Supports Any Rule Files** – Works with **custom or pre-existing** `.rule` files  
✅ **Efficient Large-Scale Processing** – Handles **millions of variations** efficiently  

## 🛠 Installation & Setup

### 1⃣ Clone the Repository

```bash
git clone https://github.com/intelligencegroup-io/password-mutation-tool.git
cd password-mutation-tool
```

### 2⃣ Set Up a Virtual Environment

```bash
python3 -m venv myenv && source myenv/bin/activate  # On Windows use: myenv\Scripts\activate
```

### 3⃣ Install Dependencies

```bash
pip install -r requirements.txt
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

💡 **Tip:** Use company names, department names, and project names to generate highly effective lists.

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

Sorting 42,465,809 unique entries...
✅ Sorted and saved to generated_passwords_2024-06-01_12-30-45.txt
```

## 🔬 Technical Details

### **Optimised for Performance**

- **Python `set` for deduplication**: Guarantees only **unique** values  
- **Sorting with tqdm**: Provides **real-time progress feedback**  
- **Batch writing**: Reduces disk I/O, improving speed  

### **Why This Beats Traditional Wordlist Generators**

❌ **Traditional lists**: Generic and bloated with irrelevant entries  
✅ **This tool**: Produces **targeted, realistic variations**, tuned to the engagement  

### **Handling Large Datasets**

- Efficiently processes **tens of millions** of variations  
- For very large lists, **16GB+ RAM** is recommended  

## 🚀 Future Enhancements

- **Parallel Processing** – Multi-threading for faster generation  
- **GPU Acceleration** – Offload transformations for higher throughput  
- **Custom Rule Selection** – Choose specific rule files for more control  

## 🏆 Contributing

Want to improve this tool? Fork the repo and submit a PR! Bug reports & feature requests are welcome.

## ⚠ Disclaimer

This tool is intended for **authorised security testing and research** only. Unauthorised use against systems without permission is **illegal**. The developers are **not responsible for misuse**.
