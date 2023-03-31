import tkinter as tk
from tkinter import ttk

BUTTON = [
    ["AC", "C", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", "00", ".", "="],
]

SYMBOL = ['+', '-', '*', '/']

class CalcGui(object):
    def __init__(self, app=None):
        # 表示式
        self.formula = ""

        # 画面設定
        app.title("Calculator")
        app.geometry("400x600")

        # 枠設定
        calc_frame = ttk.Frame(app, width=400, height=150)
        calc_frame.propagate(False)
        calc_frame.pack(side=tk.TOP, padx=15, pady=30)
        button_frame = ttk.Frame(app, width=400, height=450)
        button_frame.propagate(False)
        button_frame.pack(side=tk.BOTTOM)

        # 文字設定
        self.calc_var = tk.StringVar()
        calc_label = tk.Label(calc_frame, textvariable=self.calc_var, font=("", 20))
        self.ans_var = tk.StringVar()
        ans_label = tk.Label(calc_frame, textvariable=self.ans_var, font=("",25))

        calc_label.pack(anchor=tk.E)
        ans_label.pack(anchor=tk.E)

        for i, row enumerate(BUTTON, 1):
            for j, num in enumerate(row):
                button = tk.Button(button_frame, text=num, font=("", 15), width=6, height=3)
                button.grid(row=i, column=j)
                

def main():
    app = tk.Tk()
    CalcGui(app)

    app.mainloop()

if __name__ == "__main__":
    main()