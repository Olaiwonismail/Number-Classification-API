"# HNG12-STAGE-1" 
# Number Classification API

## Overview
The **Number Classification API** is a simple RESTful API that takes a number as input and returns interesting mathematical properties about it, along with a fun fact.

## Features
- Checks if the number is **prime**.
- Checks if the number is **perfect**.
- Identifies if the number is an **Armstrong number**.
- Determines whether the number is **even** or **odd**.
- Computes the **digit sum** of the number.
- Fetches a **fun fact** about the number from the [Numbers API](http://numbersapi.com/).

## Technology Stack
- **Python** (Flask)
- **Flask-CORS** for handling cross-origin requests
- **Requests** library for fetching fun facts
- **Deployed on:** [Your Hosting Platform]

## API Endpoint
### **GET /api/classify-number?number=371**
#### Request Parameters
| Parameter | Type  | Required | Description |
|-----------|-------|----------|-------------|
| number    | int   | Yes      | The number to classify |

#### Example Request
```
GET https://your-api-url.com/api/classify-number?number=371
```

#### Example Response (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### Error Response (400 Bad Request)
```json
{
    "number": "alphabet",
    "error": true
}
```

## Setup Instructions
### **Clone the Repository**
```bash
git clone https://github.com/Olaiwonismail/HNG12-Stage-1.git
cd HNG12-Stage-1
```

### **Install Dependencies**
Ensure you have Python installed, then install the required libraries:
```bash
pip install -r requirements.txt
```

### **Run the API Locally**
```bash
python app.py
```


## Resources
- Numbers API: [http://numbersapi.com](http://numbersapi.com)
- Parity (Math): [Wikipedia](https://en.wikipedia.org/wiki/Parity_(mathematics))
- Hire Python Developers: [HNG Tech](https://hng.tech/hire/python-developers)

---


