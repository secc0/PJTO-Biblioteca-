from functools import wraps
from flask import request, jsonify, render_template, redirect, url_for, session

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user' not in session:         
            return redirect(url_for('login'))
        return f(*args, **kwargs)          
    return wrapper

def somente_admin():
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if session.get("perfil") != "admin":
                return jsonify({"erro": "Acesso restrito a administradores."}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator


