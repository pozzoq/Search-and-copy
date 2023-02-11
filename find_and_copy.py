import tkinter as tk
from tkinter import filedialog
import os

class FileSearchGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("File Search and Copy")

        self.search_folder_label = tk.Label(self.master, text="Enter the folder to search in or browse for it:")
        self.search_folder_label.grid(row=0, column=0, padx=10, pady=10)

        self.search_folder_entry = tk.Entry(self.master)
        self.search_folder_entry.grid(row=0, column=1, padx=10, pady=10)

        self.browse_search_folder_button = tk.Button(self.master, text="Browse", command=self.browse_search_folder)
        self.browse_search_folder_button.grid(row=0, column=2, padx=10, pady=10)

        self.filename_label = tk.Label(self.master, text="Enter the filename to search for or browse for the .txt file containing the filenames:")
        self.filename_label.grid(row=1, column=0, padx=10, pady=10)

        self.filename_entry = tk.Entry(self.master)
        self.filename_entry.grid(row=1, column=1, padx=10, pady=10)

        self.browse_filename_button = tk.Button(self.master, text="Browse", command=self.browse_filename)
        self.browse_filename_button.grid(row=1, column=2, padx=10, pady=10)

        self.destination_folder_label = tk.Label(self.master, text="Enter the destination folder:")
        self.destination_folder_label.grid(row=2, column=0, padx=10, pady=10)

        self.destination_folder_entry = tk.Entry(self.master)
        self.destination_folder_entry.grid(row=2, column=1, padx=10, pady=10)

        self.browse_destination_folder_button = tk.Button(self.master, text="Browse", command=self.browse_destination_folder)
        self.browse_destination_folder_button.grid(row=2, column=2, padx=10, pady=10)

        self.search_button = tk.Button(self.master, text="Search and Copy", command=self.search_and_copy)
        self.search_button.grid(row=3, column=1, padx=10, pady=10)

    def browse_search_folder(self):
        search_folder = filedialog.askdirectory()
        self.search_folder_entry.delete(0, tk.END)
        self.search_folder_entry.insert(0, search_folder)


    def browse_filename(self):
        input_file = filedialog.askopenfilename()
        self.filename_entry.delete(0, tk.END)
        self.filename_entry.insert(0, input_file)

    def browse_destination_folder(self):
        destination_folder = filedialog.askdirectory()
        self.destination_folder_entry.delete(0, tk.END)
        self.destination_folder_entry.insert(0, destination_folder)

    def search_and_copy(self):
        input = self.filename_entry.get()
        destination_folder = self.destination_folder_entry.get()

        if os.path.isfile(input):
            with open(input) as file:
                search_names = file.read().splitlines()
        else:
            search_names = [input]

        for search_name in search_names:
            found_files = [f for f in os.listdir() if f.startswith(search_name)]
            for found_file in found_files:
                os.rename(found_file, os.path.join(destination_folder, found_file))

root = tk.Tk()
FileSearchGUI(root)
root.mainloop()
