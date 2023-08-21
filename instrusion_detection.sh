#!/bin/bash

# Log file to monitor
log_file="/var/log/auth.log"

# Threshold for triggering alerts (number of failed login attempts)
alert_threshold=5

# Email address to send alerts
alert_email="security@laelcorp.com"

# Function to send email alerts
send_alert_email() {
    local subject="Intrusion Detected on $(hostname)"
    local message="Potential intrusion detected on $(date). Please review the following log entries:"
    message+="\n$1"
    echo -e "$message" | mail -s "$subject" "$alert_email"
}

# Main script
echo "Intrusion Detection: Monitoring $log_file..."
while true; do
    # Count failed login attempts
    failed_attempts=$(grep "Failed password" "$log_file" | wc -l)
    
    if [ "$failed_attempts" -ge "$alert_threshold" ]; then
        echo "Potential intrusion detected! Failed attempts: $failed_attempts"
        log_entries=$(grep "Failed password" "$log_file" | tail -n 5)
        send_alert_email "$log_entries"
    fi
    
    sleep 300  # Check every 5 minutes
done
