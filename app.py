import streamlit as st
import pandas as pd

st.title("📊 Google Play Store ML Dashboard")
df = pd.read_csv("cleaned_googleplaystore.csv")
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
