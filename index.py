from flask import Flask, render_template    #el render_temp sirve para llamar los archivos html

app =  Flask(__name__)          #con esto indico que este archivo es la biblioteca principal y tambien la estoy     asignando a una variable

@app.route('/')                 #con esto definimos la tura para la pagina principal
def home():                     #creamos una funcion que definira que pasara cuando se acceda a la pag principal
    return render_template('home.html')               #esta funcion esta corriendo siempre en el servidor para dar acceso a todo aquel que quiera entrar a la pagina

@app.route('/about')            #creamos una segunda pagina para llevar a la pagina About
def about():
    return render_template('about.html')



if __name__ == '__main__':      #vamos a validar que este archivo sea un archivo de ejecucion continua y no un modul
    app.run(debug=True)         #debug=True es la forma de decir que esta en pruba para no reiniciar cada vez la app