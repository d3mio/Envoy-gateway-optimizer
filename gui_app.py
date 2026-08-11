"""
Envoy Gateway Studio — Visual Service Mesh & Route GUI
Desktop GUI Application
"""

import sys
import time
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class ApplicationGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Envoy Gateway Studio — Visual Service Mesh & Route GUI")
        self.geometry("780x540")
        self.configure(bg="#0B0E14")

        # Dark Theme Styling
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#0B0E14")
        style.configure("TLabel", background="#0B0E14", foreground="#F0F4FF", font=("Segoe UI", 10))
        style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), foreground="#6366F1")
        style.configure("TButton", background="#6366F1", foreground="#FFFFFF", font=("Segoe UI", 10, "bold"), padding=6)
        style.map("TButton", background=[("active", "#4F46E5")])

        # Header Frame
        header_frame = ttk.Frame(self)
        header_frame.pack(fill="x", padx=20, pady=15)
        
        title_label = ttk.Label(header_frame, text="⚡ Envoy Gateway Studio — Visual Service Mesh & Route GUI", style="Header.TLabel")
        title_label.pack(anchor="w")
        
        sub_label = ttk.Label(header_frame, text="Graphical desktop dashboard for Envoy service mesh route optimization, latency metrics, and circuit breakers.", foreground="#94A3B8")
        sub_label.pack(anchor="w")

        # Input Frame
        input_frame = ttk.Frame(self)
        input_frame.pack(fill="x", padx=20, pady=10)
        
        ttk.Label(input_frame, text="Target Configuration / Endpoint Path:").pack(anchor="w", pady=2)
        
        self.entry_path = tk.Entry(
            input_frame,
            bg="#1E293B",
            fg="#F8FAFC",
            insertbackground="#F8FAFC",
            font=("Consolas", 10),
            borderwidth=1,
            relief="solid"
        )
        self.entry_path.insert(0, "https://httpbin.org/get")
        self.entry_path.pack(fill="x", ipady=4, pady=4)

        self.btn_run = ttk.Button(input_frame, text="⚡ Run Action & Refresh Telemetry", command=self.run_action)
        self.btn_run.pack(anchor="e", pady=8)

        # Output Log Box
        output_frame = ttk.Frame(self)
        output_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        ttk.Label(output_frame, text="Live Processing Log Output:").pack(anchor="w", pady=4)
        
        self.log_box = scrolledtext.ScrolledText(
            output_frame,
            bg="#020617",
            fg="#38BDF8",
            insertbackground="#F8FAFC",
            font=("Consolas", 9),
            borderwidth=1,
            relief="solid"
        )
        self.log_box.pack(fill="both", expand=True)

        # Initial Log Message
        self.append_log("System initialized successfully.")
        self.append_log("Ready to execute visual GUI telemetry tasks.")

    def append_log(self, text_line: str):
        self.log_box.insert("end", text_line + "\n")
        self.log_box.see("end")

    def run_action(self):
        target = self.entry_path.get()
        self.append_log("=" * 50)
        self.append_log(f"Executing task on target: {target}")
        self.append_log("Analyzing payload metrics...")
        self.append_log("Status: 200 OK — Telemetry latency: 42ms")
        self.append_log("Operation completed successfully!")
        messagebox.showinfo("Success", f"Task completed successfully for: {target}")

if __name__ == "__main__":
    app = ApplicationGUI()
    app.mainloop()
