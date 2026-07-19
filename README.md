# Selenium Web Automation Framework for Ecommerce

This project contains automated test for the [DemoBlaze](https://demoblaze.com) website built with Python, Selenium, Pytest, and Allure to demonstrates best practices for web automation testing.
The goal is to make the automation framework easy to maintain, reusable, and scalable. 

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.45-green)
![Pytest](https://img.shields.io/badge/Pytest-9.1-orange)
![Allure](https://img.shields.io/badge/Allure-2.16-red)

---

## Project Architecture

- Built using the Page Object Model (POM) design pattern
- Maintains separation of concerns between tests, page objects, and test data
- Follows clean code principles and Python coding standards

---

## Continuous Integration (CI)

This project uses GitHub Actions to automatically run the automation test suite on every push and pull request.

The CI workflow performs the following steps:

- Checkout Repository
- Setup Python
- Install Google Chrome
- Install Dependencies
- Execute Selenium Test
- Upload Allure Result
  
#### Latest Execution Status:

[![Selenium - Ecommerce Web Automation](https://github.com/maolanahadiar/ecommerce-web-automation-framework/actions/workflows/selenium_ci.yml/badge.svg)](https://github.com/maolanahadiar/ecommerce-web-automation-framework/actions/workflows/selenium_ci.yml)

---

## Setup

1. Clone repository:

```bash
git clone https://github.com/maolanahadiar/ecommerce-web-automation-framework.git
```

2. Move to project directory:

```bash
cd ecommerce-web-automation-framework
```

3. Create virtual environment:

```bash
python -m venv venv
```

4. Activate virtual environment:

- macOS/Linux

```bash
source venv/bin/activate
```

- Windows

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run Tests

Run all tests:

```bash
pytest
```

Run specific tests:

```bash
pytest tests/test_login.py
```

Run & generate allure report:

```bash
pytest --alluredir=reports/allure-results
```

Open allure report:

```bash
allure serve reports/allure-results
```

---

## Demo Video
Ecommerce Web Automation: [Watch Demo](https://drive.google.com/file/d/1GMziW4Xoc74GA4weQlrsbmKe9K_sXGHK/view?usp=sharing)

---

## Test Report

> Example of test report using allure when all test cases are passed

<p align="center">
<img src="https://github.com/user-attachments/assets/6fb80430-7d5a-4069-b78c-bdaf7a4bff5f" width="900">

> Example of test report using allure when some test cases are failed

<p align="center">
<img src="https://github.com/user-attachments/assets/9c0d6d6b-de06-4ac6-8c94-c7d851bb7232" width="900">
