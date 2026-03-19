
# Glowify Automation Framework

## Overview
Glowify Automation is a robust test framework for end-to-end UI testing of the Glowify Cosmetics web application. It uses the Page Object Model for maintainable and scalable test design.

## Tech Stack
- Python 3
- Selenium WebDriver
- Pytest
- Allure Reports

## Project Structure
- `pages/`: Page Object classes for each site page (Home, Product List, Product Detail, Cart, Login, Signup, Checkout)
- `tests/`: Test scripts (e.g., test_e2e_flow.py for full user journey)
- `utils/`: Utility modules (driver factory, waits)
- `config/`: Configuration files
- `test_data/`: Test data
- `reports/`: Test reports and screenshots

## Key Features
- End-to-end user journey automation
- Dynamic waits and robust element handling
- Automatic screenshots on test failure (with Allure attachment)
- Page Object Model for maintainability
- Smart login/signup handling
- Allure reporting for rich test results

## How to Run Tests
```bash
pytest -v -s
```

## Generate Allure Report
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

## Example Test Flow
- Open site
- Navigate to products
- Add product to cart
- Proceed to checkout
- Handle login/signup if needed
- Complete order