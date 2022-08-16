import streamlit as st
import pandas as pd
import numpy as np
import json


with open('onoff.json', 'r') as fp:
    data = json.loads(fp)


st.write(data)
