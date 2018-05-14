# course: Databases
# assignment: Project 2
# name: Carlos Calderon , Marlon Fuentes
# description: module that has the methods involved in customer management
import psycopg2
from config import config


def update_paciente(id, idprofesion, nombre, apellido, dpi, sexo, telefono, correo, fechanacimiento, foto,
                    usuariotwitter, pagomedicinas=0):
    """ update vendor name based on the vendor id """
    sql = """ UPDATE paciente
                SET 
                idprofesion = %s,
                nombre = %s,
                apellido = %s,
                dpi = %s,
                sexo = %s,
                telefono = %s,
                correo = %s,
                fechanacimiento= %s,
                foto= %s,
                usuariotwitter= %s
                WHERE id = %s"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (idprofesion, nombre, apellido, dpi, sexo, telefono, correo, fechanacimiento, foto,
                          usuariotwitter, id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


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


def get_paciente(filter, searchterm):
    sql = """select * from paciente where """ + filter + """ LIKE '%""" + searchterm + """%'"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return data


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


def delete_patient(part_id):
    """ delete part by part id """
    conn = None
    rows_deleted = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("DELETE FROM paciente WHERE id = %s", (part_id,))
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted


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

def profesion_masconsultas():
    sql = """
    select count(paciente.id),profesion.tipo from profesion
    inner join paciente on paciente.idprofesion=profesion.id
    inner join consulta on consulta.idpaciente=paciente.id
    group by profesion.tipo
    order by count(paciente.id) desc
    limit 5
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        lista1 = []
        lista2 = []
        for i in data:
            lista1.append(i[0])
            lista2.append(i[1])

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return lista1,lista2

def profesion_mascompras():
    sql = """
    select profesion.tipo,sum(pagomedicinas) from paciente
inner join profesion on paciente.idprofesion=profesion.id
group by idprofesion,profesion.tipo
order by sum(pagomedicinas) desc
limit 5
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        lista1 = []
        lista2 = []
        for i in data:
            lista1.append(i[0])
            lista2.append(i[1])

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return lista1,lista2

def medicina_mascomprada():
    sql = """
    select medicina.nombre,compra.idmedicina,sum(compra.cantidad) from compra
inner join medicina on compra.idmedicina=medicina.id
group by idmedicina,medicina.nombre
order by sum(cantidad) desc
limit 5
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        lista1 = []
        lista2 = []
        for i in data:
            lista1.append(i[0])
            lista2.append(i[1])

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return lista1,lista2

def meses():
    sql = """
    select date_part('month', fecha),sum(compra.cantidad) from compra
group by date_part('month', fecha)
order by sum(cantidad) desc
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        lista1 = []
        lista2 = []
        for i in data:
            lista1.append(int(i[0]))
            lista2.append(i[1])

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return lista1,lista2

def meses_consultas():
    sql = """
    select date_part('month', fecha),count(date_part('month', fecha)) from consulta
group by date_part('month', fecha)
order by count(date_part('month', fecha)) desc
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        lista1 = []
        lista2 = []
        for i in data:
            lista1.append(int(i[0]))
            lista2.append(i[1])

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return lista1,lista2

def departamentos():
    sql = """
    select count(idpaciente),departamento.nombre from direccion
inner join departamento on departamento.id= direccion.iddepartamento
group by departamento.id 
order by count(idpaciente) desc
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        lista1 = []
        lista2 = []
        for i in data:
            lista1.append(i[0])
            lista2.append(i[1])

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return lista1,lista2

"""lista1,lista2 = departamentos()
for i in lista1:
    print(i)
print("---")
for i in lista2:
    print(i)"""
# print(get_profession('Arquitectura','Arquitectur'))

# print(get_idpaciente())
# print (insert_patient(33,7,'Carla','Ovalle',34567,'F',31600978,'cas15151@uvg.edu.gt','1988-03-06','ff','@sam',0))
