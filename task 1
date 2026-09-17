class ThreatDetector:
    def __init__(self, device_name, ip_address, threat_level):
        self.device_name = device_name
        self.ip_address = ip_address
        self.threat_level = threat_level

    def scan(self):
        level = self.threat_level.lower()
        if level == "low":
            print(f"[{self.device_name} - {self.ip_address}]: System Safe")
        elif level == "medium":
            print(f"[{self.device_name} - {self.ip_address}]: Suspicious Activity")
        elif level == "high":
            print(f"[{self.device_name} - {self.ip_address}]: Critical Threat Detected")
        else:
            print(f"[{self.device_name} - {self.ip_address}]: Unknown Threat Level")

if __name__ == "__main__":
    print("--- Threat Detector ---")
    name = input("Enter device name (e.g., PC-1): ")
    ip = input("Enter IP address: ")
    threat = input("Enter threat level (Low/Medium/High): ")
    
    device = ThreatDetector(name, ip, threat)
    print("\nScanning Device...")
    device.scan()
    input("\nPress Enter to exit...")
