import tkinter as tk
import json
from datetime import datetime

# Initialize the call dictionary with initial counts
call_groups = {
    "No answer": 0,
    "Contact": 0,
    "Same Day": 0,
    "Next Day": 0,
    "Call back": 0,
    "Seen": 0,
    "Sold": 0
}

# Function to update count for a group
def update_count(group, value):
    call_groups[group] += value
    update_display()

# Function to clear all numbers
def clear_all():
    for group in call_groups:
        call_groups[group] = 0
    update_display()

# Function to save data to a plain text file
def save_data():
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"call_data_{current_time}.txt"
    with open(filename, "w") as file:
        for group, count in call_groups.items():
            file.write(f"{group}: {count}\n")
    print(f"Data saved successfully to {filename}!")


# Function to update the display with current counts
def update_display():
    for group, count in call_groups.items():
        label_text = f"{group}: {count}"
        label_dict[group].config(text=label_text)

# Create the main window
root = tk.Tk()
root.title("Phone Call Tracker")
root.configure(bg="lightgray")  # Set the background color of the window

# Dictionary to store labels and buttons for each call group
label_dict = {}
button_dict = {}

# Create labels and buttons for each call group and add them to the window
for group in call_groups:
    label_frame = tk.Frame(root, bg="lightgray")  # Set the background color of the frame
    label_frame.pack(side=tk.TOP, padx=10, pady=10)
    
    label = tk.Label(label_frame, text=f"{group}: {call_groups[group]}", font=("Arial", 12), bg="lightgray", fg="black")
    label.pack(side=tk.LEFT)
    label_dict[group] = label

    increase_button = tk.Button(label_frame, text="+", command=lambda grp=group: update_count(grp, 1), font=("Arial", 12), bg="green", fg="white")
    decrease_button = tk.Button(label_frame, text="-", command=lambda grp=group: update_count(grp, -1), font=("Arial", 12), bg="red", fg="white")
    increase_button.pack(side=tk.LEFT, padx=5)
    decrease_button.pack(side=tk.LEFT)
    
    button_dict[group] = (increase_button, decrease_button)

# Add a button to clear all numbers
clear_button = tk.Button(root, text="Clear All", command=clear_all, font=("Arial", 12), bg="blue", fg="white")
clear_button.pack(pady=10)

# Add a button to save data
save_button = tk.Button(root, text="Save", command=save_data, font=("Arial", 12), bg="orange", fg="white")
save_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
