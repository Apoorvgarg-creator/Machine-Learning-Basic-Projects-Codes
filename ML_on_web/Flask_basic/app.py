from flask import Flask, render_template, request, redirect

# __name__ == __main__
app = Flask(__name__)
# app is a master variable
friends = ['Prateek','Jatin','Garima']


num = 5

@app.route('/')
def hello():
    # return "Hello Apoorv to flask community, Yo!!" + " WOW WOW"
    return render_template("index.html",my_friends = friends,number = num)

@app.route('/about')
def about():
    return "<h1> Apoorv is learning Machine learning</h1>"

@app.route("/home")
def home():
    return redirect('/')

@app.route('/submit', methods = ['POST'])
def submit_data():
    if request.method == 'POST':
        # name = request.form['username']
        # no1 = int(request.form['no1'])
        # no2 = int(request.form['no2'])
        f = request.files['userfile']
        # print(f)
        f.save(f.filename)
    # return "<h1> Hello {} !!</h1>".format(name)
    # return "<h1> Sum --> {} </h1>".format(no1+no2)


if __name__ == '__main__':
    # app.debug = True
    app.run(debug = True)
