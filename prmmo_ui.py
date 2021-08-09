import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.sidebar.title('PRIMO Search')
# st.sidebar.text_input('Enter keyword or NIIN')

# col1, col2 = st.columns(2)
# with col1:
#     st.header('Lifecycle')

# with col2:
    # st.header('Dates')

#-- Set search by NIIN or keyword
select_event = st.sidebar.selectbox('How do you want to find data?',
                                    ['By NIIN', 'By Keyword'])

if select_event == 'By NIIN':      
    str_t0 = st.sidebar.text_input('NIIN', '13754920')
    t0 = int(str_t0)

    st.sidebar.markdown("""
    Example NIINs:
    * 6843419
    * 12822053
    * 13926982
    """)
else:
    str_t0 = st.sidebar.text_input('Keyword', 'O-RING')
    t0 = str(str_t0)

    st.sidebar.markdown("""
    Example Keywords:
    * O-RING
    * CONNECTOR
    * ELECTRON TUBE
    """)

# col1, col2 = st.columns([2,1])

def random_date_generator(start_date, range_in_days):
    days_to_add = np.arange(0, range_in_days)
    random_date = np.datetime64(start_date) + np.random.choice(days_to_add)
    return random_date

date_data = random_date_generator('2022-08-08', 60)
# with col1:
#     st.header('Lifecycle')

# with col2:
#     st.header('Purchase Date')
#     st.write(date_data)

df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=('Item', 'Product Halted', 'Purchase Date'),

)

st.table(df)