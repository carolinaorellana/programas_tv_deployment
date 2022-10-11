from aplicacion import app
from flask import render_template, redirect, request, session, flash
from aplicacion.models.programa import Programa

#plantilla para visualizar la pagina de crear programa
@app.route("/programas/nuevo")
def plantilla_nuevo_programa():
    if session['login']==True:
        return render_template("nuevo_programa.html")
    else:
        return redirect ('/')

#ruta que crea el nuevo programa
@app.route("/crear_programa", methods=['POST'])
def crear_programa():
    if not Programa.validacion_programa(request.form):
        return redirect("/programas/nuevo")
    data={
        "titulo": request.form['titulo'],
        "canal": request.form['canal'],
        "fecha": request.form['fecha'],
        "descripcion": request.form['descripcion'],
        "usuario_id": request.form['usuario_id'],
    }
    nuevo_programa=Programa.crear_programa(data)
    return redirect(f"/programas/{session['usuario_id']}")

#ruta que renderiza la plantilla para editar un progrma
@app.route("/programas/editar/<int:id>")
def plantilla_editar_programa(id):
    if session['login']==True:
        data={
            "id":id
        }
        un_programa=Programa.leer_programa(data)
        return render_template("editar_programa.html", un_programa=un_programa)
    else:
        return redirect ('/')

@app.route("/editar_programa", methods=['POST'])
def editar_programa():
    if not Programa.validacion_programa(request.form):
        return redirect(f"/programas/editar/{request.form['id']}")
    data={
        "titulo": request.form['titulo'],
        "canal": request.form['canal'],
        "fecha": request.form['fecha'],
        "descripcion": request.form['descripcion'],
        "id": request.form['id'],
    }
    Programa.editar_programa(data)
    return redirect(f"/programas/{session['usuario_id']}")

#ruta para ver un solo programa
@app.route("/programas/ver/<int:id>")
def ver_programa(id):
    if session['login']==True:
        data={
            "id":id
        }
        un_programa=Programa.leer_programa(data)
        return render_template("ver_programa.html", un_programa=un_programa)
    else:
        return redirect ('/')

#ruta para eliminar un programa:
@app.route("/programas/eliminar/<int:id>")
def eliminar_programa(id):
    data={
        "id":id
    }
    Programa.eliminar_programa(data)
    return redirect(f"/programas/{session['usuario_id']}")