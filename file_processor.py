import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import scrolledtext
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

class FileProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Processor")

        self.file_paths = []  # List to store uploaded file paths

        # Create GUI components
        self.label = tk.Label(root, text="Choose a file:")
        self.label.pack(pady=10)

        self.button_browse = tk.Button(root, text="Browse", command=self.browse_file)
        self.button_browse.pack(pady=10)

        self.button_process = tk.Button(root, text="Process Files", command=self.process_files)
        self.button_process.pack(pady=10)

        self.progressbar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progressbar.pack(pady=10)

        self.report_text = scrolledtext.ScrolledText(root, height=10, width=50)
        self.report_text.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.label.config(text=f"Selected file: {file_path}")
            self.file_paths.append(file_path)

    def process_files(self):
        if self.file_paths:
            result_window = tk.Toplevel(self.root)
            result_window.title("Processing Results")

            result_text = scrolledtext.ScrolledText(result_window, height=20, width=80)
            result_text.pack(padx=10, pady=10)

            self.report_text.delete(1.0, tk.END)  # Clear previous report

            pdf_filename = "File_Processor_Report.pdf"
            pdf_path = os.path.join(os.getcwd(), pdf_filename)

            # Create a PDF canvas
            c = canvas.Canvas(pdf_path, pagesize=letter)

            for file_path in self.file_paths:
                file_extension = file_path.split('.')[-1].lower()

                if file_extension == 'csv':
                    self.process_csv(file_path, result_text)
                    # Add entry to table of contents
                    c.drawString(50, 750 - len(self.file_paths) * 15, f"File: {os.path.basename(file_path)}")
                    c.drawString(200, 750 - len(self.file_paths) * 15, f"Page: {len(self.file_paths)}")
                    c.showPage()

            c.save()

            result_text.insert(tk.END, f"PDF report generated: {pdf_path}")

    def process_csv(self, file_path, result_text):
        try:
            df = pd.read_csv(file_path)
            report = f"CSV file processed. Summary:\n{df.describe()}\n\n"
            result_text.insert(tk.END, report)
        except Exception as e:
            result_text.insert(tk.END, f"Error processing CSV file {file_path}: {e}\n")

    def update_progress(self, value):
        self.progressbar["value"] = value
        self.root.update_idletasks()


if __name__ == "__main__":
    root = tk.Tk()
    app = FileProcessorApp(root)
    root.mainloop()
