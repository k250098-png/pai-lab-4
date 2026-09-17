class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def charge(self, amount):
        self.battery += amount
        print(f"{self.name} charged. Battery is now {self.battery}%.")

    def move(self):
        if self.battery < 20:
            print(f"{self.name} cannot move: Battery level ({self.battery}%) is below 20%.")
            return False
        return True

class DeliveryRobot(Robot):
    def move(self):
        if super().move():
            print(f"{self.name} moves to a delivery location.")

class SecurityRobot(Robot):
    def move(self):
        if super().move():
            print(f"{self.name} patrols a specific area.")

class RescueRobot(Robot):
    def move(self):
        if super().move():
            print(f"{self.name} moves toward a disaster location.")

if __name__ == "__main__":
    print("--- Robot Control System ---")
    battery_level = int(input("Set the initial battery level for all robots (0-100): "))
    
    delivery_bot = DeliveryRobot("DeliveryBot-1", battery_level)
    security_bot = SecurityRobot("SecBot-1", battery_level)
    rescue_bot = RescueRobot("RescueBot-1", battery_level)
    
    print("\nIssuing move commands...")
    delivery_bot.move()
    security_bot.move()
    rescue_bot.move()
    
    input("\nPress Enter to exit...")
