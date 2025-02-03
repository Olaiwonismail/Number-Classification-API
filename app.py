from flask import Flask,request,jsonify
from flask_cors import CORS # type: ignore
import requests,math
app= Flask(__name__)


CORS(app)

def is_number(s):
    try:
        float(s)  # Can handle negatives and decimals
        return True
    except ValueError:
        return False

def is_prime(num):
    if num < 2:
        return False
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True



def is_perfect(num):
    if num < 2:
        return False
    sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_of_divisors == num


def is_armstrong(num):
    digits = list(map(int, str(num)))
    power = len(digits)
    return sum(d ** power for d in digits) == num


def get_properties(num):
    properties = []
    if is_armstrong(num):
        properties.append("armstrong")

    if num % 2 == 0:
        properties.append("even")

    else:
        properties.append("odd")
    
    return properties    

def digital_sum(num):
    sum = 0
    list_of_num = list(str(num))
    for x in list_of_num:
        sum+=int(x)
    return sum    

def fun_fact(num):
    try:
        response = requests.get(f'http://numbersapi.com/{num}/math')
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as err:
        return f"Error fetching fun fact: {err}"
    
@app.route('/api/classify-number',methods = ['POST','GET'])
def home():
    # number=371
    number = request.args.get('number')
    if not is_number(number):
        return jsonify({
                        "number": "alphabet",
                        "error": True
                        }), 400
    number = int(number)
    return jsonify({
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties":get_properties(number),
        "digit_sum": digital_sum(number),  
        "fun_fact": fun_fact(number)
    })



if __name__ == '__main__':
    app.run(debug=True)