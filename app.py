from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
        return render_template('home.html')

@app.route('/iac')
def iac():
        return render_template('iac.html')

@app.route('/sre')
def sre():
        return render_template('sre.html')

@app.route('/about')
def about():
        return render_template('about.html')


if __name__ == '__main__':
        app.run(debug=True)