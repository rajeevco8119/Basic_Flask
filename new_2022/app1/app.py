# Integrate html with flask
# HTTP verb GET and POST
# Jinja 2

from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/pass/<int:score>')
def success(score):
    res = ''
    if score >= 50:
        res = 'PASS'
    else:
        res = 'FAIL'

    exp = {'score':score,'res':res}
    return render_template('result.html', result=exp)


# Result checker HTML page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science) / 4
    return redirect(url_for('success', score=total_score))


if __name__ == '__main__':
    app.run(debug=True)
