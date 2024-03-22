import tkinter as tk
from tkinter import filedialog, messagebox
from rembg import remove
from PIL import Image

class BackgroundRemoverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Удаление фона изображения")

        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Выберите изображение:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(self.master, textvariable=self.input_path, width=40, state='disabled').grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.master, text="Обзор", command=self.browse_input).grid(row=0, column=2, padx=10, pady=5)

        tk.Label(self.master, text="Сохранить результат в:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self.master, textvariable=self.output_path, width=40, state='disabled').grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.master, text="Обзор", command=self.browse_output).grid(row=1, column=2, padx=10, pady=5)

        tk.Button(self.master, text="Удалить фон", command=self.remove_background).grid(row=2, column=1, pady=10)

    def browse_input(self):
        file_path = filedialog.askopenfilename(title="Выберите изображение", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))
        if file_path:
            self.input_path.set(file_path)

    def browse_output(self):
        file_path = filedialog.asksaveasfilename(title="Выберите место для сохранения", defaultextension=".png", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
        if file_path:
            self.output_path.set(file_path)

    def remove_background(self):
        input_path = self.input_path.get()
        output_path = self.output_path.get()
        if not input_path or not output_path:
            messagebox.showerror("Ошибка", "Выберите изображение и место для сохранения")
            return

        try:
            open_image = Image.open(input_path)
            output = remove(open_image)
            output.save(output_path)
            messagebox.showinfo("Успех", "Фон успешно удален и сохранен")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

def main():
    root = tk.Tk()
    app = BackgroundRemoverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
