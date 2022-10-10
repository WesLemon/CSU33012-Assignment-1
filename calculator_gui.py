import tkinter as tk
import calculator

calculation = ""


class GUI:

    # Initialises a new calculator GUI instance
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x275")
        self.text_result = tk.Text(self.root, height=2, width=16, font=("Arial", 24))
        self.text_result.grid(columnspan=5)

        # Individual buttons for the calculator
        btn_1 = tk.Button(self.root, text="1", command=lambda: self.add_to_calculation(1), width=5, font=("Arial", 14))
        btn_1.grid(row=2, column=1)
        btn_2 = tk.Button(self.root, text="2", command=lambda: self.add_to_calculation(2), width=5, font=("Arial", 14))
        btn_2.grid(row=2, column=2)
        btn_3 = tk.Button(self.root, text="3", command=lambda: self.add_to_calculation(3), width=5, font=("Arial", 14))
        btn_3.grid(row=2, column=3)
        btn_4 = tk.Button(self.root, text="4", command=lambda: self.add_to_calculation(4), width=5, font=("Arial", 14))
        btn_4.grid(row=3, column=1)
        btn_5 = tk.Button(self.root, text="5", command=lambda: self.add_to_calculation(5), width=5, font=("Arial", 14))
        btn_5.grid(row=3, column=2)
        btn_6 = tk.Button(self.root, text="6", command=lambda: self.add_to_calculation(6), width=5, font=("Arial", 14))
        btn_6.grid(row=3, column=3)
        btn_7 = tk.Button(self.root, text="7", command=lambda: self.add_to_calculation(7), width=5, font=("Arial", 14))
        btn_7.grid(row=4, column=1)
        btn_8 = tk.Button(self.root, text="8", command=lambda: self.add_to_calculation(8), width=5, font=("Arial", 14))
        btn_8.grid(row=4, column=2)
        btn_9 = tk.Button(self.root, text="9", command=lambda: self.add_to_calculation(9), width=5, font=("Arial", 14))
        btn_9.grid(row=4, column=3)
        btn_0 = tk.Button(self.root, text="0", command=lambda: self.add_to_calculation(0), width=5, font=("Arial", 14))
        btn_0.grid(row=5, column=2)
        btn_plus = tk.Button(self.root, text="+", command=lambda: self.add_to_calculation("+"), width=5,
                             font=("Arial", 14))
        btn_plus.grid(row=2, column=4)
        btn_minus = tk.Button(self.root, text="-", command=lambda: self.add_to_calculation("-"), width=5,
                              font=("Arial", 14))
        btn_minus.grid(row=3, column=4)
        btn_mul = tk.Button(self.root, text="*", command=lambda: self.add_to_calculation('*'), width=5,
                            font=("Arial", 14))
        btn_mul.grid(row=4, column=4)
        btn_equals = tk.Button(self.root, text="=", command=self.calculate, width=11,
                               font=("Arial", 14))
        btn_equals.grid(row=5, column=3, columnspan=2)
        btn_clear = tk.Button(self.root, text="C", command=self.clear_field, width=5, font=("Arial", 14))
        btn_clear.grid(row=5, column=1, columnspan=1)
        self.root.mainloop()

    # Clears the text field in the calculator
    def clear_field(self):
        global calculation
        calculation = ""
        self.text_result.delete(1.0, "end")

    # Calculates the equation from the user's input string
    def calculate(self):
        global calculation
        # TODO

    # Adds the value associated with each button to the user's input string
    def add_to_calculation(self, symbol):
        global calculation
        calculation += str(symbol)
        self.text_result.delete(1.0, "end")
        self.text_result.insert(1.0, calculation)
