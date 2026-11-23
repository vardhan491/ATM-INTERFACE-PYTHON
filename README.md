# ATM Interface Using Python

A simple command-line ATM simulation built with Python and object-oriented programming.

## Features

- PIN authentication (maximum 3 attempts)
- Check account balance
- Deposit money
- Withdraw money with insufficient-balance validation
- View a masked account number
- Input validation and menu navigation

## Project structure

```text
ATM-Interface-Using-Python/
├── main.py
├── atm.py
├── bank_account.py
├── README.md
└── .gitignore
```

## Requirements

- Python 3.8 or newer
- No external packages required

## Run the project

1. Extract the ZIP file.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py`.

## Demo account

- Account number: `1234567890`
- PIN: `1234`
- Initial balance: `₹5,000`

These are demonstration credentials only. The program stores data in memory, so the balance resets to ₹5,000 whenever the program is restarted. Do not use real banking credentials or financial data.

## Files

- `main.py` — creates the demo account and starts the ATM.
- `atm.py` — handles authentication, menu display, and user interaction.
- `bank_account.py` — contains account details and deposit/withdrawal logic.
- `.gitignore` — excludes common Python-generated files.
