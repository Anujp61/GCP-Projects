from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Hello, World! Welcome to Flask."

# Route with dynamic URL
@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name.capitalize()}! Welcome to Flask."

# JSON API route
@app.route('/api/data')
def api_data():
    return jsonify({
        "message": "This is an example JSON response.",
        "status": "success"
    })

# HTML template route (requires a templates folder with 'index.html')
@app.route('/html')
def render_html():
    return render_template('index.html')

# Form handling route
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Form submitted! Hello, {name.capitalize()}!"
    return '''
    <form method="post">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Submit">
    </form>
    '''

# Custom error handling
@app.errorhandler(404)
def page_not_found(e):
    return "Oops! Page not found. Try again.", 404

if __name__ == '__main__':
    app.run(debug=True)
