#!/usr/bin/env python3

import socket
import json
import csv
import argparse
from concurrent.futures import ThreadPoolExecutor
from ping3 import ping

def scan_ip(ip):
    """Ping an IP to check if it's active."""
    response = ping(ip, timeout=1)
    if response:
        return ip
    return None

def scan_network(base_ip, start=1, end=255):
    """Scan a network range for active devices."""
    active_devices = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(scan_ip, [f"{base_ip}.{i}" for i in range(start, end + 1)])
    
    for ip in results:
        if ip:
            device_type = identify_device(ip)
            active_devices.append({"IP": ip, "Device Type": device_type})
    
    return active_devices

def identify_device(ip):
    """Basic device identification based on hostname."""
    try:
        hostname = socket.gethostbyaddr(ip)[0].lower()
        if "router" in hostname or "modem" in hostname:
            return "Router/Modem"
        elif "phone" in hostname or "mobile" in hostname:
            return "Smartphone/Tablet"
        elif "tv" in hostname:
            return "Smart TV"
        elif "printer" in hostname:
            return "Printer"
        elif "iot" in hostname or "sensor" in hostname:
            return "IoT Device"
        else:
            return "PC/Laptop"
    except socket.herror:
        return "Unknown Device"

def save_to_csv(devices, filename="shadowscan_report.csv"):
    """Save results to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["IP", "Device Type"])
        writer.writeheader()
        writer.writerows(devices)

def save_to_json(devices, filename="shadowscan_report.json"):
    """Save results to a JSON file."""
    with open(filename, "w") as file:
        json.dump(devices, file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ShadowScan - Lightweight Network Scanner")
    parser.add_argument("base_ip", help="Base IP (e.g., 192.168.1)")
    parser.add_argument("--csv", help="Save results to CSV file", action="store_true")
    parser.add_argument("--json", help="Save results to JSON file", action="store_true")
    args = parser.parse_args()

    scanned_devices = scan_network(args.base_ip)

    for device in scanned_devices:
        print(f"IP: {device['IP']}, Device Type: {device['Device Type']}")

    if args.csv:
        save_to_csv(scanned_devices)
        print("Results saved to shadowscan_report.csv")

    if args.json:
        save_to_json(scanned_devices)
        print("Results saved to shadowscan_report.json")
