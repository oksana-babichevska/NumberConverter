import tkinter as tk
from tkinter import messagebox, filedialog
from converter.core import convert_to_binary, convert_to_octal, convert_to_decimal, convert_to_hexadecimal
from converter.file_handler import save_results

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвертація чисел")
        self.root.geometry("600x400")
        self.root.configure(bg="#F5F5F5")

        # Заголовок
        tk.Label(self.root, text="Конвертація чисел", font=("Arial", 18, "bold"), bg="#F5F5F5", fg="#333333").pack(pady=10)

        # Поля введення
        self.frame_input = tk.Frame(self.root, bg="#F5F5F5")
        self.frame_input.pack(pady=10)

        tk.Label(self.frame_input, text="Число:", bg="#F5F5F5", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
        self.entry_number = tk.Entry(self.frame_input, font=("Arial", 12), width=20)
        self.entry_number.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_input, text="Система (2, 8, 10, 16):", bg="#F5F5F5", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
        self.entry_base = tk.Entry(self.frame_input, font=("Arial", 12), width=20)
        self.entry_base.grid(row=1, column=1, padx=5, pady=5)

        # Кнопка для переведення
        self.convert_button = tk.Button(self.root, text="Перевести", command=self.convert_number, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.convert_button.pack(pady=10)

        # Вивід результатів
        self.frame_output = tk.Frame(self.root, bg="#F5F5F5")
        self.frame_output.pack(pady=10)

        self.results = {}
        for idx, label in enumerate(["Двійкова:", "Вісімкова:", "Десяткова:", "Шістнадцяткова:"]):
            tk.Label(self.frame_output, text=label, bg="#F5F5F5", font=("Arial", 12)).grid(row=idx, column=0, padx=5, pady=5)
            self.results[label] = tk.Entry(self.frame_output, font=("Arial", 12), state='readonly', width=30)
            self.results[label].grid(row=idx, column=1, padx=5, pady=5)

        # Кнопка для збереження результатів
        self.save_button = tk.Button(self.root, text="Зберегти результати", command=self.save_results, bg="#2196F3", fg="white", font=("Arial", 12))
        self.save_button.pack(pady=10)

    def convert_number(self):
        try:
            number = self.entry_number.get()
            base = int(self.entry_base.get())
            decimal_number = convert_to_decimal(number, base)

            binary = convert_to_binary(decimal_number)
            octal = convert_to_octal(decimal_number)
            hexadecimal = convert_to_hexadecimal(decimal_number)

            self.results["Двійкова:"].config(state='normal')
            self.results["Двійкова:"].delete(0, tk.END)
            self.results["Двійкова:"].insert(0, binary)
            self.results["Двійкова:"].config(state='readonly')

            self.results["Вісімкова:"].config(state='normal')
            self.results["Вісімкова:"].delete(0, tk.END)
            self.results["Вісімкова:"].insert(0, octal)
            self.results["Вісімкова:"].config(state='readonly')

            self.results["Десяткова:"].config(state='normal')
            self.results["Десяткова:"].delete(0, tk.END)
            self.results["Десяткова:"].insert(0, str(decimal_number))
            self.results["Десяткова:"].config(state='readonly')

            self.results["Шістнадцяткова:"].config(state='normal')
            self.results["Шістнадцяткова:"].delete(0, tk.END)
            self.results["Шістнадцяткова:"].insert(0, hexadecimal)
            self.results["Шістнадцяткова:"].config(state='readonly')
        except ValueError:
            messagebox.showerror("Помилка", "Неправильний ввід даних!")

    def save_results(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                    filetypes=[("Text files", "*.txt")])
            if filename:
                results = {label: field.get() for label, field in self.results.items()}
                save_results(filename, results)
                messagebox.showinfo("Успіх", "Результати збережено!")
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося зберегти файл: {e}")
