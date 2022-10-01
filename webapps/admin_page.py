from algosdk import mnemonic
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import LoginManager, current_user, login_user

from .algodand import create_account
from .forms import LoginForm
from .models import User

login_manager = LoginManager()

auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='frontend_page',
    static_folder='static'
)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Default login page"""
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.index'))

    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User(passphrase=form.passphrase.data)
            login_user(user)
            return redirect(url_for('main_bp.index'))
        except Exception as err:
            flash(err)
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """Generates a user account and shows its passphrase"""
    passphrase = create_account()
    user = User(passphrase=passphrase)
    login_user(user)
    return render_template('mnemonic.html', passphrase=passphrase)


@login_manager.user_loader
def load_user(user_id):
    """User load logic"""
    return User(mnemonic.from_private_key(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to login page"""
    return redirect(url_for('auth_bp.login'))
