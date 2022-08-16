import streamlit as st
import pandas as pd
import numpy as np
import json


with open('onoff.json', 'r') as fp:
    data = json.load(fp)


lt = data.values()
lt = [0 if item == '"off"' else 1 for item in lt]
st.write(lt)
