import os
import time
import psycopg2
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#Dane logowania ze zmiennych środowiskowych
DB_HOST = os.environ.get("DB_HOST", "db")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASS = os.environ.get("DB_PASSWORD", "postgres")
DB_NAME = os.environ.get("DB_NAME", "tododb")

