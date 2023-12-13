import streamlit as st
import pandas as pd
import numpy as np

# st.set_page_config(page_title='XYZ', layout = 'wide', page_icon = 'logo2.png', initial_sidebar_state = 'auto')
st.set_page_config(page_title="UBER")
st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/''streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows = nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data




# Create a text element and let the reader know the data is loading..
data_load_state = st.text('Loading data ...')
# Load 10,000 rows of data into dataframe
data = load_data(10000)

# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

# Inspect the raw data on button toggle
if st.button('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
    if st.button('Hide data'):
        pass

# Draw a histogram
st.subheader('Number of pickups by hour')

hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins= 24, range=(0,24))[0]

st.bar_chart(hist_values)


# filtering
hour_to_filter = st.slider('hour',0,23,17)#min:0h, max:23h, default:17h

filter_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader(f'Map of all pickups at {hour_to_filter}:00')

st.map(filter_data)