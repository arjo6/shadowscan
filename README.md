# ShadowScan - Network Scanner (No Scapy)

ShadowScan is a lightweight command-line tool for scanning networks and identifying connected devices without using Scapy.

## Features 🚀
✅ **Network Scanning** – Detects active devices in a given IP range.  
✅ **Device Categorization** – Identifies different types of devices:  
   - Routers & Modems  
   - Smartphones & Tablets  
   - PCs & Laptops  
   - Smart TVs  
   - Printers  
   - IoT Devices  
✅ **Save Reports** – Exports results in CSV/JSON format.  
✅ **No External Libraries Required** – Uses Python's built-in `socket` & `ping3`.  

## Installation
```bash
git clone https://github.com/YOUR_USERNAME/ShadowScan.git
cd ShadowScan
pip3 install -r requirements.txt
```

## Usage
```bash
python3 shadowscan.py 192.168.1 --csv --json
```
This scans the network and saves results to `shadowscan_report.csv` and `shadowscan_report.json`.

## Requirements
- Python 3  
- `ping3` (`pip3 install ping3`)

## License
MIT License
