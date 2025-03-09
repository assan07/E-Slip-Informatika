from flask import Flask, render_template, redirect, url_for, request, session, flash, send_from_directory, jsonify
import mysql.connector
from jinja2 import Environment, FileSystemLoader
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key ='123456'

@app.route('/' , methods=['GET', 'POST'])
def login_mahasiswa():
    return render_template('mahasiswa/login_mahasiswa.html')

@app.route('/mahasiswa/register_mahasiswa' , methods=['GET', 'POST'])
def register_mahasiswa():
    return render_template('mahasiswa/register_mahasiswa.html')


if __name__ == '__main__':
    app.run(debug=True)