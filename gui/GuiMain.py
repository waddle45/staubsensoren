import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

root = tk.Tk()

# Create a dropdown menu
options = ["Bitte wählen...", "P1", "P2"]
selected_option = tk.StringVar(value=options[0])
dropdown = ttk.Combobox(root, textvariable=selected_option, values=options)
dropdown.pack()

# Create two date picker widgets
start_date_label = tk.Label(root, text="Start Date:")
start_date_label.pack()
start_date = DateEntry(root, year=2022)
start_date.pack()

end_date_label = tk.Label(root, text="End Date:")
end_date_label.pack()
end_date = DateEntry(root, year=2022)
end_date.pack()

# Constrain the end date to be after the start date
def validate_end_date(event):
    if end_date.get_date() < start_date.get_date():
        end_date.set_date(start_date.get_date())

start_date.bind("<<DateEntrySelected>>", validate_end_date)

root.mainloop()
