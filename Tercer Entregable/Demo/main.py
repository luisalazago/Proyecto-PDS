from flask import Flask, url_for, render_template, redirect, request
import random

app = Flask(__name__)

# Información
dron1 = ["50m", "Juan David Aycardi", 
		 "5 m/s", "documentos académicos de la facultad de ingeniería"]
dron2 = ["45m", "Jedemías Villarica",
		 "25 m/s", "comida de la cafetería, papas con queso y tocino"]
envio1 = ["4565", "Juan David Aycardi",
		  "documentos académicos", "Entrada Principal",
		  "formatos de despido para el profesor encargado de Sistemas Inteligentes"]
envio2 = ["6969", "Jedemías Villarica",
		  "comida de la cafetería, papas con queso y tocino", "Portería Cedro",
		  "Hambre"]
metros = 100	 

# Variables Globales
fallo = False
usuarios = {"messirve": "Luis"}
contrasenas = {"messirve": "1234"}
usuario_activo = ""

# Funciones Principales
@app.route("/")
def login():
    global fallo
    texto = ""
    if fallo:
        texto = "Por favor digite un usuario existente."
        fallo = False
    return render_template("login.html", content = texto)

# Home
@app.route("/home", methods = ["GET", "POST"])
def home():
	global usuario_activo
	if(usuario_activo == ""): 
		usuario = request.form["usuario"]
		if(usuario in usuarios): usuario_activo = usuarios[usuario]
	if("nombre" in request.form):
		temp = []
		temp.append(request.form["nombre"])
		temp.append(request.form["pedido"])
		temp.append(request.form["lugar"])
		temp.append(request.form["motivo"])
		print("Pedido realizado: {}".format(temp))
	return render_template("home.html", usuario = usuario_activo)

# Drones
@app.route("/drones", methods = ["GET", "POST"])
def drones():
	return render_template("drones.html", usuario = usuario_activo)

@app.route("/drones/1", methods = ["GET", "POST"])
def dron_aumentado1():
	return render_template("dron_aumentado.html", usuario = usuario_activo, numero = "1",
												  info = dron1)

@app.route("/drones/2", methods = ["GET", "POST"])
def dron_aumentado2():
	return render_template("dron_aumentado.html", usuario = usuario_activo, numero = "2",
												  info = dron2)

# Reservas
@app.route("/reservas", methods = ["GET", "POST"])
def reservas():
	return render_template("reserva.html", usuario = usuario_activo)

# Envios
@app.route("/envios", methods = ["GET", "POST"])
def envios():
	return render_template("envios.html", usuario = usuario_activo)

@app.route("/envios/4565", methods = ["GET", "POST"])
def envio_aumentado1():
	return render_template("envio_aumentado.html", usuario = usuario_activo, envio = envio1)

@app.route("/envios/6969", methods = ["GET", "POST"])
def envio_aumentado2():
	return render_template("envio_aumentado.html", usuario = usuario_activo, envio = envio2)

# Rutas
@app.route("/rutas", methods = ["GET", "POST"])
def rutas():
	return render_template("rutas.html", usuario = usuario_activo)

@app.route("/rutas/1", methods = ["GET", "POST"])
def ruta_aumentado():
	global metros
	if(metros >= 0): metros -= random.randint(1, 10)
	else: metros = 0
	return render_template("ruta_aumentado.html", usuario = usuario_activo, metros = metros)

if __name__ == "__main__":
	app.run(debug = True)