from flask import Flask
from flask import render_template
from flask import session, redirect, url_for, escape, request

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

@app.route('/hello/<name>')
def parameter_example(name):
    app.logger.debug('Sending a greetung to %s', name)
    return 'Hello ' + name

@app.route('/hello')
def template_example():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)


