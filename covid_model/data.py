import json
import requests
import logging

import pandas as pd
import streamlit as st

from .exceptions.data_error import DataError

logger = logging.getLogger(__name__)


@st.cache(ttl=60*60*24)
def covid_india_statewise_df():
    """Load statewise covid data for India from covid19india.org/v4 api.

    URL: https://api.covid19india.org/v4/min/timeseries.min.json

    Returns pandas dataframe of statewise data with state codes
    All India data is under the state code `TT`
    """
    source = 'https://api.covid19india.org/v4/min/timeseries.min.json'
    dest_file = './data/india.min.json'
    with open(dest_file, 'wb') as f:
        r = requests.get(source, stream=True)
        if r.status_code != 200:
            raise DataError()
        f.writelines(r.iter_content(1024))
    rows = []
    with open(dest_file, 'r') as f:
        j = json.load(f)
        for state in j.keys():
            for dt in j[state]['dates'].keys():
                if 'total' not in j[state]['dates'][dt]:
                    logger.warning(f'total not found in {state} {dt}')
                    continue
                data = j[state]['dates'][dt]['total'].copy()
                data['record_date'] = dt
                data['state_code'] = state
                rows.append(data)
    df = pd.DataFrame(rows)
    df.loc[:, 'active'] = df.confirmed - df.recovered - df.deceased
    return df


@st.cache(ttl=60*60*24)
def covid_india_df():
    """Covid data for India."""
    df = covid_india_statewise_df()
    df = df[df.state_code == 'TT'].copy()
    df = df.drop(columns=['state_code'])
    df.loc[:, 'record_date'] = pd.to_datetime(df.record_date)
    return df.set_index('record_date')


def world_population_df():
    """World population in a pandas dataframe."""
    return pd.read_csv('https://raw.githubusercontent.com/datasets/population/'
                       'master/data/population.csv')


@st.cache()
def india_population():
    """Latest estimated population of India."""
    df = world_population_df()
    latest_year = df[df['Country Name'] == 'India'].Year.max()
    return int(
        df[(df['Country Name'] == 'India') & (df['Year'] == latest_year)].Value
        )
