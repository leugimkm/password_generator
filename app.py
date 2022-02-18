import random
from flask import Flask, render_template, request
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits

app = Flask(__name__)
LONGITUD_MINIMA = 8


def generar_password(
    longitud: int = None,
    simbolos: bool = None,
    digitos: bool = None,
    mayusculas: bool = None,
    minusculas: bool = None,
) -> str:
    """Genera un password aleatorio

    :param longitud: longitud del password
    :longitud type: int
    :param simbolos: incluir simbolos
    :simbolos type: bool
    :param digitos: incluir digitos
    :digitos type: bool
    :param mayusculas: incluir mayusculas
    :mayusculas type: bool
    :param minusculas: incluir minusculas
    :minusculas type: bool
    :return: password aleatorio
    :rtype: str
    """
    simbolos = "~`!@#$%^&*()_-+={[}]|\:;<,>.?/\"'" if simbolos else ""
    digitos = digits if digitos else ""
    mayusculas = ascii_uppercase if mayusculas else ""
    minusculas = ascii_lowercase if minusculas else ""
    caracteres = simbolos + digitos + mayusculas + minusculas
    if not caracteres:
        caracteres = ascii_letters
    return "".join(random.choices(caracteres, k=longitud))


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        longitud = request.form.get("longitud")
        simbolos = request.form.get("simbolos")
        digitos = request.form.get("digitos")
        mayusculas = request.form.get("mayusculas")
        minusculas = request.form.get("minusculas")
        password = generar_password(
            longitud=int(longitud),
            simbolos=bool(simbolos),
            digitos=bool(digitos),
            mayusculas=bool(mayusculas),
            minusculas=bool(minusculas),
        )
        return render_template('index.html', password=password)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
