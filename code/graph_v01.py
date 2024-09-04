import pandas as pd

a = pd.read_csv('data\\기온.csv', encoding = 'cp949')
b = pd.read_csv('data\\강수량.csv', encoding = 'cp949')
df=pd.merge(left=a,right=b,how='inner',left_on=['행정구역별(1)','시점'],right_on=['행정구역별','시점'])
df=df.drop(['행정구역별(1)'],axis=1)
df.columns=['year','temp','region','preci']
df=df[df['region']!='전국(평균)']
df['temp']=df['temp'].astype(float)
df['preci']=df['preci'].astype(float)
df=df[df['region']!='세종특별자치시']

si_do={'강원도':'강원특별자치도','경기도':'경기도', '경상남도':'경상남도','경상북도':'경상북도',
       '광주광역시':'광주','대구광역시':'대구','대전광역시':'대전','부산광역시':'부산',
       '서울특별시':'서울','세종특별자치시':'세종','울산광역시':'울산','인천광역시':'인천',
       '전라남도':'전라남도','전라북도':'전라북도','제주특별자치도':'제주도','충청남도':'충청남도',
       '충청북도':'충청북도'}
eng_sido=pd.DataFrame.from_dict(si_do,orient='index').reset_index()
eng_sido.columns=['kor','도']
df2=pd.merge(left=df,right=eng_sido,how='left',left_on=df['region'],right_on=eng_sido['kor'])
sido_dict=df2[['kor','도']].set_index('kor')

import plotly.express as px

fig = px.scatter(df2, x="temp", y="preci", color="도", animation_frame='year')
fig.update_xaxes(range=[8, 18])
f1=fig.to_json()


fig.write_html('my_plot.html')
