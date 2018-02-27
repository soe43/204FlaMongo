from flask import Flask, render_template, request
import utils.db as d

app=Flask(__name__)

#c=d.connection
#c.drop_database("gaoJsoeW")
#d.createDB()

@app.route("/")
def home():
    return render_template("mongo.html")

@app.route("/submitted", methods=["POST", "GET"])
def submitted():
    if request.method=="POST":
        num=request.form["input"]
        choice=request.form["dropdown"]
        message=""
        toReturn=[]
        if choice=="femalelte":
            toReturn=d.femalePopLessThanEqualTo(int(num))
            message="You searched for ages where the number of females is less than or equal to "+num
        elif choice=="malegte":
            toReturn=d.malePopGreaterThanEqualTo(int(num))
            message="You searched for ages where the number of males is greater than or equal to "+num
        else:
            toReturn=d.popLessThan(int(num))
            message="You searched for ages where the number of females OR the number of males is less than "+num
        return render_template("submitted.html",results=toReturn, show=message)
    else:
        return render_template("mongo.html")


if __name__=="__main__":
    app.debug=True
    app.run()
