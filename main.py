import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkcalendar import DateEntry
import json
from datetime import datetime
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Database")

        self.file_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.file_dir, '1.json')
        
        self.setup_data_fields()
        self.setup_buttons()

    def setup_data_fields(self):

        # Date field
        ttk.Label(self, text="Куплено:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self, width=12, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        self.combos = {}
        # Define options
        self.manufacturer_options = {
            "ПК": ["HP", "Dell", "Lenovo"],
            "Моноблок": ["Apple", "Lenovo", "HP"],
            "Ноутбук": ["Asus", "Acer", "MSI"],
            "Принтер": ["Canon", "Epson", "Brother"]
        }

        options = {
            "Тип": ["ПК", "Моноблок", "Ноутбук", "Принтер"],
            "Состояние": ["Хорошее", "Нормальное", "Плохое"],
            "Производитель": self.manufacturer_options["ПК"]  # Default to PC manufacturers
        }

        def update_manufacturers(*args):
            selected_type = self.combos["Тип"][1].get()
            self.combos["Производитель"][0]['values'] = self.manufacturer_options[selected_type]
            self.combos["Производитель"][1].set(self.manufacturer_options[selected_type][0])

        # Create dropdown menus for each option
        for row, (label, values) in enumerate(options.items(), 1):
            ttk.Label(self, text=label).grid(row=row, column=0, padx=5, pady=5)

            var = tk.StringVar(value=values[0])
            combo = ttk.Combobox(self, values=values, textvariable=var, state="readonly")
            combo.grid(row=row, column=1, padx=5, pady=5)

            self.combos[label] = (combo, var)
            
            if label == "Тип":
                var.trace('w', update_manufacturers)


        ttk.Label(self, text="Доп. Заметки:").grid(row=4, column=0, padx=5, pady=5)
        self.notes_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.notes_var).grid(row=4, column=1, padx=5, pady=5)

    def setup_buttons(self):
        ttk.Button(self, text="Сохранить", command=self.save_file).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(self, text="Загрузить", command=self.load_file).grid(row=1, column=2, padx=5, pady=5)
        ttk.Button(self, text="Ремонт", command=self.view_repair).grid(row=2, column=2, padx=5, pady=5)
        ttk.Button(self, text="Утиль", command=self.view_scrap).grid(row=3, column=2, padx=5, pady=5)

    def refresh_listbox(self, listbox, data):
        listbox.delete(0, tk.END)
        for index, item in enumerate(data):
            record_summary = (
                f"№ {index + 1}: "
                f"Дата: {item.get('purchase_date')} | "
                f"Тип: {item.get('Тип')} | "
                f"Состояние: {item.get('Состояние')} | "
                f"Производитель: {item.get('Производитель')}"
            )
            listbox.insert(tk.END, record_summary)

    def view_items(self, filename, title):
        filepath = os.path.join(self.file_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Create a new window to display records
            display_window = tk.Toplevel(self)
            display_window.title(title)

            # Create a listbox to display records
            record_listbox = tk.Listbox(display_window, width=100, height=10)
            record_listbox.pack(padx=10, pady=10)

            if isinstance(data, list):
                for index, item in enumerate(data):
                    record_summary = (
                        f"№ {index + 1}: "
                        f"Дата: {item.get('purchase_date')} | "
                        f"Тип: {item.get('Тип')} | "
                        f"Состояние: {item.get('Состояние')} | "
                        f"Производитель: {item.get('Производитель')}"
                    )
                    record_listbox.insert(tk.END, record_summary)


    def view_repair(self):
        self.view_items('repair.json',"Ремонт")
    
    def view_scrap(self):
        self.view_items('scrap.json',"Утиль")

    def save_file(self):
        purchase_date_obj = self.date_entry.get_date()
        purchase_date_str = purchase_date_obj.strftime("%Y-%m-%d") # Format as string

        data = {
            'purchase_date': purchase_date_str, 
            'Тип': self.combos['Тип'][1].get(), 
            'Состояние': self.combos['Состояние'][1].get(), 
            'Производитель': self.combos['Производитель'][1].get(), 
            'notes_text': self.notes_var.get(),
            'entry_saved_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S") # timestamp of save
        }

        if path := filedialog.askopenfilename(filetypes=[("JSON files", "*.json")]):
            try:
                existing_data = []
                if os.path.exists(path):
                    with open(path, 'r') as f:
                        existing_data = json.load(f)
                        if not isinstance(existing_data, list):
                            existing_data = [existing_data]

                existing_data.append(data)

                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(existing_data, f, indent=4)
            except Exception as e:
                messagebox.showerror("Error", str(e))   

    def load_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Create a new window to display records
        display_window = tk.Toplevel(self)
        display_window.title("Saved Records")

        # Create a listbox to display records
        record_listbox = tk.Listbox(display_window, width=100, height=10)
        record_listbox.pack(padx=10, pady=10)

        if isinstance(data, list):
            # Populate the listbox with record summaries
            for index, item in enumerate(data):
                record_summary = (
                    f"№ {index + 1}: "
                    f"Дата: {item.get('purchase_date')} | "
                    f"Тип: {item.get('Тип')} | "
                    f"Состояние: {item.get('Состояние')} | "
                    f"Производитель: {item.get('Производитель')}"
                )
                record_listbox.insert(tk.END, record_summary)

            def show_details():
                selected_index = record_listbox.curselection()
                if selected_index:
                    
                    # Create detail window
                    detail_window = tk.Toplevel(display_window)
                    detail_window.title(f"Запись {selected_index[0] + 1}")

                    # Create text widget for details
                    text_widget = tk.Text(detail_window, wrap=tk.WORD, width=60, height=20)
                    text_widget.pack(padx=10, pady=10)

                    # Add scrollbar
                    scrollbar = ttk.Scrollbar(detail_window, command=text_widget.yview)
                    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                    text_widget.config(yscrollcommand=scrollbar.set)

                    # Display detailed information
                    item = data[selected_index[0]]
                    display_string = (
                        f"Дата: {item.get('purchase_date')}\n"
                        f"Тип: {item.get('Тип')}\n"
                        f"Состояние: {item.get('Состояние')}\n"
                        f"Производитель: {item.get('Производитель')}\n"
                        f"Доп. Заметки: {item.get('notes_text')}\n"
                        f"Сохранено: {item.get('entry_saved_at')}\n"
                    )
                    text_widget.insert(tk.END, display_string)
                    text_widget.config(state='disabled')  # Make text read-only

                    self.selected_record = item 

            detail_button = ttk.Button(display_window, text="Показать детали", command=show_details)
            detail_button.pack(pady=5)

            delete_button = ttk.Button(display_window, text="Удалить запись", command=lambda: self.delete_record(data, record_listbox))
            delete_button.pack(pady=5)

            # Initialize selected_record attribute
            self.selected_record = None
            
            repair_button = ttk.Button(display_window, text="На ремонт", command=lambda: self.send_to_repair(data, record_listbox))
            repair_button.pack(pady=5)

            scrap_button = ttk.Button(display_window, text="На утилизацию", command=lambda: self.send_to_scrap(data, record_listbox))
            scrap_button.pack(pady=5)
    
    def send_to_repair(self, data, listbox):
        selected_index = listbox.curselection()
        if selected_index:
            item = data[selected_index[0]]
            item['status'] = 'repair'
            item['entry_saved_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            repair_file = os.path.join(self.file_dir, 'repair.json')
            if os.path.exists(repair_file):
                with open(repair_file, 'r', encoding='utf-8') as f:
                    repair_data = json.load(f)
                    if not isinstance(repair_data, list):
                        repair_data = [repair_data]

                repair_data.append(item)
                with open(repair_file, 'w', encoding='utf-8') as f:
                    json.dump(repair_data, f, indent=4)

                del data[selected_index[0]]
                with open(self.file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4)
            else:
                repair_data = []

            self.refresh_listbox(listbox, data)
            

    def send_to_scrap(self, data, listbox):
        selected_index = listbox.curselection()
        if selected_index:
            item = data[selected_index[0]]
            item['status'] = 'scrap'
            item['entry_saved_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            scrap_file = os.path.join(self.file_dir, 'scrap.json')
            if os.path.exists(scrap_file):
                with open(scrap_file, 'r', encoding='utf-8') as f:
                    scrap_data = json.load(f)
                    if not isinstance(scrap_data, list):
                        scrap_data = [scrap_data]

                scrap_data.append(item)

                with open(scrap_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4)

                del data[selected_index[0]]
                with open(self.file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4)
            else:
                scrap_data = []

            self.refresh_listbox(listbox, data)

    def delete_record(self, data, listbox):
        selected_index = listbox.curselection()
        if selected_index:
            if messagebox.askyesno("Confirm", "Вы уверены, что хотите удалить эту запись?"):
                del data[selected_index[0]]
                with open(self.file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4)
                listbox.delete(selected_index)
                messagebox.showinfo("Success", "Запись удалена")
            self.refresh_listbox(listbox, data)
            
if __name__ == "__main__":
    Application().mainloop()