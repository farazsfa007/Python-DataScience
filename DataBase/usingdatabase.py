import streamlit as st
from database import Smartphone
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy import create_engine

engine= create_engine('sqlite:///mydatabase.sqlite3')
Session=sessionmaker(engine)
session=Session()


sidebar=st.sidebar

sidebar.header('Add Smart Phone Data here')
sidebar.markdown('---')

brand_v=sidebar.text_input('Brand')
name_v=sidebar.text_input('Name')
price_v=sidebar.text_input('Price')
ram_v=sidebar.text_input('Ram')
storage_v=sidebar.text_input('Storage')

btn = sidebar.button('Save Data')

if btn:
    try:
        myphone=Smartphone(brand=brand_v,name=name_v,
        price=price_v,ram=ram_v,storage=storage_v)

        session.add(myphone)
        session.commit()

        st.success('Data Saved!!!')
    except Exception as e:
        print(e)
        st.error('Error in Saving Data')

st.header('Smart Phone Saved')
st.markdown('---')

data=session.query(Smartphone).all()

print(data)

entry1=data[0]

col1, col2,col3,col4,col5,col6=st.columns(6)

col1.subheader('ID')
col2.subheader('Brand')
col3.subheader('Name')
col4.subheader('Price')
col5.subheader('Ram')
col6.subheader('Storage')

for entry in data:
    
    col1.text(entry.id)
    col2.text(entry.brand)
    col3.text(entry.name)
    col4.text(entry.price)
    col5.text(entry.ram)
    col6.text(entry.storage)