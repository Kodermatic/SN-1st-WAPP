from flask import Flask, render_template
import datetime

app = Flask(__name__)     #to je aplikacija

@app.route("/")
def index():
  trenutni_cas = datetime.datetime.now() 
  return f"<h1>Moja prva stran.</h1> <br> Trenutni čas je: {trenutni_cas}"

@app.route("/about")
def on_about():
  #preberi file
  with open ("./templates/index2.html") as html_datoteka:
    vsebina = html_datoteka.read()
  return vsebina

@app.route("/kontakt")
def on_kontakt():
  #render template prebere file iz mape "templates" 
  return render_template("index.html")

if __name__ == "__main__":
  app.run()