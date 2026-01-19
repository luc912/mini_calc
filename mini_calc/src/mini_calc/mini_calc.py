import tkinter as tk
 
 
def calculate(op):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
 
        if op == '+':
            result.set(a + b)
        elif op == '-':
            result.set(a - b)
        elif op == '*':
            result.set(a * b)
        elif op == '/':
            result.set(a / b if b != 0 else "Fehler: ÷0")
    except ValueError:
        result.set("Ungültige Eingabe")
 
 
# ==================================================
# Farben (Dark Mode)
# ==================================================
BG = "#1e1e1e"
ENTRY_BG = "#2d2d2d"
BTN_BG = "#3a3a3a"
BTN_ACTIVE = "#505050"
TEXT = "#ffffff"
ACCENT = "#00adb5"
 
# ==================================================
# Hauptfenster
# ==================================================
root = tk.Tk()
root.title("Mini-Rechner")
root.configure(bg=BG, padx=20, pady=20)
root.resizable(False, False)
 
# ==================================================
# Eingabefelder
# ==================================================
entry_font = ("Segoe UI", 14)
 
entry_a = tk.Entry(
    root,
    font=entry_font,
    width=12,
    justify="right",
    bg=ENTRY_BG,
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat"
)
 
entry_b = tk.Entry(
    root,
    font=entry_font,
    width=12,
    justify="right",
    bg=ENTRY_BG,
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat"
)
 
entry_a.grid(row=0, column=0, padx=5, pady=5)
entry_b.grid(row=0, column=1, padx=5, pady=5)
 
# ==================================================
# Ergebnisanzeige
# ==================================================
result = tk.StringVar(value="0")
 
result_label = tk.Label(
    root,
    textvariable=result,
    font=("Segoe UI", 20, "bold"),
    bg=BG,
    fg=ACCENT,
    width=18,
    anchor="e"
)
 
result_label.grid(row=1, column=0, columnspan=2, pady=(15, 25))
 
# ==================================================
# Buttons
# ==================================================
button_font = ("Segoe UI", 14, "bold")
 
buttons = ['+', '-', '*', '/']
 
for i, op in enumerate(buttons):
    tk.Button(
        root,
        text=op,
        font=button_font,
        width=6,
        height=2,
        bg=BTN_BG,
        fg=TEXT,
        activebackground=BTN_ACTIVE,
        activeforeground=TEXT,
        relief="flat",
        command=lambda o=op: calculate(o)
    ).grid(row=2 + i // 2, column=i % 2, padx=8, pady=8)
 
# ==================================================
# Start
# ==================================================
root.mainloop()
 
 