class Computer:
    def __init__(self, cpu_usage, ram_usage, battery_level):
        self.cpu_usage = int(cpu_usage)
        self.ram_usage = int(ram_usage)
        self.battery_level = int(battery_level)

    def system_status(self):
        warnings = []
        if self.cpu_usage > 80:
            warnings.append("Heavy CPU Load")
        if self.ram_usage > 85:
            warnings.append("High Memory Usage")
        if self.battery_level < 20:
            warnings.append("Low Battery")
            
        if not warnings:
            print("System is operating normally.")
        else:
            for warning in warnings:
                print(warning)

if __name__ == "__main__":
    print("--- Computer Resource Manager ---")
    
   
    print("\n[Configure Computer 1]")
    cpu = input("Enter CPU usage %: ")
    ram = input("Enter RAM usage %: ")
    batt = input("Enter Battery level %: ")
    
    comp1 = Computer(cpu, ram, batt)
    print("Computer 1 Status:")
    comp1.system_status()
    
    
    print("\n[Computer 2 - Hardcoded Test (CPU 90%, RAM 50%, Battery 15%)]")
    comp2 = Computer(90, 50, 15)
    print("Computer 2 Status:")
    comp2.system_status()
    
    input("\nPress Enter to exit...")
