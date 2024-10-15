import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

class TranslatorApp:
    def __init__(self):
        # Expanded languages list
        self.languagesList = [
            "English", "Spanish", "French", "German", "Chinese",
            "Japanese", "Korean", "Italian", "Russian", "Portuguese",
            "Arabic", "Dutch", "Turkish", "Swedish", "Danish",
            "Finnish", "Norwegian", "Thai", "Hindi", "Bengali", "Nepali"
        ]
        self.rootWindow = tk.Tk()
        self.rootWindow.title("Language Translation App")
        self.setupUi()

    def setupUi(self):
        # Set the main window background color
        self.rootWindow.configure(bg="#e3f2fd")

        # Create and style the original text box
        self.originalTextBox = tk.Text(self.rootWindow, height=10, width=40, bg="#ffffff", fg="#333333", font=("Arial", 12), bd=2, relief="groove")
        self.originalTextBox.grid(row=0, column=0, padx=10, pady=10)

        # Create and style the translated text box
        self.translatedTextBox = tk.Text(self.rootWindow, height=10, width=40, bg="#ffffff", fg="#333333", font=("Arial", 12), bd=2, relief="groove")
        self.translatedTextBox.grid(row=0, column=2, padx=10, pady=10)

        # Create and style the translate button
        self.translateButton = tk.Button(self.rootWindow, text="Translate", command=self.translateText, bg="#4CAF50", fg="white", font=("Arial", 12), bd=0)
        self.translateButton.grid(row=0, column=1, padx=10)
        self.translateButton.bind("<Enter>", lambda e: self.onHover(self.translateButton, "#45a049"))
        self.translateButton.bind("<Leave>", lambda e: self.onHover(self.translateButton, "#4CAF50"))

        # Create and style the language comboboxes
        self.fromLanguageCombo = ttk.Combobox(self.rootWindow, values=self.languagesList, font=("Arial", 12))
        self.fromLanguageCombo.grid(row=1, column=0, padx=10)
        self.fromLanguageCombo.current(0)  # Default to English

        self.toLanguageCombo = ttk.Combobox(self.rootWindow, values=self.languagesList, font=("Arial", 12))
        self.toLanguageCombo.grid(row=1, column=2, padx=10)
        self.toLanguageCombo.current(1)  # Default to Spanish

        # Create and style the clear button
        self.clearButton = tk.Button(self.rootWindow, text="Clear", command=self.clearText, bg="#f44336", fg="white", font=("Arial", 12), bd=0)
        self.clearButton.grid(row=2, column=1, padx=10)
        self.clearButton.bind("<Enter>", lambda e: self.onHover(self.clearButton, "#d32f2f"))
        self.clearButton.bind("<Leave>", lambda e: self.onHover(self.clearButton, "#f44336"))

        self.rootWindow.mainloop()

    # Method to handle button hover effects
    def onHover(self, button, color):
        button.config(bg=color)

    # Method to translate text
    def translateText(self):
        text = self.originalTextBox.get(1.0, tk.END).strip()
        if not text:
            messagebox.showerror("Error", "Please enter text to translate.")
            return

        try:
            fromLang = self.fromLanguageCombo.get().lower()
            toLang = self.toLanguageCombo.get().lower()
            translatedText = GoogleTranslator(source=fromLang, target=toLang).translate(text)
            self.translatedTextBox.delete(1.0, tk.END)  # Clear previous text
            self.translatedTextBox.insert(tk.END, translatedText)
        except Exception as e:
            messagebox.showerror("Translation Error", str(e))

    # Method to clear text
    def clearText(self):
        self.originalTextBox.delete(1.0, tk.END)
        self.translatedTextBox.delete(1.0, tk.END)

class EnhancedTranslator(TranslatorApp):
    def __init__(self):
        super().__init__()

    def translateText(self):
        print("Translation requested")  # Logging the request
        super().translateText()

if __name__ == "__main__":
    app = EnhancedTranslator()  # Instantiate the enhanced translator
