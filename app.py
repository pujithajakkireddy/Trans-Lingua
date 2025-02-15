import tkinter as tk
from tkinter import ttk, messagebox
from translate import Translator  # Correct import
def translate_text():
    try:
        source_text = text_input.get("1.0", tk.END).strip()
        src_lang = source_lang_combo.get()
        dest_lang = dest_lang_combo.get()

        if not source_text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return

        translator = Translator(from_lang=src_lang, to_lang=dest_lang)
        translation = translator.translate(source_text)

        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translation)

    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")
        print(f"Full Error Details: {e}")

# Initialize main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("600x400")
root.resizable(False, False)

# Supported languages (you can customize this list)
language_choices = [
    "en", "es", "fr", "de", "it", "pt", "ja", "ko", "zh", "ru", "ar", "hi"  # Common languages
]

# Source language selection
source_lang_label = ttk.Label(root, text="Source Language:")
source_lang_label.pack(pady=5)
source_lang_combo = ttk.Combobox(root, values=language_choices, width=20)
source_lang_combo.set("en")  # Default to English
source_lang_combo.pack()

# Text input
text_input = tk.Text(root, height=5, width=60)
text_input.pack(pady=5)

# Destination language selection
dest_lang_label = ttk.Label(root, text="Destination Language:")
dest_lang_label.pack(pady=5)
dest_lang_combo = ttk.Combobox(root, values=language_choices, width=20)
dest_lang_combo.set("es")  # Default to Spanish
dest_lang_combo.pack()

# Translate button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Output text field
text_output = tk.Text(root, height=5, width=60, state=tk.NORMAL)
text_output.pack(pady=5)

# Run application
root.mainloop()
