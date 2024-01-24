import tkinter as tk
from tkinter import ttk
from mergeSortAnalysis import plot_execution_times

class MergeSortGUI(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("MergeSort Analysis GUI")
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Arial', 12), foreground='blue')
        self.style.configure('TEntry', font=('Arial', 12))
        self.style.configure('TCombobox', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12), foreground='white', background='blue')
        self.create_widgets()

    def create_widgets(self):
        # arr sizes
        ttk.Label(self, text="Array Sizes:").grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.array_sizes_entry = ttk.Entry(self, style='TEntry')
        self.array_sizes_entry.grid(row=0, column=1, padx=5, pady=5)

        # number of arrays to get runtimes for at each arr size
        ttk.Label(self, text="Number of Arrays:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.num_arrays_entry = ttk.Entry(self, style='TEntry')
        self.num_arrays_entry.grid(row=1, column=1, padx=5, pady=5)

        # range of the integers 0-n in the arrays, user is choosing n
        ttk.Label(self, text="Integer Range:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.integer_range_entry = ttk.Entry(self, style='TEntry')
        self.integer_range_entry.grid(row=2, column=1, padx=5, pady=5)

        # plot median  or average runtime
        ttk.Label(self, text="Plot Type:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.plot_type_combobox = ttk.Combobox(self, values=["Median", "Average"], style='TCombobox')
        self.plot_type_combobox.set("Median")
        self.plot_type_combobox.grid(row=3, column=1, padx=5, pady=5)

        # button to generate plot
        ttk.Button(self, text="Plot", command=self.plot, style='TButton').grid(row=4, column=0, columnspan=2, pady=10)

    def plot(self):
        array_sizes = [int(size) for size in self.array_sizes_entry.get().split(",")]
        num_arrays = int(self.num_arrays_entry.get())
        integer_range = int(self.integer_range_entry.get())
        plot_type = self.plot_type_combobox.get()

        plot_execution_times(array_sizes, num_arrays, integer_range, plot_type)
        
if __name__ == "__main__":
    app = MergeSortGUI()
    app.mainloop()


