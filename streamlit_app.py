from urllib.parse import urlencode, parse_qs
import streamlit as st
import session_state

logger = st._LOGGER

def get_query_param(key, query_params, default=''):
    return query_params[key][0] if key in query_params else default

query_params = {k: v[0] for k, v in st.experimental_get_query_params().items()}

session = session_state.get(initial_query_params='')

if not session.initial_query_params:
    session.initial_query_params = query_params.copy()
    logger.info(f'Initial query params: {session.initial_query_params}')

initial_query_params = session.initial_query_params

st.write("Initial query params:", initial_query_params)
st.write("Query params before setting new ones:", query_params)

new_query_string = st.text_area("New query params string (like 'a=b&c=d')", value=urlencode(initial_query_params))

if st.button("Set new query params"):
    st.experimental_set_query_params(**parse_qs(new_query_string))
