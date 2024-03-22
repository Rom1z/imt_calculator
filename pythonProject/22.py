import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        result_label.config(text=f"Ваш ИМТ: {bmi:.2f}")
        interpret_bmi(bmi)
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовые значения для веса и роста.")

def interpret_bmi(bmi):
    if bmi < 18.5:
        messagebox.showinfo("Интерпретация", "Недостаточный вес")
    elif 18.5 <= bmi < 25:
        messagebox.showinfo("Интерпретация", "Нормальный вес")
    elif 25 <= bmi < 30:
        messagebox.showinfo("Интерпретация", "Избыточный вес")
    else:
        messagebox.showinfo("Интерпретация", "Ожирение")

# Создание главного окна
root = tk.Tk()
root.title("Калькулятор ИМТ")

# Создание и размещение виджетов
weight_label = tk.Label(root, text="Вес (кг):")
weight_label.grid(row=0, column=0, padx=5, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

height_label = tk.Label(root, text="Рост (м):")
height_label.grid(row=1, column=0, padx=5, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Рассчитать", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2, padx=5, pady=5)

# Запуск главного цикла обработки событий
root.mainloop()
