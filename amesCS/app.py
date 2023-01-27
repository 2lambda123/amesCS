
# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
# A GOOD ARTICLE: https://medium.com/swlh/dashboards-in-python-3-advanced-examples-for-dash-beginners-and-everyone-else-b1daf4e2ec0a
import dash
import dash_core_components as dcc
import dash_html_components as html

from amesgcm.FV3_utils import  areo_avg

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Plot selection'),
    dcc.Dropdown(
        options=[
            {'label': '(2D) Lat/Lon map plot', 'value': '2D_lon_lat'},
            {'label': '(2D) Lat/Altitude cross section', 'value': '2D_lat_lev'},
            {'label': '(2D) Lon/Altitude cross section', 'value': '2D_lon_lev'},
            {'label': '(2D) Time/Latitude plot', 'value': '2D_time_lat'},
            {'label': '(2D) Time/Altitude plot', 'value': '2D_time_lev'},
            {'label': '(2D) Longitude/Time plot', 'value': '2D_lon_time'},
            {'label': '(1D) Time serie', 'value': '1D_time'},
            {'label': '(1D) Lat plot', 'value': '1D_lat'},
            {'label': '(1D) Lon plot', 'value': '1D_lon'},
            {'label': '(1D) Altitude profile', 'value': '1D_lev'},
            {'label': '(1D) Diurnal cycle', 'value': '1D_diurn'},
        ],
        value='MTL'
    ),


    html.Label('Variables selection (multi)'),
    dcc.Dropdown(
        options=[
            {'label': 'Surface Temperature  [K]', 'value': 'ps'},
            {'label': 'surface pressure  [Pa]', 'value': 'ts'},
            {'label': 'zonal wind  [m/sec]', 'value': 'ucomp'},
            {'label': 'meridional wind  [m/sec]', 'value': 'vcomp'},
            {'label': 'temperature  [K]', 'value': 'temp'}
        ],
        value=['MTL', 'SF'],
        multi=True
    ),

    html.Label('Vertical coordinates'),
    dcc.RadioItems(
        options=[
            {'label': 'Pressure[Pa]', 'value': 'pstd'},
            {'label': 'Altitude above ground level [m]', 'value': 'zagl'},
            {'label': 'Altitude with respect to ref aeroid', 'value': 'zstd'},
        ],
        value='MTL'
    ),

    html.Label('Export data'),
    dcc.RadioItems(
        options=[
            {'label': 'PNG image', 'value': 'png'},
            {'label': 'Netcdf File', 'value': 'ncdf'},
            {'label': '.csv text file', 'value': 'csv'},
        ],
        value='MTL'
    ),

    html.Label('Options'),
    dcc.Checklist(
        options=[
            {'label': 'Add solid contours', 'value': 'solid_cont'},
        ],
        value=['MTL', 'SF']
    ),

    html.Label('Custom Title for archiving figure'),
    dcc.Input(value='(default title)', type='text'),

    html.Label('Solar Longitude'),
    dcc.Slider(
        min=0,
        max=360,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(0, 360,15)},
        value=5,
    ),


    dcc.Input(id='my-id', value='Level (Pa)', type="text"),
    html.Button('Submit', id='button'),
    html.Div(id='my-div'),

], style={'columnCount': 2})



if __name__ == '__main__':
    app.run_server(debug=True) #This upload the webrowser automatically when changes are made to the code
