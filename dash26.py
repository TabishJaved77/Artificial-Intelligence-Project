import pandas as pd
import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.figure_factory as ff
import dash_table as dt
from dash.dependencies import Input, Output
import plotly.plotly as py
import plotly.graph_objs as go
####new file
df = pd.read_csv('monfuel2.csv')


app = dash.Dash()

######normal input boxes and dropdown(apna wala dropdown daal lena)

app.layout = html.Div(children=[
    html.H1(children='INTERACTIVE OUTLIERS FINDER(TOTAL FUEL AND TOTAL AMOUNT )'),
    dcc.Input(id='input',value='200',type='number',placeholder='MAX LIMIT OF FUEL/Amount'),
       dcc.Dropdown(
        id='input3',
        options=[
                    {'label': 'TOTAL AMOUNT', 'value': 'Amount'},
                {'label': 'TOTAL FUEL', 'value': 'totalFUEL'},

            ],value='totalFUEL'),
     dcc.Dropdown(
        id='input4',
        options=[
                    {'label': 'october', 'value': 'Oct-18'},
                {'label': 'november', 'value': 'Nov-18'},
            {'label': 'decemeber', 'value': 'Dec-18'},
            {'label': 'january', 'value': 'Jan-19'},

            ],value='Jan-19'),
     dcc.Dropdown(
        id='input2',
        options=[
                    {'label': 'ALL', 'value': 'ALL'},
                {'label': 'Agra', 'value': 'Agra'},
            {'label': 'Aligarh', 'value': 'Aligarh'},
             {'label': 'Allahabad', 'value': 'Allahabad'},
              {'label': 'Ambedkar Nagar	', 'value': 'Ambedkar Nagar'},
              {'label': 'Amethi', 'value': 'Amethi'},
              {'label': 'Amroha', 'value': 'Amroha'},
              {'label': 'Auraiya	', 'value': 'Auraiya'},
              {'label': 'Azamgarh', 'value': 'Azamgarh'},
              {'label': 'Badaun	', 'value': 'Badaun'},
              {'label': 'Bagpat', 'value': 'Bagpat'},
              {'label': 'Bahraich', 'value': 'Bahraich'},
              {'label': 'Ballia', 'value': 'Ballia'},
              {'label': 'Balrampur', 'value': 'Balrampur'},
              {'label': 'Banda', 'value': 'Banda'},
              {'label': 'Barabanki', 'value': 'Barabanki'},
              {'label': 'Bareilly', 'value': 'Bareilly'},
              {'label': 'Basti', 'value': 'Basti'},
              {'label': 'Bhadohi', 'value': 'Bhadohi'},
              {'label': 'Bijnor', 'value': 'Bijnor'},
              {'label': 'Bulandshahr', 'value': 'Bulandshahr'},
              {'label': 'Chandauli', 'value': 'Chandauli'},
              {'label': 'Chitrakoot', 'value': 'Chitrakoot'},
              {'label': 'Deoria', 'value': 'Deoria'},
              {'label': 'Etah', 'value': 'Etah'},
              {'label': 'Etawah', 'value': 'Etawah'},
              {'label': 'Faizabad', 'value': 'Faizabad'},
              {'label': 'Farrukhabad	', 'value': 'Farrukhabad'},
              {'label': 'Fatehpur', 'value': 'Fatehpur'},
              {'label': 'Firozabad	', 'value': 'Firozabad'},
              {'label': 'Gautam Buddh Nagar	', 'value': 'Gautam Buddh Nagar'},
              {'label': 'Ghaziabad', 'value': 'Ghaziabad'},
              {'label': 'Ghazipur', 'value': 'Ghazipur'},
              {'label': 'Gonda', 'value': 'Gonda'},
              {'label': 'Gorakhpur', 'value': 'Gorakhpur'},
              {'label': 'Hamirpur', 'value': 'Hamirpur'},
              {'label': 'Hardoi', 'value': 'Hardoi'},
              {'label': 'Hathras', 'value': 'Hasthras'},
              {'label': 'Jalaun', 'value': 'Jalaun'},
              {'label': 'Jaunpur', 'value': 'Jaunpur'},
              {'label': 'Jhansi', 'value': 'Jhansi'},
              {'label': 'Jyotiba Phule Nagar', 'value': 'Jyotiba Phule Nagar'},
              {'label': 'Kannauj', 'value': 'Kannauj'},
              {'label': 'Kanpur Dehat	', 'value': 'Kanpur Dehat'},
              {'label': 'Kanpur Nagar	', 'value': 'Kanpur Nagar'},
              {'label': 'Kasganj', 'value': 'Kasganj'},
              {'label': 'Kaushambi', 'value': 'Kaushambi'},
              {'label': 'Kushinagar	', 'value': 'Kushinagar	'},
              {'label': 'Lakhimpur Kheri	', 'value': 'Lakhimpur Kheri'},
              {'label': 'Lucknow	', 'value': 'Lucknow'},
              {'label': 'Maharajganj', 'value': 'Maharajganj'},
              {'label': 'Mahoba', 'value': 'Mahoba'},
              {'label': 'Mainpuri', 'value': 'Mainpuri'},
              {'label': 'Mathura', 'value': 'Mathura'},
              {'label': 'Mau', 'value': 'Mau'},
              {'label': 'Meerut', 'value': 'Meerut'},
              {'label': 'Mirzapur', 'value': 'Mirzapur'},
              {'label': 'Moradabad', 'value': 'Moradabad'},
              {'label': 'Muzaffarnagar	', 'value': 'Muzaffarnagar'},
              {'label': 'Pilibhit', 'value': 'Pilibhit'},
              {'label': 'Pratapgarh', 'value': 'Pratapgarh'},
              {'label': 'Raebareli', 'value': 'Raebareli'},
              {'label': 'Rampur', 'value': 'Rampur'},
              {'label': 'Saharanpur', 'value': 'Saharanpur'},
              {'label': 'Sambhal	', 'value': 'Sambhal'},
              {'label': 'Shahjahanpur', 'value': 'Shahjahanpur'},
              {'label': 'Shamli', 'value': 'Shamli'},
              {'label': 'Shravasti', 'value': 'Shravasti'},
              {'label': 'Sitapur', 'value': 'Sitapur'},
              {'label': 'Sonbhadra	', 'value': 'Sonbhadra'},
              {'label': 'Sultanpur', 'value': 'Sultanpur'},
              {'label': 'Unnao	', 'value': 'Unnao'},
              {'label': 'Varanasi	', 'value': 'Varanasi'},
              {'label': 'ALL', 'value': 'ALL'},


        ],
        value='ALL'
        ),
    html.Div(id='bar'),
    html.Div(id='output-graph'),

])
#################3
#############table upload

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value'),
    Input(component_id='input2', component_property='value'),
    Input(component_id='input3', component_property='value'),
    Input(component_id='input4', component_property='value')]

)

def update_table(val,val2,val4,val3):
    val=int(val)
    con=val2
    strr="ALL"
    if(con==strr):
        df1=df
        df2 = df1[df1[val4] >val]

    else:
        df1=df[df['District']==con]
        df2 = df1[df1[val4] > val]
        df2 = df2.drop(['District'],axis = 1)
    df3=df2[df2['Month']==val3]
    df4=df3.drop(['Month','PRV'],axis=1)

    data = df4.to_dict('rows')
    columns =  [{"name": i, "id": i,} for i in (df4.columns)]
    return dt.DataTable(data=data, columns=columns)



 ##################bar upload

@app.callback(
    Output(component_id='bar', component_property='children'),
    [Input(component_id='input', component_property='value'),
    Input(component_id='input2', component_property='value'),
    Input(component_id='input3', component_property='value')
    ,Input(component_id='input4', component_property='value')]

)
def update_value(val,val2,val4,val3):
    val=int(val)
    con=val2
    strr="ALL"
    if(con==strr):
        df1=df
        df2 = df1[df1[val4] >val]

    else:
        df1=df[df['District']==con]
        df2 = df1[df1[val4] > val]
        df2 = df2.drop(['District'],axis = 1)
    df3=df2[df2['Month']==val3]
    df4= df3.sort_values(by = [val4], ascending=False).iloc[0:5]
    df4=df4.drop(['Month','PRV'],axis=1)
    con1='PRV NO.'

    return dcc.Graph(
        id='example',
        figure={
            'data':[
                {'x':df4[con1],'y':df4[val4], 'type':'bar'}
              ],
            'layout':{
               # 'title':'PRV Number:"{}"'.format(prv)
            }
        }
    )




##################################
if __name__== "__main__":
    app.run_server(debug=True)

