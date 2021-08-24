from tkinter import *

LARGE_FONT_STYLE = ("Arial", 30, "bold")
SMALL_FONT_STYLE = ("Arial", 15)
DIGITS_FONT_STYLE = ("Arial", 15, "bold")
DEFAULT_FONT_STYLE = ("Arial", 10)

class Calculadora:
    def __init__(self):
        self.root = Tk()
        self.window()
        self.total_expression = ''
        self.current_expression = ''
        self.display_frame()
        self.buttons_frame()
        self.root.mainloop()

    def window(self):
        self.root.title('Calculadora')
        self.root.geometry("250x350")
        self.root.resizable(False, False)

    def display_frame(self):
        display = Frame(self.root)
        display.pack(expand=True, fill=BOTH)

        self.total_label = Label(display, text=self.total_expression, anchor=E, padx=5, font=SMALL_FONT_STYLE)
        self.total_label.pack(expand=True, fill=X)

        self.current_label = Label(display, text=self.current_expression, anchor=E, padx=5, font=LARGE_FONT_STYLE)
        self.current_label.pack(expand=True, fill=X)

    def buttons_frame(self):
        self.buttons_display_frame = Frame(self.root)
        self.buttons_display_frame.pack(fill=X, anchor=CENTER)

        for x in range(0, 4):
            self.buttons_display_frame.rowconfigure(x, weight=1)
            self.buttons_display_frame.columnconfigure(x, weight=1)

        self.clear_current_button = Button(self.buttons_display_frame, text='CE', font=DEFAULT_FONT_STYLE, command = self.clear_labels)
        self.clear_current_button.grid(row=0, column=0, sticky=NSEW)

        self.clear_total_button = Button(self.buttons_display_frame, text='C', font=SMALL_FONT_STYLE, command=self.clear_current_label)
        self.clear_total_button.grid(row=0, column=1, sticky=NSEW)

        self.erase_current_button = Button(self.buttons_display_frame, text='\u232b', font=DEFAULT_FONT_STYLE, command=self.erase_current_label)
        self.erase_current_button.grid(row=0, column=2, sticky=NSEW)

        self.num_digits = {
            7: (1, 0), 8: (1, 1), 9: (1, 2),
            4: (2, 0), 5: (2, 1), 6: (2, 2),
            1: (3, 0), 2: (3, 1), 3: (3, 2),
            '.': (4, 0), 0: (4, 1) 
        }

        for digit, grid in self.num_digits.items():
            button = Button(self.buttons_display_frame, text=str(digit), font=DIGITS_FONT_STYLE, command= lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid[0], column=grid[1], sticky=NSEW)

        button = Button(self.buttons_display_frame, text='=', font=DEFAULT_FONT_STYLE, command=self.evaluate)
        button.grid(row=4, column=2, columnspan=2, sticky=NSEW)

        self.operations_digits = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        i=0
        for operator, symbol in self.operations_digits.items():
            button = Button(self.buttons_display_frame, text=str(symbol), font=SMALL_FONT_STYLE, command= lambda x = operator: self.append_operator(x))
            button.grid(row=i, column=3, sticky=NSEW)
            i += 1

    def add_to_expression(self, value):
        self.current_expression += str(value)
        if self.current_expression.startswith('Error'):
            self.current_expression = self.current_expression[5:]
        elif self.current_expression[0] == '0' or self.current_expression[0] == '.':
            self.current_expression = self.current_expression[1:]
        self.update_current_label()

    def append_operator(self, operator):
        self.current_expression += operator
        if self.current_expression[0] in ['+', '-', '/', '*']:
            self.current_expression = self.current_expression[1:]
        elif self.current_expression.startswith('Error'):
            self.current_expression = ''       
        self.total_expression += self.current_expression
        if len(self.total_expression) > 3:
            last = self.total_expression[len(self.total_expression)-1]
            result = self.total_expression[:len(self.total_expression)-1]
            self.total_expression = str(eval(result)) + last
        self.current_expression = ""
        self.update_total_label()
        self.update_current_label()

    def update_total_label(self):
        expression = self.total_expression
        if expression == 'Error':
            self.total_expression = ''
        for operator, symbol in self.operations_digits.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression[:25])

    def update_current_label(self):
        self.current_label.config(text=self.current_expression[:10])

    def clear_labels(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_current_label()
        self.update_total_label()

    def clear_current_label(self):
        self.current_expression = ""
        self.update_current_label()

    def erase_current_label(self):
        self.current_expression = self.current_expression[:len(self.current_expression)-1]
        self.update_current_label()

    def evaluate(self):
        self.total_expression += self.current_expression
        if self.total_expression.find('Error'):
            self.total_expression = self.total_expression.replace('Error', '')
        self.update_total_label() 
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_current_label()

    def historico_frame(self):
        self.history_frame = Frame(self.root)
        self.history_frame.grid(row=0, column=1)

if __name__ == "__main__":
    Calculadora()