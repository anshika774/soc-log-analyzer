#!/bin/bash
# SOC Log Analyzer - Detects brute-force attacks
# Author: Anshika | Aspiring SOC Analyst

LOG_FILE="/var/log/auth.log"
echo "--- SOC Failed Login Report ---"
echo "Analyzing: $LOG_FILE"
echo ""

# Top 5 Attacker IPs
grep "Failed password" $LOG_FILE 2>/dev/null | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | head -5

echo ""
echo "Report generated for SOC monitoring"
