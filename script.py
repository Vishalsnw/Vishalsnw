```python
import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        self.total_expression = ""
        self.current_expression = ""
        
        self.display_font = font.Font(size=20)
        
        self.total_label = tk.Label(self.root, text=self.total_expression, anchor=tk.E, padx=20, font=self.display_font)
        self.total_label.pack(fill=tk.X)
        
        self.current_label = tk.Label(self.root, text=self.current_expression, anchor=tk.E, padx=20, font=self.display_font)
        self.current_label.pack(fill=tk.X)
        
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(expand=True, fill=tk.BOTH)
        
        self.create_buttons()
    
    def create_buttons(self):
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(
                self.buttons_frame, 
                text=text, 
                font=self.display_font,
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, sticky=tk.NSEW, padx=2, pady=2)
            self.buttons_frame.grid_rowconfigure(row, weight=1)
            self.buttons_frame.grid_columnconfigure(col, weight=1)
    
    def on_button_click(self, text):
        if text == 'C':
            self.current_expression = ""
            self.total_expression = ""
        elif text == '=':
            try:
                self.total_expression = self.current_expression
                self.current_expression = str(eval(self.current_expression))
            except Exception:
                self.current_expression = "Error"
        else:
            self.current_expression += str(text)
        
        self.update_display()
    
    def update_display(self):
        self.current_label.config(text=self.current_expression[:10])
        self.total_label.config(text=self.total_expression[:10])

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
```