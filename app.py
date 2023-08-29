import tkinter as tk
from tkinter import messagebox, simpledialog

class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking App")

        self.account = None
        self.create_account()

    def create_account(self):
        self.clear_frame()
        self.root.geometry("300x250")
        self.root.title("Create Account")

        self.first_name_label = tk.Label(self.root, text="First Name:")
        self.first_name_label.pack()

        self.first_name_entry = tk.Entry(self.root)
        self.first_name_entry.pack()

        self.last_name_label = tk.Label(self.root, text="Last Name:")
        self.last_name_label.pack()

        self.last_name_entry = tk.Entry(self.root)
        self.last_name_entry.pack()

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.pack()

        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.create_button = tk.Button(self.root, text="Create Account", command=self.initialize_account)
        self.create_button.pack()

    def initialize_account(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if first_name and last_name and email and password:
            self.account = Account(first_name, last_name, email, password)
            self.account.activate()
            self.show_menu()
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")

    def show_menu(self):
        self.clear_frame()
        self.root.geometry("300x200")
        self.root.title("Banking Menu")

        self.deposit_button = tk.Button(self.root, text="Deposit Cash", command=self.deposit)
        self.deposit_button.pack()

        self.withdraw_button = tk.Button(self.root, text="Withdraw Cash", command=self.withdraw)
        self.withdraw_button.pack()

        self.balance_button = tk.Button(self.root, text="View Balance", command=self.view_balance)
        self.balance_button.pack()

        self.profile_button = tk.Button(self.root, text="View Profile", command=self.view_profile)
        self.profile_button.pack()

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack()

    def deposit(self):
        amount = simpledialog.askinteger("Deposit", "Enter deposit amount:")
        if amount:
            if self.account.deposit(amount):
                messagebox.showinfo("Success", f"Successfully deposited {amount}.")

    def withdraw(self):
        amount = simpledialog.askinteger("Withdraw", "Enter withdrawal amount:")
        if amount:
            message = self.account.withdraw(amount)
            if message:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showwarning("Warning", "Insufficient balance.")

    def view_balance(self):
        if self.account:
            messagebox.showinfo("Balance", f"Your balance is {self.account.balance}")
        else:
            messagebox.showwarning("Warning", "Please create an account first.")

    def view_profile(self):
        if self.account:
            profile_info = f"Name: {self.account.first_name} {self.account.last_name}\nEmail: {self.account.email}"
            messagebox.showinfo("Profile", profile_info)
        else:
            messagebox.showwarning("Warning", "Please create an account first.")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


class Account:
    def __init__(self, first_name, last_name, email, password, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.balance = balance
        self.activated = False

    def activate(self):
        self.activated = True

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return f"Withdrawn {amount} from your account."
        return None


if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
