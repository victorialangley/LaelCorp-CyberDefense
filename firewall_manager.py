#!/usr/bin/env python3

import requests

# List of trusted IP addresses
trusted_ips = ["192.168.1.1", "10.0.0.2"]

# API endpoint for threat intelligence feed
threat_feed_url = "https://threat-intel-api.example.com/feed"

def fetch_threat_ips():
    try:
        response = requests.get(threat_feed_url)
        threat_ips = response.json()
        return threat_ips
    except requests.exceptions.RequestException as e:
        print("Error fetching threat intelligence feed:", e)
        return []

def update_firewall_rules(threat_ips):
    new_rules = [ip for ip in threat_ips if ip not in trusted_ips]

    if new_rules:
        print("Updating firewall rules:")
        for ip in new_rules:
            print(f"Blocking {ip}")
            # Add code here to update firewall rules and block the IP

def main():
    print("Firewall Manager: Fetching threat intelligence feed...")
    threat_ips = fetch_threat_ips()
    
    if threat_ips:
        print("Fetched", len(threat_ips), "threat IPs.")
        update_firewall_rules(threat_ips)
    else:
        print("No threat IPs found in the feed.")

if __name__ == "__main__":
    main()
