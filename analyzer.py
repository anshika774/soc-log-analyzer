# Phishing Email Analyzer - By Anshika
import re

def analyze_email(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    print("[+] Analyzing Email...")
    score = 0
    if "urgent" in content.lower() or "verify your account" in content.lower():
        print("[!] Suspicious Keyword Found")
        score += 1
    urls = re.findall(r'http[s]?://\S+', content)
    if urls:
        print(f"[!] Found {len(urls)} URLs: {urls}")
        score += 1
    if "spf=fail" in content.lower():
        print("[!] SPF Check Failed - Possible Spoofed Email")
        score += 2

    if score >= 2:
        print("\n🚨 RESULT: PHISHING EMAIL DETECTED")
    else:
        print("\n✅ RESULT: Looks Safe")

analyze_email("sample_email.txt")
