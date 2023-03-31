from flask import Flask, request, render_template

app = Flask(__name__)

welcome_text = "Congratulations! This is your first containerized APP!!"
@app.route('/')
def index():
    return render_template('home.html',welcome_text=welcome_text)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)