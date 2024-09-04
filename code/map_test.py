import pandas as pd
import glob
import plotly.express as px

def make_dt(df):
    df = df.drop(df.index[-1])
    df.날짜.replace('\t','', inplace = True)
    df['날짜'] = pd.to_datetime(df.날짜)
    return df

def find_maxtem(df, year, month):
    df = make_dt(df)
    max_df = df[(df.날짜.dt.year == year) & (df.날짜.dt.month == month)].sort_values(by = '최고기온(℃)', ascending = False).head(1)
    return max_df

def find_temdf(df, month):
    df1 = find_maxtem(df, 2013, month)
    df2 = find_maxtem(df, 2014, month)
    df3 = find_maxtem(df, 2015, month)
    df4 = find_maxtem(df, 2016, month)
    df5 = find_maxtem(df, 2017, month)
    df6 = find_maxtem(df, 2018, month)
    df7 = find_maxtem(df, 2019, month)
    df8 = find_maxtem(df, 2020, month)
    df9 = find_maxtem(df, 2021, month)
    df10 = find_maxtem(df, 2022, month)
    df11 = find_maxtem(df, 2023, month)
    df_year = pd.merge(df1, df2, how = 'outer')
    df_year = pd.merge(df_year, df3, how = 'outer')
    df_year = pd.merge(df_year, df4, how = 'outer')
    df_year = pd.merge(df_year, df5, how = 'outer')
    df_year = pd.merge(df_year, df6, how = 'outer')
    df_year = pd.merge(df_year, df7, how = 'outer')
    df_year = pd.merge(df_year, df8, how = 'outer')
    df_year = pd.merge(df_year, df9, how = 'outer')
    df_year = pd.merge(df_year, df10, how = 'outer')
    df_year = pd.merge(df_year, df11, how = 'outer')
    df_year = df_year[['날짜', '지점', '최고기온(℃)']]
    return df_year

def recolumns(df,month, location):
    df = find_temdf(df, month)
    df['날짜'] = df.날짜.dt.year
    df['지점'] = location
    df.rename(columns = {'날짜':'year','지점':'region','최고기온(℃)':'temp'}, inplace = True)
    return df

def make_ko(month):
    global gg, cn, jj, js, se, bu, cs, ic, sj, jn, ks, da, dg, ul, gj, gw, kn
    df1 = recolumns(gg, month, '경기도')
    df2 = recolumns(cn, month, '충청북도')
    df3 = recolumns(jj, month, '제주도')
    df4 = recolumns(js, month, '전라남도')
    df5 = recolumns(se, month, '서울특별시')
    df6 = recolumns(bu, month, '부산광역시')
    df7 = recolumns(cs, month, '충청남도')
    df8 = recolumns(ic, month, '인천광역시')
    df9 = recolumns(sj, month, '세종특별자치시')
    df10 = recolumns(jn, month, '전라북도')
    df11 = recolumns(ks, month, '경상남도')
    df12 = recolumns(da, month, '대전광역시')
    df13 = recolumns(dg, month, '대구광역시')
    df14 = recolumns(ul, month, '울산광역시')
    df15 = recolumns(gj, month, '광주광역시')
    df16 = recolumns(gw, month, '강원도')
    df17 = recolumns(kn, month, '경상북도')
    ko_6 = pd.merge(df1, df2, how = 'outer')
    ko_6 = pd.merge(ko_6, df3, how = 'outer')
    ko_6 = pd.merge(ko_6, df4, how = 'outer')
    ko_6 = pd.merge(ko_6, df5, how = 'outer')
    ko_6 = pd.merge(ko_6, df6, how = 'outer')
    ko_6 = pd.merge(ko_6, df7, how = 'outer')
    ko_6 = pd.merge(ko_6, df8, how = 'outer')
    ko_6 = pd.merge(ko_6, df9, how = 'outer')
    ko_6 = pd.merge(ko_6, df10, how = 'outer')
    ko_6 = pd.merge(ko_6, df11, how = 'outer')
    ko_6 = pd.merge(ko_6, df12, how = 'outer')
    ko_6 = pd.merge(ko_6, df13, how = 'outer')
    ko_6 = pd.merge(ko_6, df14, how = 'outer')
    ko_6 = pd.merge(ko_6, df15, how = 'outer')
    ko_6 = pd.merge(ko_6, df16, how = 'outer')
    ko_6 = pd.merge(ko_6, df17, how = 'outer')
    return ko_6

file_list = glob.glob('mapdata\\*.csv')

dataframes = {}
for file in file_list:
    name = file.replace('.csv', '').replace('mapdata\\','')
    df = pd.read_csv(file, encoding='cp949')
    dataframes[name] = df
    
gg = dataframes['경기(이천)']
cn = dataframes['충청북도(청주)']
jj = dataframes['제주(제주시)']
js = dataframes['전라남도(광양)']
se = dataframes['서울']
bu = dataframes['부산']
cs = dataframes['충청남도(부여)']
ic = dataframes['인천']
sj = dataframes['세종']
jn = dataframes['전라북도(순창)']
ks = dataframes['경상남도(양산)']
da = dataframes['대전']
dg = dataframes['대구']
ul = dataframes['서울']
gj = dataframes['광주']
gw = dataframes['강원(홍천)']
kn = dataframes['경상북도(의성)']

ko = make_ko(6)


si_do={'강원도':'Gangwon-do','경기도':'Gyeonggi-do', '경상남도':'Gyeongsangnam-do','경상북도':'Gyeongsangbuk-do',
       '광주광역시':'Gwangju','대구광역시':'Daegu','대전광역시':'Daejeon','부산광역시':'Busan',
       '서울특별시':'Seoul','세종특별자치시':'Sejongsi','울산광역시':'Ulsan','인천광역시':'Incheon',
       '전라남도':'Jeollanam-do','전라북도':'Jeollabuk-do','제주특별자치도':'Jeju-do','충청남도':'Chungcheongnam-do',
       '충청북도':'Chungcheongbuk-do'}

eng_sido=pd.DataFrame.from_dict(si_do,orient='index').reset_index()
eng_sido.columns=['kor','do']
df2=pd.merge(left=ko,right=eng_sido,how='left',left_on=ko['region'],right_on=eng_sido['kor'])
sido_dict=df2[['kor','do']].set_index('kor')

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/southkorea/southkorea-maps/master/kostat/2018/json/skorea-provinces-2018-geo.json') as response:
    kor = json.load(response)
max_count = ko['temp'].max()
fig = px.choropleth_mapbox(ko, geojson=kor,
                      locations='region', 
                      color='temp',
                      color_continuous_scale=[
                          (0.0, 'white'),
                          (0.4, "blue"),
                          (0.8, "green"),
                          (1.0, "red")
                          ],
                      range_color=(0, max_count),
                      featureidkey="properties.name",
                      mapbox_style="carto-positron",
                      opacity=0.5,
                      center = {"lat": 36.910968, "lon": 127.964387}, 
                      zoom=5,
                      animation_frame='year'
                          )
fig.update_traces(marker=dict(line=dict(width=0.5, color='DarkSlateGrey')))
fig.update_geos(fitbounds="locations",visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},)
fig.write_html('my_map.html')
map_temp=fig.to_json()
