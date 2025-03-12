import os
import subprocess
import time
from datetime import datetime
from tqdm import tqdm

# ANSI Colors for terminal output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Get timestamp for sorted output file
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"generated_passwords_{timestamp}.txt"

# Ask for keywords
keywords = input(YELLOW + "Enter keywords (comma-separated): " + RESET).split(',')
keywords = [word.strip() for word in keywords if word.strip()]

# Define rules directory
rules_dir = "./rules"

# Get rule files (both .rule and .7z compressed rule files)
rule_files = [f for f in os.listdir(rules_dir) if f.endswith(".rule") or f.endswith(".rule.7z")]

if not rule_files:
    print(RED + "❌ No rule files found in the directory!" + RESET)
    exit(1)

print(GREEN + f"\n🔍 Found {len(rule_files)} rule files. Starting processing...\n" + RESET)

# Store all unique passwords in a set to avoid duplicates
master_set = set()

# Process each rule file
for rulefile in tqdm(rule_files, desc=BLUE + "Processing rule files" + RESET, unit="rule"):
    rule_path = os.path.join(rules_dir, rulefile)
    temp_rule_path = None

    # Handle compressed .7z rule files
    if rulefile.endswith(".7z"):
        temp_rule_path = os.path.join(rules_dir, rulefile.replace(".7z", ""))
        extract_cmd = f'7z e -y -o"{rules_dir}" "{rule_path}" > /dev/null 2>&1'
        os.system(extract_cmd)  # Extracts the .rule file
        rule_path = temp_rule_path  # Use the extracted rule file

    print(YELLOW + f"\n📜 Using rule file: {rulefile}\n" + RESET)

    for word in keywords:
        print(f"🔹 {BLUE}Processing keyword:{RESET} {word} {GREEN}with rule file:{RESET} {rulefile}")

        # Run Hashcat
        cmd = f'echo "{word}" | hashcat --stdout -r "{rule_path}"'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="utf-8", errors="ignore")
        output = result.stdout.strip()

        # Process results and filter out lines starting with "Cannot convert rule" or "Skipping invalid or unsupported rule"
        generated = output.split("\n")
        filtered_generated = [pwd for pwd in generated if not pwd.startswith("Cannot convert rule") and not pwd.startswith("Skipping invalid or unsupported rule")]

        if filtered_generated:
            print(f"✅ {GREEN}Generated {len(filtered_generated)} variations for {word}{RESET}")
            print("\n".join(["  ➜ " + pwd for pwd in filtered_generated[:5]]) + ("..." if len(filtered_generated) > 5 else ""))  # Show up to 5 samples

            # Add to the master set for de-duplication
            master_set.update(filtered_generated)

        time.sleep(0.1)  # Small delay for readability

    # Clean up temporary rule file if extracted
    if temp_rule_path and os.path.exists(temp_rule_path):
        os.remove(temp_rule_path)

# Sorting Progress
print(GREEN + f"\n📂 Sorting {len(master_set):,} unique passwords. This may take a while...\n" + RESET)

sorted_passwords = sorted(master_set)

# Save final unique passwords
print(GREEN + f"\n💾 Writing sorted passwords to file: {output_file}\n" + RESET)
with open(output_file, "w", encoding="utf-8") as f:
    for password in tqdm(sorted_passwords, desc=BLUE + "Saving passwords" + RESET, unit="entry"):
        f.write(password + "\n")

# Estimate final file size
estimated_size_mb = (sum(len(p) + 1 for p in sorted_passwords) / (1024 * 1024))
print(GREEN + f"\n🎉 Password generation complete! Saved {len(sorted_passwords):,} unique passwords ({estimated_size_mb:.2f} MB) in {output_file}\n" + RESET)
