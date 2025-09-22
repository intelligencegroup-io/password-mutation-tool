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

# 📑 Included Rule Files

| Rule File | Rule File |
|-----------|-----------|
| Incisive-leetspeak.rule | InsidePro-HashManager.rule |
| InsidePro-PasswordsPro.rule | KoreLogicRulesAdd1234_Everywhere.rule |
| KoreLogicRulesAdd2006Everywhere.rule | KoreLogicRulesAdd2010Everywhere.rule |
| KoreLogicRulesAddDotCom.rule | KoreLogicRulesAddJustNumbersLimit8.rule |
| KoreLogicRulesAddOnes.rule | KoreLogicRulesAddShortMonthsEverywhere.rule |
| KoreLogicRulesAppend1_AddSpecialEverywhere.rule | KoreLogicRulesAppend2Letters.rule |
| KoreLogicRulesAppend4Num.rule | KoreLogicRulesAppend6Num.rule |
| KoreLogicRulesAppend6NumbersSpecial.rule | KoreLogicRulesAppendCurrentYearSpecial.rule |
| KoreLogicRulesAppendJustNumbers.rule | KoreLogicRulesAppendMonthCurrentYear.rule |
| KoreLogicRulesAppendMonthDay.rule | KoreLogicRulesAppendNumberNumberSpecialTwice.rule |
| KoreLogicRulesAppendNumbers_or_Specials_PrependLetter.rule | KoreLogicRulesAppendSpecial4num.rule |
| KoreLogicRulesAppendSpecialNumberNumberNumber.rule | KoreLogicRulesAppendYears.rule |
| KoreLogicRulesDevProdTestUAT.rule | KoreLogicRulesL33t.rule |
| KoreLogicRulesMonthsFullPreface.rule | KoreLogicRulesPrepend2NumbersAppend2Numbers.rule |
| KoreLogicRulesPrepend4LetterMonths.rule | KoreLogicRulesPrependCAPCAPAppendSpecial.rule |
| KoreLogicRulesPrependDaysWeek.rule | KoreLogicRulesPrependHello.rule |
| KoreLogicRulesPrependJustSpecials.rule | KoreLogicRulesPrependMonthDayYear.rule |
| KoreLogicRulesPrependNumNum.rule | KoreLogicRulesPrependNumNum3LetterMonths.rule |
| KoreLogicRulesPrependNumNumNum.rule | KoreLogicRulesPrependNumNumNumNum.rule |
| KoreLogicRulesPrependNumNumSpecial.rule | KoreLogicRulesPrependRockYou50000.rule |
| KoreLogicRulesPrependSeason.rule | KoreLogicRulesPrependSpecialSpecial.rule |
| KoreLogicRulesPrependYears.rule | KoreLogicRulesReplaceLetters.rule |
| KoreLogicRulesReplaceLettersCaps.rule | KoreLogicRulesReplaceNumbers.rule |
| KoreLogicRulesReplaceNumbers2Special.rule | KoreLogicRulesReplaceSpecial2Special.rule |
| OneRuleToRuleThemStill.rule | T0XlC-insert_00-99_1950-2050_toprules_0_F.rule |
| T0XlC-insert_space_and_special_0_F.rule | T0XlC-insert_top_100_passwords_1_G.rule |
| T0XlC.rule | T0XlC_3_rule.rule |
| T0XlC_insert_HTML_entities_0_Z.rule | T0XlCv2.rule |
| _NSAKEY.v1.dive.rule | _NSAKEY.v2.dive.rule |
| append_d.rule | append_d_passthrough.rule |
| append_ds.rule | append_ds_passthrough.rule |
| append_du.rule | append_du_passthrough.rule |
| append_dus.rule | append_dus_passthrough.rule |
| append_hl.rule | append_hl_passthrough.rule |
| append_hu.rule | append_hu_passthrough.rule |
| append_l.rule | append_l_passthrough.rule |
| append_ld.rule | append_ld_passthrough.rule |
| append_lds.rule | append_lds_passthrough.rule |
| append_ldu.rule | append_ldu_passthrough.rule |
| append_ldus.rule | append_ldus_passthrough.rule |
| append_ls.rule | append_ls_passthrough.rule |
| append_lu.rule | append_lu_passthrough.rule |
| append_lus.rule | append_lus_passthrough.rule |
| append_s.rule | append_s_passthrough.rule |
| append_u.rule | append_u_passthrough.rule |
| append_us.rule | append_us_passthrough.rule |
| auto.rule | best66.rule |
| combinator.rule | d3ad0ne.rule |
| d3adhob0.rule | dive.rule |
| evil.rule | generated.rule |
| generated2-full.rule | generated2.rule |
| generated3.rule | hob064.rule |
| leetspeak.rule | new-auto.rule |
| nsa64.rule | oscommerce.rule |
| prepend_d.rule | prepend_d_passthrough.rule |
| prepend_ds.rule | prepend_ds_passthrough.rule |
| prepend_du.rule | prepend_du_passthrough.rule |
| prepend_dus.rule | prepend_dus_passthrough.rule |
| prepend_hl.rule | prepend_hl_passthrough.rule |
| prepend_hu.rule | prepend_hu_passthrough.rule |
| prepend_l.rule | prepend_l_passthrough.rule |
| prepend_ld.rule | prepend_ld_passthrough.rule |
| prepend_lds.rule | prepend_lds_passthrough.rule |
| prepend_ldu.rule | prepend_ldu_passthrough.rule |
| prepend_ldus.rule | prepend_ldus_passthrough.rule |
| prepend_ls.rule | prepend_ls_passthrough.rule |
| prepend_lu.rule | prepend_lu_passthrough.rule |
| prepend_lus.rule | prepend_lus_passthrough.rule |
| prepend_s.rule | prepend_s_passthrough.rule |
| prepend_u.rule | prepend_u_passthrough.rule |
| prepend_us.rule | prepend_us_passthrough.rule |
| rockyou-30000.rule | specific.rule |
| stacking58.rule | toggles1.rule |
| toggles2.rule | toggles3.rule |
| toggles4.rule | toggles5.rule |
| top10_2023.rule | unix-ninja-leetspeak.rule |


## 🏆 Contributing

Want to improve this tool? Fork the repo and submit a PR! Bug reports & feature requests are welcome.

## ⚠ Disclaimer

This tool is intended for **authorised security testing and research** only. Unauthorised use against systems without permission is **illegal**. The developers are **not responsible for misuse**.
