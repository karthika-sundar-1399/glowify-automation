# Glowify Automation Framework

## Tech Stack
- Python
- Selenium
- Pytest
- Allure Reports

## Features
- End-to-End automation
- Login handling
- Dynamic waits
- Page Object Model

## Run Tests
```bash
pytest -v -s

# Generate Report
pytest --alluredir=reports/allure-results
allure serve reports/allure-results