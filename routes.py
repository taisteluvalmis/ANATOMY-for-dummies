from app import app
from flask import redirect, render_template, request
import users, courses, stats

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    if not users.login(username, password):
        return render_template('error.html', message='Wrong username or password')
    
    user_id = session.get('user_id')
    user_role = users.get_user_role(user_id)
    if user_role:
        session['role'] = user_role
    return redirect('/login')

@app.route('/logout')
def logout():
    users.logout()
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        username = request.form['username']
        if len(username) < 1 or len(username) > 20:
            return render_template('error.html', message='Username must have 1-20 characters')

        password1 = request.form['password1']
        password2 = request.form['password2']
        if password1 != password2:
            return render_template('error.html', message='Passwords do not match')
        if password1 == '':
            return render_template('error.html', message='Password is empty')

        role = request.form['role']
        if role not in ('1', '2'):
            return render_template('error.html', message='Unknown user role')

        if not users.register(username, password1, role):
            return render_template('error.html', message='Registartion failed, make sure to check username and password')
        return redirect('/')

# Add new course
@app.route('/add_course', methods=['POST'])
def add_course():


# Add new lesson
@app.route('/add_lesson', methods=['POST'])
def add_lesson():

# Sign up for the course
@app.route('/enroll_course', methods=['POST'])
def enroll_course():




