from flask import Flask, jsonify,render_template
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)

engine = create_engine('postgresql://postgres:admin@localhost:5432/postgres')

results = engine.execute("""SELECT * FROM public.\"TEST_DATA\" """).fetchall()

new = []
for i in results:
    a = {"id":i[0],"state":i[1],"abbr":i[2],"poverty":i[3],"povertyMoe":i[4],"age":i[5],"ageMoe":i[6],"income":i[7],"incomeMoe":i[8],"healthcare":i[9],"healthcareLow":i[10],"healthcareHigh":i[11],"obesity":i[12],"obesityLow":i[13],"obesityHigh":i[14],"smokes":i[15],"smokesLow":i[16],"smokesHigh":i[17]}
    new.append(a)




@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/data")
def custom_f1():
    return jsonify(new)


if __name__ == '__main__':
    app.run(debug=True)
