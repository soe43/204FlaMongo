from flask import Flask
import db as d

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("mongo.html")

@app.route("/submitted")
def submitted():
    num=request.form["input"]
    choice=request.form["dropdown"]
    toReturn=[]
    if choice=="femalelte":
        toReturn=femalePopLessThanEqualTo(num)
    elif choice=="malegte":
        toReturn=malePopGreaterThanEqualTo(num)
    else:
        toReturn=popLessThan(num)
    return render_template("submitted.html",results=toReturn)


if __name__=="__main__":
    app.debug=True
    app.run()
