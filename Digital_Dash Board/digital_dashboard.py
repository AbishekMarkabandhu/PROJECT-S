import tkinter as tk
import random
from tkinter import ttk

class DigitalDashboard(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.title("Digital Dashboard")
        self.geometry("400x300")
        self.config(bg='black')

        # Speed Label
        self.speed_label = ttk.Label(self, text="Speed: 0 km/h", font=("Arial", 18), foreground="white", background="black")
        self.speed_label.pack(pady=10)

        # Fuel Level Label
        self.fuel_label = ttk.Label(self, text="Fuel Level: 100%", font=("Arial", 18), foreground="white", background="black")
        self.fuel_label.pack(pady=10)

        # Warning Signal Label
        self.warning_label = ttk.Label(self, text="Warning: None", font=("Arial", 18), foreground="green", background="black")
        self.warning_label.pack(pady=10)

        # Update the dashboard data periodically
        self.update_dashboard()

    def update_dashboard(self):
        # Simulate Speed
        speed = random.randint(0, 240)
        self.speed_label.config(text=f"Speed: {speed} km/h")

        # Simulate Fuel Level
        fuel_level = random.randint(0, 100)
        self.fuel_label.config(text=f"Fuel Level: {fuel_level}%")

        # Simulate Warning Signals
        warning = random.choice(["None", "Check Engine", "Low Fuel", "Overheat"])
        if warning == "None":
            self.warning_label.config(text=f"Warning: {warning}", foreground="green")
        else:
            self.warning_label.config(text=f"Warning: {warning}", foreground="red")

        # Schedule the next update
        self.after(1000, self.update_dashboard)  # Update every 1 second

# Run the application
if __name__ == "__main__":
    dashboard = DigitalDashboard()
    dashboard.mainloop()
