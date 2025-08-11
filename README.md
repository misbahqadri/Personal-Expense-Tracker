# 💸 Personal Finance Tracker

A comprehensive personal finance management application built with Streamlit that helps you track expenses, income, set budgets, and achieve financial goals.

## ✨ Features

### 📊 Core Features
- **Expense & Income Tracking**: Add, edit, and delete financial transactions
- **Budget Management**: Set monthly budgets and track spending against them
- **Financial Goals**: Set and track progress towards financial goals
- **Data Visualization**: Interactive charts and reports
- **Data Export/Import**: Backup and restore your financial data

### 🎯 Advanced Features
- **Smart Validation**: Input validation to prevent data errors
- **Data Cleanup**: Tools to maintain data quality
- **Caching**: Improved performance with data caching
- **Backup System**: Automatic backup creation and management
- **Responsive Design**: Works on desktop and mobile devices

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd expense_tracker_copy
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run main.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

## 📁 Project Structure

```
expense_tracker_copy/
├── main.py                 # Main application entry point
├── config.py              # Configuration and constants
├── utils.py               # Shared utility functions
├── home.py                # Home dashboard
├── add_expense.py         # Add/edit transactions
├── budget.py              # Budget management
├── report.py              # Reports and analytics
├── monthly.py             # Monthly overview
├── goal.py                # Financial goals
├── about.py               # About page
├── guidelines.py          # User guidelines
├── data_cleanup.py        # Data maintenance tools
├── data/                  # Data storage
│   ├── add_expense.csv    # Transaction data
│   └── financial_goals.csv # Goals data
├── backups/               # Backup files
├── images/                # Application images
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🎮 How to Use

### 1. Getting Started
- **Home Page**: View your financial summary and recent transactions
- **Add Expense**: Record new income or expense entries
- **Budget**: Set and track monthly budgets by category

### 2. Adding Transactions
1. Go to "Add Expense" page
2. Select transaction type (Income/Expense)
3. Choose or create a category
4. Enter amount and date
5. Add optional description
6. Click "Save Entry"

### 3. Budget Management
1. Go to "Budget" page
2. Set monthly budgets for each category
3. Use quick templates or set custom amounts
4. Monitor spending against budgets

### 4. Data Management
- **Export Data**: Download your data as CSV
- **Data Cleanup**: Use the cleanup tools to maintain data quality
- **Backup**: Automatic backups are created regularly

## 🔧 Configuration

### Customizing Categories
Edit `config.py` to modify default categories:
```python
DEFAULT_CATEGORIES = ["Salary", "Food", "Transport", "Shopping", "Bills", "Others"]
```

### Currency Settings
Change currency in `config.py`:
```python
CURRENCY = "₹"  # Change to your preferred currency
```

## 🛠️ Data Validation

The application includes comprehensive data validation:
- **Amount Validation**: Must be between 0.01 and 1,000,000
- **Category Validation**: Required field with 50 character limit
- **Description Validation**: Optional field with 200 character limit
- **Date Validation**: Ensures valid date format

## 📊 Data Storage

- **Format**: CSV files stored in `data/` directory
- **Backup**: Automatic backups in `backups/` directory
- **Security**: Data stays on your local machine

## 🐛 Troubleshooting

### Common Issues

1. **"No module named 'streamlit'"**
   ```bash
   pip install streamlit
   ```

2. **Data not loading**
   - Check if `data/` directory exists
   - Verify CSV file permissions

3. **Performance issues**
   - Use data cleanup tools to remove invalid entries
   - Clear browser cache

### Data Recovery
- Check `backups/` directory for recent backups
- Use data cleanup tools to fix common issues

## 🔒 Privacy & Security

- **Local Storage**: All data is stored locally on your machine
- **No Cloud**: No data is sent to external servers
- **Backup**: Regular automatic backups protect your data

## 🎨 Customization

### Styling
Modify the application appearance by editing CSS in individual pages or creating a custom theme.

### Adding Features
The modular structure makes it easy to add new features:
1. Create new Python files for new pages
2. Add navigation entries in `main.py`
3. Use utility functions from `utils.py`

## 📈 Performance Tips

1. **Regular Cleanup**: Use data cleanup tools monthly
2. **Limit Data**: Archive old data if performance slows
3. **Browser Cache**: Clear cache if experiencing issues

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 Changelog

### Version 2.0 (Current)
- ✅ Added budget management system
- ✅ Improved data validation
- ✅ Added data cleanup tools
- ✅ Enhanced UI/UX
- ✅ Added caching for better performance
- ✅ Implemented backup system

### Version 1.0 (Original)
- ✅ Basic expense tracking
- ✅ Simple reports
- ✅ Goal setting

## 📞 Support

- **Documentation**: Check the Guidelines page in the app
- **Issues**: Report bugs through GitHub issues
- **Email**: Contact developer at xyz@gmail.com

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io)
- Data visualization with [Plotly](https://plotly.com)
- Data processing with [Pandas](https://pandas.pydata.org)

---

**Happy Financial Tracking! 💰**
"# Personal-Finance-Tracker" 
