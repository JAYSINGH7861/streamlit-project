# streamlit run premier.py

import streamlit as st 
import pandas as pd 
import plotly.express as px

st.set_page_config(layout='wide',
                   page_title='premier league dashboard',
                   page_icon=":soccer:")

@st.cache_data
def load():
    return pd.read_csv('premierleague.csv')

# main code starts here 
df = load()

st.image('banner.png',use_column_width=True)
st.title("premier league dashboard")
with st.expander("view raw premier league data"):
    st.dataframe(df.sample(1000))

rows,cols=df.shape
c1,c2=st.columns(2)
c1.markdown(f'### total record :{rows}')
c2.markdown(f'### total columns:{cols}')

numeric_df=df.select_dtypes(include='number')
cat_df=df.select_dtypes(exclude='number')
with st.expander("column name"):
    st.markdown(f'columns with number :{",".join(numeric_df)}')
    st.markdown(f'colums without numbers:{",".join(cat_df)}')

# visualization 
c1,c2=st.columns([1,5])
xcol=c1.selectbox("choose a column for x- axis",numeric_df.columns)
ycol=c2.selectbox("choose a columns for y_axis",numeric_df.columns)
zcol=c1.selectbox("choose a columns for z_axis",numeric_df.columns)
color=c1.selectbox('choose columns for color', cat_df.columns)
fig=px.scatter_3d(df,x=xcol,y=ycol,z=zcol,color=color,height=500)
c2.plotly_chart(fig,use_container_width=True)

st.title('more analysics')
c1,c2=st.columns(2)
c1.video("https://www.youtube.com/watch?v=qXB5Bcj7F6M&pp=ygUUcHJpZW1lciBsZWFndWUgaW50cm8%3D")
c2.markdown('''
#uhfilhrfilhewihfiuwifgiwgfiuiufhiggkjwegfhejbffjhjdfsbjfehgef''')

st.title("Premier League Clubs")
clubs=df['HomeTeam'].unique() + df['AwayTeam'].unique()
clubs=sorted(set(clubs))
st.info(",".join(clubs))
