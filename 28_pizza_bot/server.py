from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.model.form import InlineFormAdmin
from flask_basicauth import BasicAuth
from flask import redirect

from base import app, db
from models import Items, Choices


basic_auth = BasicAuth(app)


@app.route('/')
def redirect_to_admin():
    return redirect('/admin')


class ChoicesInlineModelForm(InlineFormAdmin):
    column_labels = {'title': 'Название', 'price': 'Цена'}

    def __init__(self):
        return super(ChoicesInlineModelForm, self).__init__(Choices)


class ItemsView(ModelView):
    column_auto_select_related = True
    inline_models = (ChoicesInlineModelForm(),)
    column_labels = {'title': 'Название', 'description': 'Описание'}
    column_searchable_list = ('title',)
    column_editable_list = ('description',)


admin = Admin(app, name='Пиццерия')
admin.add_view(ItemsView(Items, db.session, name='Каталог'))
