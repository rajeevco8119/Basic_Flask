from flask import Flask,request,redirect,url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome'


@app.route('/pass/<int:score>')
def success(score):
    return "The person fail and marks are "+str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "The person fail and marks are "+str(score)


@app.route('/results/<int:marks>')
def results(marks):
    result = ''
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result,score=marks))


if __name__ == '__main__':
    app.run(debug=True)
