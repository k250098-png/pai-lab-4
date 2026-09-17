class SecuritySystem:
    def respond(self):
        pass

class Firewall(SecuritySystem):
    def respond(self):
        print("Firewall -> Block suspicious network traffic")

class Antivirus(SecuritySystem):
    def respond(self):
        print("Antivirus -> Isolate malicious files")

class IntrusionDetectionSystem(SecuritySystem):
    def respond(self):
        print("Intrusion Detection System -> Generate security alert")

if __name__ == "__main__":
    print("--- Security System Response Test ---")
    input("Press Enter to trigger all security systems...")
    
   
    tools = [Firewall(), Antivirus(), IntrusionDetectionSystem()]
    
    for tool in tools:
        tool.respond()
        
    input("\nPress Enter to exit...")
