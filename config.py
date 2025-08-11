import os
from datetime import datetime

# File paths
DATA_DIR = "data"
EXPENSE_FILE = os.path.join(DATA_DIR, "add_expense.csv")
GOALS_FILE = os.path.join(DATA_DIR, "financial_goals.csv")
BACKUP_DIR = "backups"
BUDGETS_FILE = os.path.join(DATA_DIR, "budgets.csv")

# Ensure directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(BACKUP_DIR, exist_ok=True)

# Categories
DEFAULT_CATEGORIES = ["Salary", "Food", "Transport", "Shopping", "Bills", "Others"]

# Currency
CURRENCY = "₹"

# Date formats
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# Validation limits
MAX_AMOUNT = 1000000  # Maximum transaction amount
MAX_DESCRIPTION_LENGTH = 200
MIN_AMOUNT = 0.01

# App settings
APP_TITLE = "Personal Finance Tracker"
APP_ICON = "💸"
PAGE_LAYOUT = "wide"

# Developer info
DEVELOPER_NAME = "Misbah Qadri"
DEVELOPER_EMAIL = "misbahqadri@gmail.com"
DEVELOPER_GITHUB = "github.com/yourprofile"
