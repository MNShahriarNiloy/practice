import tkinter as tk

root = tk.Tk()
root.title("Palindrome & Primes")
root.geometry("240x460")
root.resizable(0, 0)
root.configure(bg="black")

input_text = tk.StringVar(value="")  
result_text = tk.StringVar(value="")  

def update_display(button_text):
    result_text.set("")
    current = input_text.get()
    input_text.set(current + button_text)


def check_criteria():
    number_str = input_text.get()
    if not number_str.isdigit():
        result_text.set("Invalid Input!")
        return

    number = int(number_str)
    is_palindrome = number_str == number_str[::-1]
    is_prime = number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1))

    if is_palindrome and is_prime:
        result_text.set(f"{number} is a Palindrome & Prime!")
    elif is_palindrome:
        result_text.set(f"{number} is a Palindrome!")
    elif is_prime:
        result_text.set(f"{number} is a Prime!")
    else:
        result_text.set(f"{number} is Neither!")


display = tk.Label(
    root,
    textvariable=input_text,  
    font=("Arial", 24),
    bg="black",
    fg="white",
    anchor="e",  
)
display.grid(row=0, column=0, columnspan=3, pady=10, sticky="ew")


result_display = tk.Label(
    root,
    textvariable=result_text,  
    font=("Arial", 16),
    bg="black",
    fg="yellow",
    anchor="center",  
)
result_display.grid(row=1, column=0, columnspan=3, pady=10, sticky="ew")


buttons = [
    {"text": "1", "row": 2, "col": 0},
    {"text": "2", "row": 2, "col": 1},
    {"text": "3", "row": 2, "col": 2},
    {"text": "4", "row": 3, "col": 0},
    {"text": "5", "row": 3, "col": 1},
    {"text": "6", "row": 3, "col": 2},
    {"text": "7", "row": 4, "col": 0},
    {"text": "8", "row": 4, "col": 1},
    {"text": "9", "row": 4, "col": 2},
    {"text": "0", "row": 5, "col": 0},
]

for button in buttons:
    tk.Button(
        root,
        text=button["text"],
        bg="green",
        fg="black",
        width=10,
        height=5,
        command=lambda b=button["text"]: update_display(b)
    ).grid(row=button["row"], column=button["col"], padx=0, pady=0)


button_enter = tk.Button(
    root,
    text="Check",
    bg="green",
    fg="black",
    width=10,
    height=5,
    command=check_criteria
)
button_enter.grid(row=5, column=1)

def clear_display():
    input_text.set("")
    result_text.set("")

button_clear = tk.Button(
    root,
    text="Clear",
    bg="green",
    fg="black",
    width=10,
    height=5,
    command=clear_display
)
button_clear.grid(row=5, column=2)

# Run the application
root.mainloop()
