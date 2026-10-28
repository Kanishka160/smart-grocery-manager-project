# 🛒 Smart Grocery Manager

A Python-based Smart Grocery Manager designed to simplify grocery inventory management, organize grocery items, and make everyday shopping more efficient.

The application helps users manage grocery records, update item details, monitor available stock, and explore recipe-related functionality through a modular Python application.

## 📌 Project Overview

Managing grocery items manually can be time-consuming, especially when tracking available stock and maintaining item records.

Smart Grocery Manager provides a simple application for organizing grocery inventory and maintaining grocery-related information in a database. It also includes a separate recipe-related module to support recipe functionality.

The project demonstrates Python application development, database operations, and modular software design.

## ✨ Key Features

- **Grocery Management:** Manage grocery item records in one place.
- **Add Grocery Items:** Register new items in the inventory.
- **Update Item Details:** Modify existing grocery information.
- **Inventory Tracking:** View and manage grocery stock information.
- **Database Integration:** Store grocery records using a database.
- **Recipe Module:** Includes a dedicated Python module for recipe-related functionality.
- **Modular Architecture:** Separates application logic and database operations into different Python files.
- **User-Friendly Application:** Provides an accessible way to manage grocery information.

*The availability of each feature depends on its implementation in the current source code.*

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| SQLite | Local database storage, if configured by the application |
| SQL | Database queries and record management |
| Python Modules | Separation of application and database logic |
| Git and GitHub | Version control and source code management |

## 📂 Project Structure

```text
smart-grocery-manager-project/
│
├── app.py                # Main application entry point
├── ai_recipe.py          # Recipe-related functionality
├── database.py           # Database operations
├── database_manager.py   # Database management logic
├── grocery.db            # Local database file
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## ⚙️ Getting Started

### Prerequisites

Install the following before running the project:

- Python 3.10 or another version supported by the dependencies
- Git
- pip package manager

### 1. Clone the Repository

```bash
git clone https://github.com/Kanishka160/smart-grocery-manager-project.git
cd smart-grocery-manager-project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

If the project uses a different framework or startup command, follow the configuration and instructions in the source code.

## 🗄️ Database Management

The project includes database-related modules and a `grocery.db` file.

Database operations may include:

- Creating and maintaining grocery records.
- Retrieving saved inventory information.
- Updating existing grocery items.
- Supporting persistent storage between application sessions.

The exact database schema and operations are defined by the project's implementation.

## 🎯 Project Objectives

- Simplify grocery inventory management.
- Practice Python programming and modular development.
- Understand database connectivity and CRUD operations.
- Organize grocery information efficiently.
- Explore the integration of recipe-related functionality into a grocery application.

## 🔮 Future Enhancements

- Add low-stock alerts and expiry-date reminders.
- Introduce shopping list generation.
- Provide grocery usage and spending reports.
- Improve recipe suggestions using available ingredients.
- Add search, sorting, and category filters.
- Develop a dashboard for inventory analytics.
- Add automated tests and input validation.

## 👩‍💻 Author

**Kanishka Raj**

B.Tech — Artificial Intelligence and Machine Learning

[GitHub Profile](https://github.com/Kanishka160)

