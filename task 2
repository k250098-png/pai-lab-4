class PasswordVault:
    def __init__(self, username, vault_status, password):
        self.username = username             
        self._vault_status = vault_status    
        self.__password = password           

    def change_password(self, old_password, new_password):
        if self.verify_password(old_password, silent=True):
            self.__password = new_password
            print("Password successfully updated.")
        else:
            print("Cannot change password: Old password incorrect.")

    def verify_password(self, entered_password, silent=False):
        if self.__password == entered_password:
            if not silent:
                print("Access Granted")
            return True
        else:
            if not silent:
                print("Access Denied")
            return False

    def display_status(self):
        print(f"User: {self.username} | Vault Status: {self._vault_status}")

if __name__ == "__main__":
    print("--- Secure Password Vault ---")
    vault = PasswordVault("AdminUser", "Active", "secret123")
    vault.display_status()
    
    print("\n[Verification Test]")
    guess = input("Enter password to access vault: ")
    vault.verify_password(guess)
    
    print("\n[Change Password Test]")
    old_pwd = input("Enter current password: ")
    new_pwd = input("Enter new password: ")
    vault.change_password(old_pwd, new_pwd)
    
    input("\nPress Enter to exit...")
