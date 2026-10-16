import customtkinter as ctk
import configs as cfg

ctk.set_appearance_mode(cfg.APPEARANCE)
ctk.set_default_color_theme(cfg.THEME)

BUTTONS = {
    'C': (1, 0, '#a33', '#822'),
    '(': (1, 1, None, None),
    ')': (1, 2, None, None),
    '/': (1, 3, '#e08a00', '#b36e00'),

    '7': (2, 0, '#333', '#444'),
    '8': (2, 1, '#333', '#444'),
    '9': (2, 2, '#333', '#444'),
    '*': (2, 3, '#e08a00', '#b36e00'),

    '4': (3, 0, '#333', '#444'),
    '5': (3, 1, '#333', '#444'),
    '6': (3, 2, "#333", '#444'),
    '-': (3, 3, '#e08a00', '#b36e00'),

    '1': (4, 0, '#333', '#444'),
    '2': (4, 1, '#333', '#444'),
    '3': (4, 2, '#333', '#444'),
    '+': (4, 3, '#e08a00', '#b36e00'),

    '0': (5, 0, '#333', '#444'),
    '.': (5, 1, "#333", "#444"),
    '⌫': (5, 2, None, None),
    '=': (5, 3, "#2a7", "#185"),
}

class Calculator(ctk.CTk):
        def __init__(self):
                super().__init__()
                self.title(cfg.WINDOW_TITLE)
                self.geometry(cfg.WINDOW_SIZE)
                self.resizable(False, False)

                self.expression = ''

                self.display = ctk.CTkEntry(
                        self, font=(cfg.FONT, 32), justify='right', height=70
                )

                self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky='ew')

                self.buttons = {}
                for label, (row, col, fg, hover) in BUTTONS.items():
                        btn = ctk.CTkButton(
                                self,
                                text=label,
                                width=65,
                                height=65,
                                corner_radius=32,
                                font=(cfg.FONT, 20),
                                fg_color=fg,
                                hover_color=hover,
                                command=lambda x=label: self.on_click(x),
                        )

                        btn.grid(row=row, column=col, padx=5, pady=5)
                        self.buttons[label] = btn

                self.bind('<Return>', lambda e: self.on_click('='))
                self.bind('<BackSpace>', lambda e: self.on_click('⌫'))
                self.bind('<Key>', self.on_key)

        def on_key(self, event):
                if event.char and event.char in '0123456789+-*/().':
                        self.on_click(event.char)

        def on_click(self, value):
                if value == 'C':
                        self.expression = ''

                elif value == '⌫':
                        self.expression = self.expression[:-1]

                elif value == '=':
                        try:
                                self.expression = str(eval(self.expression, {'__builtins__': {}}, {}))

                        except Exception:
                                self.expression = 'Error'

                else:
                        if self.expression == 'Error':
                                self.expression = ''

                        self.expression += value\

                self.display.delete(0, 'end')
                self.display.insert(0,  self.expression)


if __name__ == '__main__':
        Calculator().mainloop()