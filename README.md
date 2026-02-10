# Petstore API Automation Tests

This project contains automated API tests for the **Swagger Petstore** service.  
The goal of the project is to demonstrate basic API automation skills using Python and pytest.

---

## 🛠 Tech Stack

- Python
- pytest
- requests

---

## 📁 Project Structure

api-automation-petstore/
├── tests/
│   ├── test_get_pet.py
│   ├── test_create_pet.py
│   ├── test_get_created_pet.py
│   └── test_delete_pet.py
├── requirements.txt
├── README.md

---

## ✅ Covered Test Scenarios

The project covers a full CRUD flow for Pet entity:

1. **GET pet by ID**  
   - Retrieve pet information

2. **POST create pet**  
   - Create a new pet
   - Validate response body

3. **GET created pet**  
   - Verify that the pet was successfully created

4. **DELETE pet**  
   - Remove pet by ID

5. **GET deleted pet**  
   - Verify that deleted pet returns `404 Not Found`

---

## ▶️ How to Run Tests

### 1. Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate

2. Install dependencies 
pip install -r requirements.txt

3. Run all tests
pytest -v

🌐 API Reference

Tests are based on the public Swagger Petstore API:
https://petstore.swagger.io/
