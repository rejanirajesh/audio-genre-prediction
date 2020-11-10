from project import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from project.models import User
from project.forms import LoginForm, RegistrationForm


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/logout')
def logout():
    logout_user()
    flash("Logged out")
    return redirect(url_for('home.html'))


@app.route('/login', methods=['POST'])
def login():

    form = LoginForm()
    if request.method == "POST":
        print(form.email.data)
        print(form.password.data)
        # if form.validate_on_submit():
        #     print(form.password.data)
        #     print(form.email.data)

        # user = User.query.filter_by(enail=form.email.data).first()

        # if user.check_password(form.password.data) and user is not None:

        #     login_user(user)
        #     flash("Logged in successfully")

        #     next = request.args.get('next')

        #     if next == None or not next[0] == '/':
        #         next = url_for('upload')

        #     return redirect(next)

    return render_template('home.html', form=form)
    # return render_template('upload.html')
    # return redirect(url_for('upload'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST':
        print(form.email.data)
        print(form.password.data)
        user = User(email=form.email.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()

        # if form.validate_on_submit():
        #     print(form.password.data)
        #     print(form.email.data)

        # user = User(email=form.email.data,
        #             # username=form.username.data,
        #             password=form.password.data)

        # db.session.add(user)
        # db.session.commit()
        # flash("Thanks for registration")
        # return redirect(url_for('upload'))
        return redirect('/upload')

    return render_template('register.html', form=form)

    # db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
