"""Streamlit app to model COVID-19 using SIR and SIRS techniques."""
import streamlit as st
import numpy as np
import pandas as pd

from covid_model import data

st.title('COVID-19 Resource Estimation Model')

india_population = data.india_population()

pop = st.sidebar.number_input(
    label='Population',
    min_value=10000,
    max_value=2000000000,
    value=india_population,
    help='Population under consideration')

num_days = st.sidebar.slider(
    label='Number of days',
    min_value=1,
    max_value=120,
    value=30,
    step=1,
    key='num_days',
    help='Number of days to simulate')

avg_contacts = st.sidebar.slider(
    label='Average contacts infected per day',
    min_value=0,
    max_value=100,
    value=5,
    step=1,
    key='avg_contacts',
    help='Average number of people that an infected person contacts in a day')

recovery_days = st.sidebar.slider(
    label='Days to recover',
    min_value=1,
    max_value=50,
    value=12,
    step=1,
    key='value3',
    help='Average number of days for an infected person to recover')


def _india_since_mar_1_2021():
    sel_cols = ['confirmed', 'active', 'recovered', 'deceased']
    df = data.covid_india_df()
    return df[df.index >= '2021-03-01'].copy()[sel_cols]


india_recent = _india_since_mar_1_2021()

st.dataframe(india_recent)

st.line_chart(india_recent)
