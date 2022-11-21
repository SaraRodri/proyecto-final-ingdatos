import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from conexion import conexion
import sql_dash as sql


# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Count de autores
con = conexion()
con.openConnection()
query = pd.read_sql_query(sql.ctAutores(), con.connection)
con.closeConnection()
cAutores = pd.DataFrame(query, columns=["round", "count"])

# Grafico barras
figBarCases = px.bar(cAutores.head(20), x="round", y="count",
                      height=1000,
                      title='Barras Horizontales')

#Grafico pie
figPieCases = px.pie(cAutores.head(20), names="round", values="count")
#Grafico linea
figLineCases = px.line(cAutores.head(20), x="round", y="count")

"""

# Casos por region
con = conexion()
con.openConnection()
query = pd.read_sql_query(sql.totalCasesByRegion(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["region_code", "region", "amount"])

# Grafico barras
figBarCasesR = px.bar(dfCases.head(20), x="region", y="amount")
"""
# Layout 
app.layout = html.Div(children=[
    html.H1(children='Dashboard Covid 19'), # genera <h1>Dashboard Covid 19</h1>
    html.Div(className= "container", children=[
        # Row for cases
        html.Div(className= "row", children=[
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H2(children='Calificación de autores'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barCtAut',
                                    figure=figBarCases
                                ),    
                    ]),    
                    
                ]),
            ]),
            
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H2(children='Calificacion autores'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieCtAut',
                                    figure=figPieCases
                                ), 
                    ]),    
                    
                ]),
            ]),
            
             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H2(children='Calificacion autores'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='lineCtAut',
                                      figure=figLineCases
                                  ),
                    ]),    
                    
                ]),
            ]),
        ]),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
