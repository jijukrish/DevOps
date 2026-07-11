#!/usr/bin/env python3
"""
Network Traffic Analyzer

This script analyzes network traffic to provide insights on:
- Packet statistics
- Protocol breakdown
- Source/Destination IP analysis
- Port usage patterns
- Traffic volume monitoring
"""

import argparse
import json
import socket
import subprocess
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

try:
    from scapy.all import sniff, IP, TCP, UDP, ICMP
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False


class NetworkTrafficAnalyzer:
    """Analyzes network traffic patterns and generates reports."""

    def __init__(self, packet_limit: int = 100):
        """
        Initialize the analyzer.
        
        Args:
            packet_limit: Maximum number of packets to capture
        """
        self.packet_limit = packet_limit
        self.packets = []
        self.stats = {
            'total_packets': 0,
            'protocols': defaultdict(int),
            'src_ips': defaultdict(int),
            'dst_ips': defaultdict(int),
            'ports': defaultdict(int),
            'bytes_total': 0,
        }

    def packet_callback(self, packet) -> None:
        """
        Process each captured packet.
        
        Args:
            packet: Scapy packet object
        """
        if len(self.packets) >= self.packet_limit:
            return

        self.packets.append(packet)
        self.stats['total_packets'] += 1

        # Extract IP information
        if IP in packet:
            ip_layer = packet[IP]
            self.stats['src_ips'][ip_layer.src] += 1
            self.stats['dst_ips'][ip_layer.dst] += 1
            self.stats['bytes_total'] += len(packet)

            # Protocol analysis
            if TCP in packet:
                tcp_layer = packet[TCP]
                self.stats['protocols']['TCP'] += 1
                self.stats['ports'][tcp_layer.dport] += 1
                self.stats['ports'][tcp_layer.sport] += 1
            elif UDP in packet:
                udp_layer = packet[UDP]
                self.stats['protocols']['UDP'] += 1
                self.stats['ports'][udp_layer.dport] += 1
                self.stats['ports'][udp_layer.sport] += 1
            elif ICMP in packet:
                self.stats['protocols']['ICMP'] += 1
            else:
                self.stats['protocols']['Other'] += 1
        else:
            self.stats['protocols']['Non-IP'] += 1

    def capture_traffic(self, interface: str = None, timeout: int = 10) -> None:
        """
        Capture network traffic on specified interface.
        
        Args:
            interface: Network interface to sniff on (None for default)
            timeout: Timeout in seconds
        """
        if not SCAPY_AVAILABLE:
            print("Error: scapy is not installed. Install with: pip install scapy")
            sys.exit(1)

        print(f"Starting packet capture (limit: {self.packet_limit} packets, timeout: {timeout}s)...")
        try:
            sniff(
                iface=interface,
                prn=self.packet_callback,
                timeout=timeout,
                store=False
            )
        except PermissionError:
            print("Error: This script requires root/administrator privileges to capture packets.")
            sys.exit(1)
        except Exception as e:
            print(f"Error during packet capture: {e}")
            sys.exit(1)

    def analyze_tcpdump(self, pcap_file: str) -> None:
        """
        Analyze a pcap file using tcpdump.
        
        Args:
            pcap_file: Path to pcap file
        """
        try:
            result = subprocess.run(
                ['tcpdump', '-r', pcap_file, '-n'],
                capture_output=True,
                text=True
            )
            
            for line in result.stdout.split('\n')[1:]:  # Skip header
                if not line.strip():
                    continue
                self.stats['total_packets'] += 1
                
        except FileNotFoundError:
            print("Error: tcpdump not found. Install with: apt-get install tcpdump")
            sys.exit(1)

    def get_top_items(self, dictionary: Dict, top_n: int = 10) -> List[Tuple]:
        """Get top N items from dictionary."""
        return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[:top_n]

    def generate_report(self) -> Dict:
        """Generate analysis report."""
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_packets': self.stats['total_packets'],
                'total_bytes': self.stats['bytes_total'],
                'average_packet_size': (
                    self.stats['bytes_total'] // self.stats['total_packets']
                    if self.stats['total_packets'] > 0 else 0
                ),
            },
            'protocol_breakdown': dict(self.stats['protocols']),
            'top_source_ips': dict(self.get_top_items(self.stats['src_ips'])),
            'top_destination_ips': dict(self.get_top_items(self.stats['dst_ips'])),
            'top_ports': dict(self.get_top_items(self.stats['ports'])),
        }
        return report

    def print_report(self) -> None:
        """Print analysis report to console."""
        report = self.generate_report()
        
        print("\n" + "="*60)
        print("NETWORK TRAFFIC ANALYSIS REPORT")
        print("="*60)
        
        print(f"\nTimestamp: {report['timestamp']}")
        print(f"\nSummary:")
        print(f"  Total Packets: {report['summary']['total_packets']}")
        print(f"  Total Bytes: {report['summary']['total_bytes']:,}")
        print(f"  Avg Packet Size: {report['summary']['average_packet_size']} bytes")
        
        print(f"\nProtocol Breakdown:")
        for proto, count in report['protocol_breakdown'].items():
            percentage = (count / report['summary']['total_packets'] * 100) if report['summary']['total_packets'] > 0 else 0
            print(f"  {proto}: {count} ({percentage:.1f}%)")
        
        print(f"\nTop 10 Source IPs:")
        for ip, count in report['top_source_ips'].items():
            print(f"  {ip}: {count} packets")
        
        print(f"\nTop 10 Destination IPs:")
        for ip, count in report['top_destination_ips'].items():
            print(f"  {ip}: {count} packets")
        
        print(f"\nTop 10 Ports:")
        for port, count in report['top_ports'].items():
            print(f"  {port}: {count} packets")
        
        print("\n" + "="*60)

    def export_report(self, output_file: str) -> None:
        """Export report to JSON file."""
        report = self.generate_report()
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"Report exported to {output_file}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Network Traffic Analyzer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Capture 100 packets on default interface
  sudo python3 network_traffic_analyzer.py

  # Capture 500 packets on eth0 with 30 second timeout
  sudo python3 network_traffic_analyzer.py --interface eth0 --limit 500 --timeout 30

  # Analyze existing pcap file
  python3 network_traffic_analyzer.py --pcap traffic.pcap

  # Export report to JSON
  sudo python3 network_traffic_analyzer.py --output report.json
        '''
    )
    
    parser.add_argument(
        '--interface', '-i',
        help='Network interface to capture on',
        default=None
    )
    parser.add_argument(
        '--limit', '-l',
        type=int,
        default=100,
        help='Maximum number of packets to capture (default: 100)'
    )
    parser.add_argument(
        '--timeout', '-t',
        type=int,
        default=10,
        help='Capture timeout in seconds (default: 10)'
    )
    parser.add_argument(
        '--pcap', '-p',
        help='Analyze existing pcap file instead of live capture'
    )
    parser.add_argument(
        '--output', '-o',
        help='Export report to JSON file'
    )
    
    args = parser.parse_args()
    
    analyzer = NetworkTrafficAnalyzer(packet_limit=args.limit)
    
    if args.pcap:
        print(f"Analyzing pcap file: {args.pcap}")
        if not Path(args.pcap).exists():
            print(f"Error: File not found: {args.pcap}")
            sys.exit(1)
        analyzer.analyze_tcpdump(args.pcap)
    else:
        analyzer.capture_traffic(interface=args.interface, timeout=args.timeout)
    
    analyzer.print_report()
    
    if args.output:
        analyzer.export_report(args.output)


if __name__ == '__main__':
    main()
