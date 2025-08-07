from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')


@app.route('/')
def index():
    myVar = "heyo, Marc!"
    myList = [1, 2, 3, 4, 5]
    return render_template('index.html', myVar=myVar, myList=myList)


@app.route('/other')
def other():
    return render_template('other.html')


@app.template_filter('capitalize')
def capitalize_filter(s):
    """Capitalize the first letter of a string."""
    if isinstance(s, str):
        return s.capitalize()
    return s

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
