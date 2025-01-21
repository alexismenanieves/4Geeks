import pandas as pd
import streamlit as st
import joblib
import matplotlib.pyplot as plt
import plotly.express as px

st.title('Bike Sharing Model - Analysis')

df_raw = pd.read_csv('data/bike.csv')
df = (
    df_raw
    .astype({'season':'category',
             'weathersit':'category',
             'holiday':'category',
             'weekday':'category',
             'workingday':'category',
             'dteday':'datetime64[ns]'})
)

X = df.drop('target', axis=1)
y = df['target']
horizon = 24*7
X_train, X_test = X.iloc[:-horizon,:], X.iloc[-horizon:,:]
y_train, y_test = y.iloc[:-horizon], y.iloc[-horizon:]
df_train = pd.concat([y_train, X_train], axis=1)
df_test = pd.concat([y_test, X_test], axis=1)

# Create a Plotly dataframe
st.write('Numerical statistics')
st.dataframe(df_train.describe(include='number').T)
st.write('Categorical statistics')
st.dataframe(df_train.describe(include='category').T)

# Create a Matplotlib plot
df_train.hist(figsize=(8,8))
plt.show()

# Create Plotly plot 
fig = px.line(df, x='dteday', y='target', title=f'Values') 
# Display the plot 
st.plotly_chart(fig)

#fig = px.line(df, x="year", y="lifeExp", color="continent", line_group="country", hover_name="country",
#        line_shape="spline", render_mode="svg")
#fig.show()