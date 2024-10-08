from flask import Flask, render_template, jsonify
app = Flask(__name__)

Jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'remote',
        'salary': 'RS 1,0000'
    },
    {
        'id': 2,
        'title': 'Backend',
        'location': 'remote',
        'salary': 'RS 1,0000'
    },
    {
        'id': 3,
        'title': 'Frontend',
        'location': 'onsite',
        'salary': 'RS 1,0000'
    },
    {
        'id': 4,
        'title': 'Data Eng',
        'location': 'remote',
        'salary': '$1,0000'
    },

]

@app.route('/jsonify')
def json():
    return jsonify(Jobs)

@app.route('/')
def hello_world():
    return render_template('index.html', jobs=Jobs)

if __name__ == '__main__':
    app.run(debug=True)