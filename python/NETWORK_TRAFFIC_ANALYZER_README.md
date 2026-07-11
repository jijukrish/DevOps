# Network Traffic Analyzer

A comprehensive Python tool for analyzing network traffic patterns, protocol breakdowns, and network performance metrics. This script provides real-time packet capture analysis or can process existing pcap files.

## Features

- **Live Packet Capture**: Capture and analyze network traffic in real-time
- **Protocol Analysis**: Breakdown of TCP, UDP, ICMP, and other protocols
- **IP Analysis**: Track source and destination IPs with packet counts
- **Port Usage**: Monitor which ports are receiving the most traffic
- **Traffic Volume**: Measure total bytes and average packet size
- **Multiple Input Modes**: Live capture or pcap file analysis
- **JSON Export**: Export detailed reports for further analysis
- **Detailed Reporting**: Console output and file export capabilities

## Requirements

- Python 3.7+
- Root/Administrator privileges (for live packet capture)
- Dependencies:
  - `scapy` - For packet sniffing and analysis
  - `tcpdump` - For pcap file analysis (optional)

## Installation

### Install Dependencies

```bash
# Install Python dependencies
pip install scapy

# Install tcpdump (for pcap file analysis)
# On Ubuntu/Debian
sudo apt-get install tcpdump

# On macOS (with Homebrew)
brew install tcpdump
```

## Usage

### Basic Live Capture

Capture 100 packets on the default network interface:

```bash
sudo python3 network_traffic_analyzer.py
```

### Advanced Capture Options

Capture packets with custom parameters:

```bash
# Capture 500 packets on eth0 with 30-second timeout
sudo python3 network_traffic_analyzer.py --interface eth0 --limit 500 --timeout 30

# Capture on a specific interface (e.g., wlan0)
sudo python3 network_traffic_analyzer.py -i wlan0 -l 1000 -t 60
```

### Analyze Existing PCAP File

Analyze a previously captured pcap file (no root required):

```bash
python3 network_traffic_analyzer.py --pcap traffic.pcap

# With output export
python3 network_traffic_analyzer.py --pcap traffic.pcap --output report.json
```

### Export Report to JSON

Save detailed analysis results to a JSON file:

```bash
sudo python3 network_traffic_analyzer.py --output report.json

# Or combine capture and export
sudo python3 network_traffic_analyzer.py -i eth0 -l 500 -o analysis_report.json
```

## Command-Line Arguments

| Argument | Short | Type | Default | Description |
|----------|-------|------|---------|-------------|
| `--interface` | `-i` | string | None | Network interface to capture on (default: system default) |
| `--limit` | `-l` | integer | 100 | Maximum number of packets to capture |
| `--timeout` | `-t` | integer | 10 | Capture timeout in seconds |
| `--pcap` | `-p` | string | None | Analyze existing pcap file instead of live capture |
| `--output` | `-o` | string | None | Export report to JSON file |

## Output

### Console Report

The script displays a formatted report with:

```
============================================================
NETWORK TRAFFIC ANALYSIS REPORT
============================================================

Timestamp: 2024-01-15T10:30:45.123456

Summary:
  Total Packets: 100
  Total Bytes: 45,230
  Avg Packet Size: 452 bytes

Protocol Breakdown:
  TCP: 65 (65.0%)
  UDP: 30 (30.0%)
  ICMP: 5 (5.0%)

Top 10 Source IPs:
  192.168.1.100: 45 packets
  10.0.0.50: 30 packets
  ...

Top 10 Destination IPs:
  8.8.8.8: 40 packets
  1.1.1.1: 35 packets
  ...

Top 10 Ports:
  443: 50 packets
  80: 35 packets
  ...

============================================================
```

### JSON Export

When using `--output`, a detailed JSON report is created:

```json
{
  "timestamp": "2024-01-15T10:30:45.123456",
  "summary": {
    "total_packets": 100,
    "total_bytes": 45230,
    "average_packet_size": 452
  },
  "protocol_breakdown": {
    "TCP": 65,
    "UDP": 30,
    "ICMP": 5
  },
  "top_source_ips": {
    "192.168.1.100": 45,
    "10.0.0.50": 30
  },
  "top_destination_ips": {
    "8.8.8.8": 40,
    "1.1.1.1": 35
  },
  "top_ports": {
    "443": 50,
    "80": 35
  }
}
```

## Examples

### Monitor Local Network Traffic

```bash
# Capture on default interface for 60 seconds, max 1000 packets
sudo python3 network_traffic_analyzer.py --timeout 60 --limit 1000
```

### Analyze Specific Network Interface

```bash
# Monitor WiFi interface
sudo python3 network_traffic_analyzer.py --interface wlan0 --limit 500
```

### Detailed Analysis and Export

```bash
# Capture 5000 packets and export to JSON for analysis
sudo python3 network_traffic_analyzer.py \
  --interface eth0 \
  --limit 5000 \
  --timeout 120 \
  --output network_analysis.json
```

### Post-Capture Analysis

```bash
# Analyze previously captured traffic
python3 network_traffic_analyzer.py --pcap capture.pcap --output results.json
```

## Network Interfaces

To list available network interfaces on your system:

```bash
# Linux
ip link show

# macOS
ifconfig

# Windows
ipconfig
```

## Troubleshooting

### Permission Denied Error

**Error**: `Error: This script requires root/administrator privileges to capture packets.`

**Solution**: Use `sudo` to run the script with elevated privileges:

```bash
sudo python3 network_traffic_analyzer.py
```

### Scapy Not Found

**Error**: `Error: scapy is not installed. Install with: pip install scapy`

**Solution**: Install the scapy library:

```bash
pip install scapy
```

### TCPdump Not Found

**Error**: `Error: tcpdump not found. Install with: apt-get install tcpdump`

**Solution**: Install tcpdump (only needed for pcap file analysis):

```bash
# Ubuntu/Debian
sudo apt-get install tcpdump

# macOS
brew install tcpdump
```

### Interface Not Found

**Error**: `Error: No such device exists` or similar

**Solution**: Verify the interface name and ensure it exists:

```bash
# List interfaces and use the correct name
ip link show
```

## Performance Considerations

- **Packet Limit**: Default is 100 packets. Increase `--limit` for longer analysis periods
- **Timeout**: Default is 10 seconds. Increase for capturing more traffic
- **Memory**: Large packet limits may consume significant memory; adjust based on available resources
- **CPU Impact**: Live packet capture is CPU-intensive; consider running on a dedicated monitoring system

## Limitations

- Live capture requires root/administrator privileges
- Packet analysis is limited to the captured sample size
- Very high-traffic networks may exceed packet loss with default settings
- Encrypted traffic (HTTPS) cannot be analyzed at the protocol level

## Use Cases

- **Network Troubleshooting**: Identify traffic anomalies and bottlenecks
- **Security Monitoring**: Detect suspicious traffic patterns
- **Performance Analysis**: Understand protocol distribution and port usage
- **Bandwidth Management**: Identify heavy traffic sources and destinations
- **Educational Purpose**: Learn network traffic patterns and analysis techniques

## License

This script is part of the DevOps repository.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
