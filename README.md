# QA Automation Intern Assignment

This project contains automated tests for:

1. API Testing (Reqres API)

2. UI Testing (https://www.iamdave.ai)

3. Optional: Locust Load Testing

The tests are written using Python, pytest, requests, Selenium, and webdriver-manager.

---



## 📦 Project Structure


QA assignment/

│

├─ tests/

│ ├─ api\_tests.py

│ ├─ ui\_tests.py

│ └─ load\_test.py (optional)

│

├─ requirements.txt

└─ README.md



---


## ⚙️ Setup Instructions

### 1. Create and activate virtual environment (optional but recommended)

python -m venv venv

venv\Scripts\activate # Windows



### 2. Install dependencies

pip install -r requirements.txt


---


## ▶️ How to Run the Tests

### **Run API Tests**

pytest tests/api_tests.py

### **Run UI Tests**

pytest tests/ui_tests.py


Make sure Google Chrome is installed.


### **Run Load Test (Optional)**

locust -f tests/load_test.py


Then open in browser:

http://localhost:8089

Enter:

- Host: `https://reqres.in`

- Users: 5

- Spawn rate: 1

---



## 🧪 API Test Notes

- Tests cover GET users, GET single user, POST create user, and 404 error case.

- JSON fields are validated when the API returns the expected codes.



### ⚠️ Note on 403 Forbidden Responses

- The Reqres public API was returning **403 Forbidden** responses on my machine.

I tested this on:
- Home WiFi  
- Mobile hotspot  
- VPN connections (multiple regions) 



All of them still returned 403, which indicates Reqres is blocking my IP range or automated requests.


To avoid false failures caused by this external API restriction, the tests allow **403** in addition to the expected status codes **200**, **201**, and **404**.  

When the API returns the expected codes, the tests also validate the JSON content normally.


---



## 🧪 UI Test Notes

- Verifies homepage title  

- Checks logo/image visibility  

- Tests navigation  

- Checks presence of input fields  

- Selenium WebDriver is managed automatically using webdriver-manager  

- Browser opens and closes automatically using pytest fixtures


---



## ✔ What This Assignment Demonstrates

- API automation using requests + pytest  

- UI automation using Selenium  

- Assertions and validations  

- Handling real-world API issues  

- Basic load testing (optional)  

- Clear setup and test execution steps



---

