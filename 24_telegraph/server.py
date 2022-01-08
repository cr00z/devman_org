from flask import Flask, render_template, request, make_response, redirect, abort
import json
import os
import random
from functools import wraps


MOVED_PERMANENTLY = 301
UNAUTHORIZED = 401
NOT_FOUND = 404


app = Flask(__name__)


def get_random_hex(bits):
    return '{0:x}'.format(random.getrandbits(bits))


def get_or_create_auth_token(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        auth_token = request.cookies.get('auth_token') or get_random_hex(128)
        response = make_response(func(*args, **kwargs, auth_token=auth_token))
        response.set_cookie('auth_token', auth_token)
        return response
    return decorated_function


def write_article(json_object, filepath):
    os.makedirs('articles', exist_ok=True)
    with open(filepath, 'w') as file_obj:
        json.dump(json_object, file_obj)


def read_article(filepath):
    try:
        with open(filepath, 'r') as file_obj:
            return json.load(file_obj)
    except FileNotFoundError:
        return None


def render_form(form_target='/', article_info=None):
    return render_template(
        'form.html',
        form_target=form_target,
        article_info=article_info
    )


def render_article(article_uid, article_info, edit_mode):
    article_info['body'] = article_info['body'].split('\n')
    return render_template(
        'article.html',
        article_uid=article_uid,
        article_info=article_info,
        edit_mode=edit_mode
    )


@app.route('/')
@get_or_create_auth_token
def show_new_article_form(auth_token=None):
    return render_form()


@app.route('/', methods=['POST'])
@get_or_create_auth_token
def save_new_article(auth_token=None):
    article_uid = get_random_hex(128)
    article_info = {
        'auth_token': auth_token,
        'header': request.form['header'],
        'signature': request.form['signature'],
        'body': request.form['body']
    }
    write_article(article_info, os.path.join('articles', article_uid))
    return redirect("/article/{}".format(article_uid), code=MOVED_PERMANENTLY)


@app.route('/edit/<article_uid>')
@get_or_create_auth_token
def show_editing_article_form(article_uid, auth_token=None):
    article_info = read_article(os.path.join('articles', article_uid))
    if auth_token == article_info['auth_token']:
        return render_form(
            '/article/{}'.format(article_uid),
            article_info
        )
    else:
        abort(UNAUTHORIZED)


@app.route('/article/<article_uid>')
@get_or_create_auth_token
def show_existing_article(article_uid, auth_token=None):
    existing_article = read_article(os.path.join('articles', article_uid))
    if existing_article:
        edit_mode = (existing_article['auth_token'] == auth_token)
        return render_article(article_uid, existing_article, edit_mode)
    else:
        abort(NOT_FOUND)


@app.route('/article/<article_uid>', methods=['POST'])
@get_or_create_auth_token
def save_existing_article(article_uid, auth_token=None):
    article_info = {
        'auth_token': auth_token,
        'header': request.form['header'],
        'signature': request.form['signature'],
        'body': request.form['body']
    }
    existing_article = read_article(os.path.join('articles', article_uid))
    if auth_token == existing_article['auth_token']:
        write_article(article_info, os.path.join('articles', article_uid))
        return redirect("/article/{}".format(article_uid), code=MOVED_PERMANENTLY)
    else:
        abort(UNAUTHORIZED)


if __name__ == "__main__":
    app.run()
