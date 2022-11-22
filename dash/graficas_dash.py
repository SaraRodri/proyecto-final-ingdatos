import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from conexion import conexion
import sql_dash as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Count de autores
con = conexion()
con.openConnection()
query = pd.read_sql_query(sql.ctAutores(), con.connection)
con.closeConnection()
cAutores = pd.DataFrame(query, columns=["round", "count"])

# Grafico pie
figPieCaut = px.pie(cAutores.head(20), names="round", values="count")
# Grafico linea
figLineCaut = px.line(cAutores.head(20), x="round", y="count")

# Count editorial
con2 = conexion()
con2.openConnection()
query = pd.read_sql_query(sql.ctEditorial(), con2.connection)
con2.closeConnection()
cEditorial = pd.DataFrame(query, columns=["round", "count"])

# Grafico pie
figPieCed = px.pie(cEditorial.head(20), names="round", values="count")

# Libros por autor
con3 = conexion()
con3.openConnection()
query = pd.read_sql_query(sql.librosAutor(), con3.connection)
con3.closeConnection()
autlib = pd.DataFrame(query, columns=["nombre", "count"])

# Grafico barras
figBarLiba = px.bar(autlib.head(20), x="nombre", y="count")

# Libros por editorial
con4 = conexion()
con4.openConnection()
query = pd.read_sql_query(sql.librosEditorial(), con4.connection)
con4.closeConnection()
autlib = pd.DataFrame(query, columns=["nombre", "count"])

# Grafico barras
figBarLibe = px.bar(autlib.head(20), x="nombre", y="count")

# Año y calificacion
con5 = conexion()
con5.openConnection()
query = pd.read_sql_query(sql.calificacion_yr(), con5.connection)
con5.closeConnection()
cal_yr = pd.DataFrame(query, columns=["publicacion_yt", "PROMEDIO"])

# Grafico barras
figBarLinac = px.bar(cal_yr.head(20), x="publicacion_yt", y="PROMEDIO")

# Promedio por autores
con6 = conexion()
con6.openConnection()
query = pd.read_sql_query(sql.prom_aut(), con6.connection)
con6.closeConnection()
promAut = pd.DataFrame(query, columns=["nombre", "PROMEDIO"])

# Grafico barras
figBarPromAut = px.bar(promAut.head(20), x="nombre", y="PROMEDIO")

# Libros por categoría
con7 = conexion()
con7.openConnection()
query = pd.read_sql_query(sql.categoria(), con7.connection)
con7.closeConnection()
cat = pd.DataFrame(query, columns=["nombre", "count"])

# Grafico barras
figBarCat = px.bar(cat.head(20), x="nombre", y="count")

# Layout
app.layout = html.Div(children=[
    html.H1(children='Dashboard Amazon Books'),  # genera <h1>Dashboard Covid 19</h1>
    html.Div(className="container", children=[
        # Row for cases
        html.Div(className="row", children=[
            # Col for vertical bars
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H2(children='Calificación de autores'),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id='barCtAut',
                            figure=figPieCaut
                        ),
                    ]),

                ]),
            ]),

            # Col for line
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H2(children='Calificacion autores'),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id='lineCtAut',
                            figure=figLineCaut
                        ),
                    ]),

                ]),
            ]),

            # Col for line
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H2(children='Calificacion editoriales'),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id='LineCtEd',
                            figure=figLineCed
                        ),
                    ]),

                ]),
            ]),

            # Col for pie
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H2(children='Calificacion editoriales'),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id='PieCtEd',
                            figure=figPieCed
                        ),
                    ]),

                ]),
            ]),

            # Col for bar
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H2(children='Libros Autor'),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id='LineLibAut',
                            figure=figBarLiba
                        ),
                    ]),

                ]),
            ]),

            # Col for bar
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H2(children='Libros Editorial'),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id='LineLibEd',
                            figure=figBarLibe
                        ),
                    ]),

                ]),
            ]),

            # Col for line
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H2(children='AVG de Año de publicación'),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id='LineAC',
                            figure=figBarLinac
                        ),
                    ]),

                ]),
            ]),

            # Col for bar
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H2(children='Promedio de libros por autor'),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id='BarPromAut',
                            figure=figBarPromAut
                        ),
                    ]),

                ]),
            ]),

            # Col for bar
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H2(children='Libros por categoría'),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id='BarCat',
                            figure=figBarCat
                        ),
                    ]),

                ]),
            ]),

        ]),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
