from aplicacion.config.mysqlconnection import connectToMySQL #siempre importar la conección con la base de datos
from flask import flash
from aplicacion import app
from aplicacion.models.usuario import Usuario

class Programa:

    base_datos="prueba_1"

    def __init__(self, data):
        self.id=data['id']
        self.titulo = data['titulo']
        self.canal = data['canal']
        self.fecha = data['fecha']
        self.descripcion = data['descripcion']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuario_id = data['usuario_id']
        self.usuario = []
    
    #MOSTRAR TODAS LAS RECETAS CON SUS USUARIOS
    @classmethod
    def todos_los_programas(cls):
        consulta = "SELECT * FROM programas JOIN usuarios ON programas.usuario_id = usuarios.id"
        resultado= connectToMySQL (cls.base_datos).query_db(consulta)
        # print(resultado, "RESULTADO EN DIRECCIONARIO")
        todos_los_programas_con_usuarios = []
        for programa in resultado:
            objeto_programa = cls(programa)
            objeto_programa.usuario.append(Usuario(programa))
            todos_los_programas_con_usuarios.append(objeto_programa)
        # print (todos_los_programas_con_usuarios, "IMPRIMIENDO DE TODOS LOS PROGRAMAS (OBJETOS)EN CLASSMETHOD")
        return todos_los_programas_con_usuarios
        

    #insertar un programa:
    @classmethod
    def crear_programa(cls,data):
        consulta= "INSERT INTO programas (titulo, canal, fecha, descripcion, created_at, updated_at, usuario_id) VALUES (%(titulo)s, %(canal)s, %(fecha)s, %(descripcion)s, NOW(), NOW(), %(usuario_id)s);" 
        resultado = connectToMySQL(cls.base_datos).query_db(consulta,data)
        return resultado

    #leer UN SOLO programa:
    @classmethod
    def leer_programa(cls, data):
        # ACA LO HICE DISTINTO PORQUE piden poner quien la postio. ENTONCES EL usuario.id lo utilizaré en esta consulta para que me de el nombre completo del usuario que la postio.
        consulta= """SELECT programas.id, programas.titulo, programas.canal, programas.fecha, programas.descripcion, programas.created_at, programas.updated_at, concat(usuarios.nombre," ", usuarios.apellido ) AS usuario_id  FROM programas JOIN usuarios ON programas.usuario_id = usuarios.id WHERE programas.id = %(id)s;"""
        resultado= connectToMySQL (cls.base_datos).query_db(consulta,data)
        return cls(resultado[0])

    #EDITAR UN PROGRAMA
    @classmethod
    def editar_programa(cls, data):
        consulta="""UPDATE programas SET titulo = %(titulo)s, canal = %(canal)s, fecha = %(fecha)s, descripcion = %(descripcion)s, updated_at = NOW() WHERE id = %(id)s; """
        resultado= connectToMySQL (cls.base_datos).query_db(consulta,data)
        return resultado

    #ELIMINAR UN PROGRAMA
    @classmethod
    def eliminar_programa(cls,data):
        consulta = "DELETE FROM programas WHERE id=%(id)s;"
        resultado= connectToMySQL (cls.base_datos).query_db(consulta,data)
        return resultado
    
    @staticmethod
    def validacion_programa(form_programa):
        is_valid = True # asumimos que esto es true
        if len(form_programa['titulo']) < 3:
            flash("El título debe contar con al menos 3 caracteres")
            is_valid = False
        if len(form_programa['canal']) < 3:
            flash("El canal debe contar con al menos 3 caracteres")
            is_valid = False
        if len(form_programa['fecha']) < 10:
            flash("Selecciona una fecha")
            is_valid = False
        if len(form_programa['descripcion']) < 3:
            flash("La descripcion debe contar con al menos 3 caracteres")
            is_valid = False
        return is_valid