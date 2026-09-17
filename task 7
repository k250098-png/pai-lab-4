class CyberAgent:
    def __init__(self, name, status, threat_score):
        self.name = name
        self.status = status
        self.__threat_score = threat_score  

    def get_threat_score(self):
        return self.__threat_score

    def set_threat_score(self, new_score):
        if new_score >= 0:
            self.__threat_score = new_score
            print(f"Threat score updated to {new_score}")
        else:
            print("Threat score cannot be negative.")

    def analyze(self):
        pass

    def respond(self):
        pass

class NetworkAgent(CyberAgent):
    def analyze(self):
        print(f"{self.name} analyzes network traffic for unusual data packets.")
    def respond(self):
        print(f"{self.name} response: Blocking compromised IP addresses.")

class MalwareAgent(CyberAgent):
    def analyze(self):
        print(f"{self.name} analyzes file signatures to detect malicious code.")
    def respond(self):
        print(f"{self.name} response: Quarantining infected files.")

class IncidentResponseAgent(CyberAgent):
    def analyze(self):
        print(f"{self.name} analyzes system-wide logs for unauthorized access.")
    def respond(self):
        print(f"{self.name} response: Initiating system lockdown protocols.")

if __name__ == "__main__":
    print("--- Autonomous Cyber Defense System ---")
    
    net_agent = NetworkAgent("NetGuard", "Active", 25)
    mal_agent = MalwareAgent("MalwareSweeper", "Active", 80)
    
    print(f"\n[{net_agent.name}] Current Threat Score: {net_agent.get_threat_score()}")
    net_agent.analyze()
    net_agent.respond()
    
    print(f"\n[{mal_agent.name}] Current Threat Score: {mal_agent.get_threat_score()}")
    mal_agent.analyze()
    mal_agent.respond()
    
    print("\n[Testing Private Threat Score Update]")
    new_score = int(input(f"Enter new threat score for {net_agent.name}: "))
    net_agent.set_threat_score(new_score)
    print(f"Verified new score: {net_agent.get_threat_score()}")
    
    input("\nPress Enter to exit...")
