from flask import Flask, render_template
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    
