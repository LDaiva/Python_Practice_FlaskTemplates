from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {'name': 'Jonas',
     'surname': 'Jonikas'
     },
    {'name': 'Petras',
     'surname': 'Petrikas'
    },
    {'name': 'Kostas',
     'surname': 'Kostukas'
    }
]


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', nname=name, world='World', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
