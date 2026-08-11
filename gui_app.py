
import tkinter as tk
from tkinter import ttk
import requests
import json
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class EnvoyGatewayStudio:
    def __init__(self, root):
        self.root = root
        self.root.title('Envoy Gateway Studio')
        self.root.configure(bg='#2b2b2b')

        # Header frame
        self.header_frame = tk.Frame(self.root, bg='#2b2b2b')
        self.header_frame.pack(fill='x')
        self.title_icon = tk.Label(self.header_frame, text='Envoy Gateway Studio', bg='#2b2b2b', fg='white', font=('Arial', 16))
        self.title_icon.pack(side='left')
        self.subtitle = tk.Label(self.header_frame, text='Visual Service Mesh & Route Config GUI', bg='#2b2b2b', fg='grey', font=('Arial', 12))
        self.subtitle.pack(side='left', padx=10)

        # Input controls frame
        self.input_frame = tk.Frame(self.root, bg='#2b2b2b')
        self.input_frame.pack(fill='x', padx=10, pady=10)
        self.service_name_label = tk.Label(self.input_frame, text='Service Name:', bg='#2b2b2b', fg='white', font=('Arial', 12))
        self.service_name_label.pack(side='left')
        self.service_name_entry = tk.Entry(self.input_frame, width=30, font=('Arial', 12))
        self.service_name_entry.pack(side='left', padx=10)
        self.optimize_button = tk.Button(self.input_frame, text='Optimize Route', command=self.optimize_route, bg='#4CAF50', fg='white', font=('Arial', 12))
        self.optimize_button.pack(side='left', padx=10)

        # Visualization display frame
        self.display_frame = tk.Frame(self.root, bg='#2b2b2b')
        self.display_frame.pack(fill='both', expand=True, padx=10, pady=10)
        self.tree = ttk.Treeview(self.display_frame)
        self.tree['columns'] = ('Service', 'Latency', 'Circuit Breaker')
        self.tree.column('#0', width=0, stretch='no')
        self.tree.column('Service', anchor='w', width=200)
        self.tree.column('Latency', anchor='w', width=100)
        self.tree.column('Circuit Breaker', anchor='w', width=100)
        self.tree.heading('#0', text='', anchor='w')
        self.tree.heading('Service', text='Service', anchor='w')
        self.tree.heading('Latency', text='Latency', anchor='w')
        self.tree.heading('Circuit Breaker', text='Circuit Breaker', anchor='w')
        self.tree.pack(fill='both', expand=True)

        # Status message frame
        self.status_frame = tk.Frame(self.root, bg='#2b2b2b')
        self.status_frame.pack(fill='x', padx=10, pady=10)
        self.status_message = tk.Label(self.status_frame, text='', bg='#2b2b2b', fg='white', font=('Arial', 12))
        self.status_message.pack(side='left')

    def optimize_route(self):
        service_name = self.service_name_entry.get()
        if service_name:
            try:
                response = requests.get(f'https://example.com/optimize/{service_name}')
                if response.status_code == 200:
                    data = json.loads(response.text)
                    self.tree.delete(*self.tree.get_children())
                    for service in data['services']:
                        self.tree.insert('', 'end', values=(service['name'], service['latency'], service['circuit_breaker']))
                    self.status_message['text'] = 'Route optimized successfully'
                else:
                    self.status_message['text'] = 'Error optimizing route'
            except requests.exceptions.RequestException as e:
                self.status_message['text'] = 'Error connecting to server'
        else:
            self.status_message['text'] = 'Please enter a service name'

if __name__ == '__main__':
    root = tk.Tk()
    app = EnvoyGatewayStudio(root)
    root.mainloop()
