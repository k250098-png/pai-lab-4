class Agent:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def perform_task(self):
        pass

class SecurityAgent(Agent):
    def perform_task(self):
        print(f"Security Agent '{self.name}': Detecting cyber threat")

class MonitoringAgent(Agent):
    def perform_task(self):
        print(f"Monitoring Agent '{self.name}': Monitoring system activity")

class RecoveryAgent(Agent):
    def perform_task(self):
        print(f"Recovery Agent '{self.name}': Recovering system services")

if __name__ == "__main__":
    print("--- AI Agent System ---")
    input("Press Enter to deploy all agents...")
    
    agents = [
        SecurityAgent("Alpha", "Active"),
        MonitoringAgent("Beta", "Active"),
        RecoveryAgent("Gamma", "Standby")
    ]
    
    for agent in agents:
        agent.perform_task()
        
    input("\nPress Enter to exit...")
