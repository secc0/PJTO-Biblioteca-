from functools import wraps
from flask import request, jsonify, render_template

def login_usuario():
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            email = request.cookies.get("email")
            if not email:
                return render_template('login.html')
            return f(*args, **kwargs)
        return wrapper
    return decorator


def somente_admin():
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            perfil = request.cookies.get("perfil")
            if perfil != "admin":
                return jsonify({"erro": "Acesso restrito a administradores."}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator
