from flask import render_template, flash, redirect, request
from app import app
from app.forms import WordJoinerForm, WordSplitterForm

from sinsandhi import SandhiTool

freq_dic_path = '/data/freq_dic_v2.txt'
stool = SandhiTool(freq_dic_path)


@app.route('/')
@app.route('/index')
def index():
    return redirect('http://nlp-tools.uom.lk/sinsandhi/word_joiner')


@app.route('/word_joiner', methods=['GET', 'POST'])
def word_join():
    form = WordJoinerForm(request.form)
    if request.method == 'POST' and form.validate():
        w1 = form.word1.data
        w2 = form.word2.data
        response = stool.join(w1, w2)
        return render_template('word_joiner.html', form=form, response=response)
    return render_template('word_joiner.html', form=form)


@app.route('/word_splitter', methods=['GET', 'POST'])
def word_split():
    form = WordSplitterForm(request.form)
    if request.method == 'POST' and form.validate():
        w1 = form.word1.data
        response = stool.split(w1)
        return render_template('word_splitter.html', form=form, response=response)
    return render_template('word_splitter.html', form=form)
