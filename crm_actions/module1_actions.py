# course: Databases
# assignment: Project 2
# name: Carlos Calderon , Marlon Fuentes
# description: module that has the methods involved in customer management
import psycopg2
from config import config


def insert_patient(id, idprofesion, nombre, apellido, dpi, sexo, telefono, correo, fechanacimiento, foto,
                   usuariotwitter, pagomedicinas=0):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO paciente(id, idprofesion, nombre, apellido, dpi, sexo, telefono, correo, fechanacimiento, foto,
                   usuariotwitter, pagomedicinas)
             VALUES(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s,
                   %s,%s) RETURNING id;"""
    conn = None
    vendor_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql,
                    (id, idprofesion, nombre, apellido, dpi, sexo, telefono, correo, fechanacimiento, foto,
                     usuariotwitter, pagomedicinas,))
        # get the generated id back
        vendor_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return vendor_id


def get_profession(nombre, tipo):
    """ query data from the profesion table """
    sql = """SELECT id FROM profesion WHERE nombre = %s AND tipo = %s """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql,
                    (nombre, tipo))
        row = cur.fetchone()[0]
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return row


def get_idpaciente():
    """ query data from the paciente table """
    sql = """SELECT max(id) FROM paciente"""
    conn = None
    row = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()[0]
        print(row)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return row + 1


#print(get_profession('Arquitectura','Arquitectur'))

#print(get_idpaciente())
# print (insert_patient(33,7,'Carla','Ovalle',34567,'F',31600978,'cas15151@uvg.edu.gt','1988-03-06','ff','@sam',0))
