import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter import messagebox as mb
from datetime import datetime

import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class App:

    selected: bool = False
    file = False

    def __init__(self, root):
        self.root = root
        self.root.geometry("275x230")
        self.root.resizable(False, False)
        self.root.title("Staubdaten")

        self.selected_value = tk.StringVar()
        self.selected_value.set("Bitte wählen...")

        self.dropdown_label = tk.Label(root, text="Werttyp auswählen:")
        self.dropdown_label.place(x=5, y=20, height=20)

        self.dropdown_menu = ttk.Combobox(root, values=["Bitte wählen...", "P1", "P2"], state="readonly",
                                          textvariable=self.selected_value)
        self.dropdown_menu.place(x=120, y=20, width=150, height=20)
        self.dropdown_menu.bind("<<ComboboxSelected>>", self.on_dropdown_select)

        self.separator = ttk.Separator(root, orient="horizontal")
        self.separator.place(x=00, y=60, width=275, height=10)

        self.help_icon = tk.PhotoImage(file="help_icon.png")
        self.help_label = tk.Label(root, image=self.help_icon)
        self.help_label.place(x=5, y=65, width=20, height=20)
        self.help_label.bind("<Enter>", self.show_help_message)
        self.help_label.bind("<Leave>", self.hide_help_message)

        self.help_text = tk.StringVar()
        self.help_text.set("")
        self.help_message_label = tk.Label(root, textvariable=self.help_text)
        self.help_message_label.place(x=25, y=65, height=20)

        self.start_date_label = tk.Label(root, text="Startdatum:")
        self.start_date_label.place(x=5, y=90, height=20)

        self.start_date_picker = tk.Entry(root)
        self.start_date_picker.place(x=120, y=90, width=150, height=20)

        self.end_date_label = tk.Label(root, text="Enddatum:")
        self.end_date_label.place(x=5, y=130, height=20)

        self.end_date_picker = tk.Entry(root)
        self.end_date_picker.place(x=120, y=130, width=150, height=20)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.place(x=2.5, y=180, width=270, height=30)

    def on_dropdown_select(self, event):
        if self.selected_value.get() != "Bitte wählen...":
            self.selected = True
        else:
            self.selected = False



    def submit(self):
        try:
            if self.selected:
                start_date = datetime.strptime(self.start_date_picker.get(), "%d.%m.%Y")
                end_date = datetime.strptime(self.end_date_picker.get(), "%d.%m.%Y")

                if start_date.year != 2022 or end_date.year != 2022:
                    mb.showerror("Falsches Jahr", "Bitte gebe ein Datum aus dem Jahr 2022 ein.")
                elif end_date < start_date:
                    mb.showerror("Falsche Daten.", "Das Enddatum muss nach dem Startdatum liegen.")
                else:
                    # Create a new window for the plot
                    x = np.linspace(0, 10, 100)
                    y = np.sin(x)

                    # Create a new window to display the plot
                    plot_window = tk.Toplevel(self.root)
                    plot_window.title("Plot")
                    plot_window.geometry("650x500")
                    plot_window.resizable(False, False)
                    close_button = tk.Button(plot_window, text="Schließen", command=plot_window.destroy)
                    close_button.place(x=35, y=0)
                    # Add "Save" and "Close" buttons
                    save_button = tk.Button(plot_window, text="Save", command=lambda: self.save_plot())
                    save_button.place(x=0, y=0)
                    # Create the plot
                    fig, ax = plt.subplots()
                    ax.plot(x, y)
                    ax.set_xlabel("X")
                    ax.set_ylabel(f"{self.selected_value}")
                    ax.set_title(f"{str(start_date).split(' ')[0]} - {str(end_date).split(' ')[0]}")
                    # Embed the plot in a Tkinter canvas
                    canvas = FigureCanvasTkAgg(fig, master=plot_window)
                    canvas.draw()
                    canvas.get_tk_widget().place(x=0, y=20)
            else:
                mb.showerror("Falscher Werttyp", "Du musst den Auszuwertenden Werttyp auswählen!")
        except ValueError:
            mb.showerror("Invalid Date", "Please enter a valid date in the format DD.MM.YYYY")

    def save_plot(self):
        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Picture", ".png .jpg .jpeg .svg")])
        # Save the plot to the selected file path
        if path:
            plt.savefig(path)


    def show_help_message(self, event):
        self.help_text.set("Benutze das Datumsformat DD.MM.YYYY")

    def hide_help_message(self, event):
        self.help_text.set("")


root = tk.Tk()
app = App(root)
root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

root.mainloop()

