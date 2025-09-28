from flask import Flask, render_template, request, redirect, url_for
from app_imc import recomendacion, calcular_imc
from coneccion_bd import obtener_coneccion
app= Flask(__name__)
 
@app.route('/')
def inicio():
    habilidades = [{"habilidad":"html", "icono": "html", "description": "Actualmente cuento con los conocimientos básicos para el desarrollo de una página web utilizando el HTML, así mismo como organizar el código, el manejo de los selectores, títulos, párrafos, clases, etc. Aún me encuentro en proceso de formación pero espero ir mejorando mis habilidades y aplicar mis conocimientos."},
                   {"habilidad":"css","icono": "css", "description": "Además, con CSS eh aprendido a darle diferentes estilos a la página web, tales como el tamaño, color y tipo de letra, también a los contenedores, imágenes, cajas de texto y demás. Cómo también mejorar el aspecto visual del contenido de la página tanto para computadores como dispositivos móviles."},
                   {"habilidad":"python", "icono": "python", "description": "Y finalmente con el lenguaje de Python, estoy aprendiendo a manejar su sintaxis y sus funciones, como lo son: Operadores, Strings, Listas, Tuplas, Funciones, Sets, Diccionarios, Clases y etc...Y también estoy aprendiendo a como enlazar Python con el HTML. El aprendizaje requiere tiempo, pero con disciplina y esfuerzo se puede lograr"}
    ]
    return render_template('index.html', index=True, habilidades=habilidades)

@app.route('/contacto')
def contacto():

    obtener_coneccion()
    return render_template('contacto.html', contacto=True)

@app.route('/contactar', methods=["POST"])
def procesar_contacto():
    nombre= request.form['nombre']
    celular= request.form['celular']
    email= request.form['email']
    mensaje = request.form['mensaje']
    return f'Mensaje recibido de {nombre} con celular {celular}, Gmail {email} y un mensaje diciendo "{mensaje}"'

@app.route('/acerca')
def nosotros():
    return render_template('acerca.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/imc', methods = ['GET','POST'])
def imc():
    if request.method=='POST':
        peso = float(request.form.get('peso'))
        altura = float(request.form.get('altura'))
        imc=(calcular_imc(peso,altura))
        res = recomendacion(imc)
        return render_template('imc.html',  imc=f'{imc:.2f}', observaciones=res, formulario=False, su_imc=True)
    return render_template('imc.html', observaciones=None, formulario=True, su_imc=None)

categorias = ['Deportivos','Casuales','Elegantes','Colegiales','Abuelitos']
marcas = ['Croydon','Calzatodo','Gomosos','Bubbles Gummers']

@app.route('/tienda')
def tienda():
    categoria=categorias
    marca=marcas
    return render_template('tienda.html', categorias=categoria, marcas=marca)

if __name__=="__main__":
    app.run(debug=True)