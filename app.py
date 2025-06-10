from flask import Flask, render_template, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Placeholder routes for now (optional)
@app.route('/games')
def games():
    return render_template_string("<h1>Games Page Coming Soon</h1>")

@app.route('/tips')
def tips():
    return render_template_string("<h1>Tips Page Coming Soon</h1>")

@app.route('/highlights')
def highlights():
    return render_template_string("<h1>Highlights Page Coming Soon</h1>")

@app.route('/contact')
def contact():
    return render_template_string("<h1>Contact Page Coming Soon</h1>")

if __name__ == '__main__':
    app.run()
