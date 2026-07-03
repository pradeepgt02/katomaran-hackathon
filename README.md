# 🚀 Tichi QA Automation Framework

A robust QA Automation Framework developed for the **Tichi Web Application** using **Playwright**, **Python**, and the **Page Object Model (POM)** design pattern. The framework automates core authentication workflows and demonstrates modern test automation practices.

---

## 📌 Project Overview

This project automates the authentication module of the Tichi Web Application, covering both positive and negative test scenarios. The framework is designed with the Page Object Model (POM) architecture to improve maintainability, scalability, and code reusability.

---

## 🛠️ Tech Stack

- Python
- Playwright
- Page Object Model (POM)
- Git
- GitHub

---

## 📂 Project Structure

```
Tichi_Automation
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── signup_page.py
│   ├── forgot_password_page.py
│   └── google_login_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_login_invalid_email.py
│   ├── test_login_invalid_password.py
│   ├── test_login_empty.py
│   ├── test_signup.py
│   ├── test_forgot_password.py
│   └── test_google_login.py
│
├── requirements.txt
├── run_all.py
└── README.md
```

---

## ✅ Automated Test Scenarios

### Login Module
- Valid Login
- Invalid Email Validation
- Invalid Password Validation
- Empty Email Validation

### Sign Up Module
- New User Registration

### Forgot Password Module
- Password Reset Verification

### Continue with Google
- Google Authentication Flow Validation

---

## 📋 Test Coverage

| Module | Status |
|---------|--------|
| Login | ✅ Automated |
| Sign Up | ✅ Automated |
| Forgot Password | ✅ Automated |
| Continue with Google | ⚠️ Popup Validation (Google blocks automated login) |

---

## 📊 Automation Execution Summary

| Test Cases | Result |
|------------|--------|
| Total Scenarios | 7 |
| Passed | 6 |
| Failed | 0 |
| Blocked | 1 |

**Google Login** is marked as **Blocked** because Google prevents automated browser authentication for security reasons.

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/pradeepgt02/katomaran-hackathon.git
```

Navigate to the project

```bash
cd katomaran-hackathon
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browsers

```bash
playwright install
```

---

## ▶️ Run Test Cases

Run all automated test cases

```bash
python run_all.py
```

Run individual test cases

```bash
python -m tests.test_login
```

```bash
python -m tests.test_signup
```

```bash
python -m tests.test_forgot_password
```

---

## 📷 Test Evidence

This project includes:

- Manual Test Cases
- Defect Report
- Automation Source Code
- Automation Execution Report
- GitHub Repository

---

## ✨ Key Features

- Reusable Page Object Model (POM)
- Modular framework architecture
- Positive and Negative test scenarios
- Easy maintenance
- Scalable automation structure
- Git version control

---

## 👨‍💻 Author

**Pradeep Kumar M**

QA Automation Engineer

GitHub: https://github.com/pradeepgt02

LinkedIn: https://www.linkedin.com/in/pradeepkumar-m-21685a335/

---

## 📄 License

This project was developed for learning, interview preparation, and QA automation portfolio purposes.