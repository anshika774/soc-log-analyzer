# 🛡️ SOC Log Analyzer
A Bash-based tool for SOC Analysts to detect brute-force attacks from auth logs.

### 🚨 Problem it Solves
SOC teams manually check logs for failed logins. This script automates it.

### ⚙️ How it Works
1. Reads `/var/log/auth.log`
2. Extracts IPs with Failed password attempts
3. Shows Top 5 attacker IPs with count

### ▶️ How to Run
```bash
chmod +x analyzer.sh
./analyzer.sh
sample output - 5 192.168.1.10
sample output - 3 10.0.0.5
skills used Linux , Bash Scripting , Log Analysis , SOC monitoring
Made by Anshika - Aspiring SOC Analyst
Linkedin: anshika2007
