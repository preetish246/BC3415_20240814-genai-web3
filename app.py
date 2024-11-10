from flask import Flask,render_template,request
import google.generativeai as genai
import os
import textblob

#os.environ["MAKERSUITE_API_KEY] = ""
api = "AIzaSyCFIL-2qRWHrUqzyf_TN3A5IKQsVgB2zHg"
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/ai_agent", methods=["GET","POST"])
def ai_agent():
    q = "Tell me a joke about Singapore"
    r = model.generate_content(q)
    return(render_template("ai_agent_reply.html",r=r.text))

@app.route("/prediction", methods=["GET","POST"])
def prediction():
    return(render_template("index.html"))

@app.route("/paynow", methods=["GET","POST"])
def paynow():
    return(render_template("paynow.html"))

@app.route("/SA", methods=["GET","POST"])
def SA():
    return(render_template("SA.html"))

@app.route("/SA_reply", methods=["GET","POST"])
def SA_reply():
    q = request.form.get("q")
    r = textblob.TextBlob(q).sentiment
    return(render_template("SA_reply.html",r=r))

if __name__ == "__main__":
    app.run()