from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'New York',
    'salary': '$150,000'
}, {
    'id': 2,
    'title': 'Data scientist',
    'location': 'New Delhi',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'DevOps Engineer',
    'location': 'Bengaluru',
}, {
    'id': 4,
    'title': 'Cloud Engineer',
    'location': 'Remote',
    'salary': 'Rs. 21,00,0000'
}, {
    'id': 5,
    'title': 'Full-Stack Developer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
}, {
    'id': 6,
    'title': 'Python Developer',
    'location': 'Pune',
    'salary': 'Rs. 8,00,000'
}]


@app.route("/")
def hello_career():
  return render_template("home.html", jobs=JOBS, company='sa')


@app.route("/api/jobs")
def jobs_return():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
