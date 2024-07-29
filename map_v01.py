import pandas as pd
import plotly.express as px

a = pd.read_csv('data\\기온.csv', encoding = 'cp949')
b = pd.read_csv('data\\강수량.csv', encoding = 'cp949')
df=pd.merge(left=a,right=b,how='inner',left_on=['행정구역별(1)','시점'],right_on=['행정구역별','시점'])
df=df.drop(['행정구역별(1)'],axis=1)
df.columns=['year','temp','region','preci']
df=df[df['region']!='전국(평균)']
df['temp']=df['temp'].astype(float)
df['preci']=df['preci'].astype(float)
df=df[df['region']!='세종특별자치시']

si_do={'강원도':'강원도','경기도':'경기도', '경상남도':'경상남도','경상북도':'경상북도',
       '광주광역시':'광주','대구광역시':'대구','대전광역시':'대전','부산광역시':'부산',
       '서울특별시':'서울','세종특별자치시':'세종','울산광역시':'울산','인천광역시':'인천',
       '전라남도':'전라남도','전라북도':'전라북도','제주특별자치도':'제주도','충청남도':'충청남도',
       '충청북도':'충청북도'}
eng_sido=pd.DataFrame.from_dict(si_do,orient='index').reset_index()
eng_sido.columns=['kor','do']
df2=pd.merge(left=df,right=eng_sido,how='left',left_on=df['region'],right_on=eng_sido['kor'])
sido_dict=df2[['kor','do']].set_index('kor')

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/southkorea/southkorea-maps/master/kostat/2018/json/skorea-provinces-2018-geo.json') as response:
    kor = json.load(response)
max_count = df['temp'].max()
fig = px.choropleth_mapbox(df, geojson=kor,
                      locations='region', 
                      color='temp',
                      color_continuous_scale="Viridis",
                      range_color=(0, max_count),
                      featureidkey="properties.name",
                      mapbox_style="carto-positron",
                      opacity=0.5,
                      center = {"lat": 36.910968, "lon": 127.964387}, 
                      zoom=5,
                      animation_frame='year'
                          )
fig.update_geos(fitbounds="locations",visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},)
fig.write_html('my_map.html')
map_temp=fig.to_json()
