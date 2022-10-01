from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, logout_user, current_user

from .forms import SendForm, AssetForm, FilterForm
#update view all pages
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='frontend_page',
    static_folder='css_file'
)


@main_bp.route('/')
@login_required
def index():
    """Main page, displays balance"""
    balance = current_user.get_balance()
    return render_template('index.html', balance=balance)


@main_bp.route('/send', methods=['GET', 'POST'])
@login_required
def send():
    """Provides a form to create and send a transaction"""
    form = SendForm()
    address = current_user.public_key
    if form.validate_on_submit():
        success = current_user.send(form.quantity.data, form.receiver.data, form.note.data)
        return render_template('success.html', success=success)

    # show the form, it wasn't submitted
    return render_template('send.html', form=form, address=address)


@main_bp.route('/nft', methods=['GET', 'POST'])
@login_required
def nft():
    """Provides a form to post and view the certeficate"""
    form = SendForm()
    address = current_user.public_key
    if form.validate_on_submit():
        success = current_user.send(form.quantity.data, form.receiver.data, form.note.data)
        return render_template('success.html', success=success)

    # show the form, it wasn't submitted
    return render_template('nft.html', form=form, address=address)


@main_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """Provides a form to create an asset"""
    form = AssetForm()
    if form.validate_on_submit():
        success = current_user.create(
            form.asset_name.data,
            form.unit_name.data,
            form.total.data,
            form.decimals.data,
            form.default_frozen.data,
            form.url.data
        )

        print(success)
        return redirect(url_for('main_bp.assets'))

    # show the form, it wasn't submitted
    return render_template('create_asset.html', form=form)


@main_bp.route('/transactions', methods=['GET', 'POST'])
@login_required
def transactions():
    """Displays all transactions from the user"""
    form = FilterForm()

    if form.validate_on_submit():
        txns = current_user.get_transactions(form.substring.data)
    else:
        txns = current_user.get_transactions("")

    return render_template('transactions.html', txns=txns, form=form)


@main_bp.route('/assets', methods=['GET', 'POST'])
@login_required
def assets():
    """Displays all assets owned by the user"""
    form = FilterForm()

    if form.validate_on_submit():
        assets_list = current_user.get_assets(form.substring.data)
    else:
        assets_list = current_user.get_assets("")

    return render_template('assets.html', assets=assets_list, form=form)


@main_bp.route('/mnemonic')
@login_required
def mnemonic():
    """Displays the recovery passphrase"""
    passphrase = current_user.passphrase
    return render_template('mnemonic.html', passphrase=passphrase)


@main_bp.route('/logout')
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))
