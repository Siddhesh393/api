from flask import Flask, request, jsonify
import string

app = Flask(__name__)

# Function to find the highest lowercase alphabet in an array
def highest_lowercase_alphabet(arr):
    lower_case_letters = [char for char in arr if char.islower()]
    return max(lower_case_letters) if lower_case_letters else None

@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        data = request.get_json()

        # Extracting the required fields from the JSON data
        status = data.get('status')
        user_id = data.get('user_id')
        college_email = data.get('college_email')
        college_roll = data.get('college_roll')
        numbers_array = data.get('numbers_array')
        alphabets_array = data.get('alphabets_array')

        # Finding the highest lowercase alphabet
        highest_lower = highest_lowercase_alphabet(alphabets_array)

        response = {
            'status': status,
            'user_id': user_id,
            'college_email': college_email,
            'college_roll': college_roll,
            'numbers_array': numbers_array,
            'alphabets_array': alphabets_array,
            'highest_lowercase': highest_lower
        }
        return jsonify(response), 200

    elif request.method == 'GET':
        operation_code = 'OPERATION_12345'
        return jsonify({'operation_code': operation_code}), 200

if __name__ == '__main__':
    app.run(debug=True)
