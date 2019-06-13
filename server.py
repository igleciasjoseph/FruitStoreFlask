from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods = ['POST'])
def checkout():
    svalue = request.form[('strawberry')]
    rvalue = request.form[('raspberry')]
    avalue = request.form[('apple')]
    fname = request.form[('first_name')]
    lname = request.form[('last_name')]
    sid = request.form[('student_id')]
    count = int(svalue) + int(rvalue) + int(avalue)
    checkout = (f"Charging {fname}  {lname} for {count} fruits")
    print(request.form)
    return render_template("checkout.html", svalue = svalue, rvalue = rvalue, avalue = avalue, fname = fname, lname = lname, sid = sid, checkout = checkout)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=False)
