from flask import Flask

app = Flask(__name__)


app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")
def hello_world():
	return "hello world3.."


@app.route("/test/<search_query>")
def search(search_query):
	return search_query.upper()



app.run()


