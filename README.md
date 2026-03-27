# 💱 Currency Converter (PRO Edition)

A powerful and interactive **Python-based currency converter** that uses real-time exchange rates from an external API. Built as a beginner project and upgraded into a structured CLI tool with proper validation, error handling, and modular design.

---

## 🚀 Features

* 💱 Convert currencies in real-time using live exchange rates
* 🌍 Supports multiple global currencies (USD, EUR, KES, etc.)
* 🧠 Smart input validation (prevents crashes)
* 🖥️ Interactive command-line interface (CLI menu)
* 📡 API integration using `requests`
* ⚠️ Robust error handling for network/API issues
* 🔎 Option to list available currencies

---

## 🛠️ Technologies Used

* Python 3.8+
* requests (for API calls)
* ExchangeRate API (for live currency data)

---

## 📦 Prerequisites

Before running this project, ensure you have:

1. **Python 3.8 or higher** installed
2. A code editor (e.g., VS Code)
3. Internet connection (required for API requests)

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/currency-converter.git
cd currency-converter
```

(Optional) Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

* **Windows:**

```bash
venv\Scripts\activate
```

* **Linux / Mac:**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

---

## 💻 Example

```
🚀 Welcome to the PRO Currency Converter

💱 Currency Converter
----------------------------------------
1. Convert Currency
2. List Available Currencies
3. Exit

Choose an option (1-3): 1

Enter amount: 100
From currency: USD
To currency: KES

✅ 100.00 USD = 15,800.00 KES
```

---

## 📁 Project Structure

```
currency-converter/

├── main.py            # Main application entry point
├── requirements.txt   # Project dependencies
└── README.md          # Documentation
```

---

## 📈 Learning Objectives

This project demonstrates:

* API integration in Python
* Working with JSON data
* Input validation and error handling
* Writing clean, modular code
* Building interactive CLI applications

---

## 🔮 Future Improvements

* 📊 Save conversion history
* 💰 Add currency symbols
* 📱 GUI version (Tkinter / PyQt)
* 🌐 Web version using Flask
* ⚡ Offline mode with cached rates

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes
4. Commit your changes

   ```bash
   git commit -m "Add new feature"
   ```
5. Push to your branch

   ```bash
   git push origin feature-branch
   ```
6. Open a Pull Request 🚀

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork it
* 🧠 Share ideas or improvements
