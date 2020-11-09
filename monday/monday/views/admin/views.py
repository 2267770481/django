from flask.views import MethodView
from flask import render_template, request
from monday.public.db_util import mysql
from monday.views.forms.add_cmp_info import AddCmpInfoForm
from monday.views.forms.add_pne_info import AddPneInfoForm


class AddCmpInfo(MethodView):
    def get(self):
        form = AddCmpInfoForm()
        return render_template('add_company.html', form=form)

    def post(self):
        form = AddCmpInfoForm(formdata=request.form)
        if form.validate():
            sql = 'insert into company values(%(name)s, %(location)s)'
            mysql.insert(sql, form.data)
            return 'success'
        else:
            return render_template('add_company.html', form=form)


class AddPneInfo(MethodView):
    def get(self):
        form = AddPneInfoForm()
        return render_template('add_phone.html', form=form)

    def post(self):
        form = AddPneInfoForm(formdata=request.form)
        if form.validate():
            print(form.data)
            sql = 'insert into phone(model, price, company_name) values(%(model)s, %(price)s, %(company)s)'
            mysql.insert(sql, form.data)
            return 'success'
        else:
            return render_template('add_phone.html', form=form)


class FindPhone(MethodView):
    def get(self):
        return render_template('find_phone.html')

    def post(self):
        model = request.form['model']
        try:
            sql = f"""
                       select id, model, price, company_name, location 
                       from phone a, company b where b.name = a.company_name and a.model = %s
                    """
            res = mysql.fetch_one(sql, model)
            print(res)
            return 'success'
        except Exception as e:
            print(e)
            return 'error'
