from crm_actions.module1_actions import profesion_masconsultas, profesion_mascompras, medicina_mascomprada, meses, \
    meses_consultas, departamentos
import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in('Carlosc23', 'rYB0EWokMlsjOUMSRtHS')  # Replace the username, and API key with your credentials.


def graph1():
    lista2, lista1 = profesion_masconsultas()

    labels = lista1
    values = lista2
    print(labels)
    print(values)

    trace = go.Pie(labels=labels, values=values)
    data = [trace]
    layout = go.Layout(title='Profesiones con mas consultas medicas', width=800, height=640)
    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, filename='Graphic1.png')
    from IPython.display import Image
    Image('Graphic1.png')


def graph2():
    lista1, lista2 = profesion_mascompras()
    labels = lista1
    values = lista2
    print(labels)
    print(values)

    trace = go.Pie(labels=labels, values=values)
    data = [trace]
    layout = go.Layout(title='Profesiones con mas compras de medicina', width=800, height=640)
    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, filename='Graphic2.png')
    from IPython.display import Image
    Image('Graphic2.png')


def graph3():
    lista1, lista2 = medicina_mascomprada()
    labels = lista1
    values = lista2
    print(labels)
    print(values)

    trace = go.Pie(labels=labels, values=values)
    data = [trace]
    layout = go.Layout(title='Medicinas más compradas', width=800, height=640)
    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, filename='Graphic3.png')
    from IPython.display import Image
    Image('Graphic3.png')


def graph4():
    lista1, lista2 = meses()
    labels = lista1
    values = lista2
    print(labels)
    print(values)

    trace = go.Bar(x=labels, y=values)
    data = [trace]
    layout = go.Layout(title='Cantidad de medicinas compradas en cada mes', width=800, height=640)
    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, filename='Graphic4.png')
    from IPython.display import Image
    Image('Graphic4.png')


def graph5():
    lista1, lista2 = meses_consultas()
    labels = lista1
    values = lista2
    print(labels)
    print(values)

    trace = go.Bar(x=labels, y=values)
    data = [trace]
    layout = go.Layout(title='Cantidad de consultas en cada mes', width=800, height=640)
    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, filename='Graphic5.png')
    from IPython.display import Image
    Image('Graphic5.png')


def graph6():
    lista2, lista1 = departamentos()
    labels = lista1
    values = lista2
    print(labels)
    print(values)

    trace = go.Bar(x=labels, y=values, text=['27% market share', '24% market share', '19% market share'], marker=dict(
        color=['rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)',
               'rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)',
               'rgba(222,45,38,0.8)', 'rgba(204,204,204,1)', 'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
               'rgba(204,204,204,1)',
               'rgba(204,204,204,1)', 'rgba(204,204,204,1)', 'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
               'rgba(204,204,204,1)',
               'rgba(204,204,204,1)', 'rgba(204,204,204,1)', 'rgba(204,204,204,1)', 'rgb(58,200,225)',
               'rgb(58,200,225)',
               'rgb(58,200,225)', 'rgb(58,200,225)', 'rgb(58,200,225)'],
        line=dict(
            color='rgb(8,48,107)',
            width=2.5,
        )
    ),
                   opacity=0.8)
    data = [trace]
    layout = go.Layout(title='Cantidad de pacientes por departamento', width=900, height=740)
    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, filename='Graphic6.png')
    from IPython.display import Image
    Image('Graphic6.png')


def generate():
    graph1()
    graph2()
    graph3()
    graph4()
    graph5()
    graph6()
