import joblib
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True, as_frame=True)
df = X
df['y'] = y

df_train, df_test = train_test_split(df, test_size=0.2, stratify=df['y'], random_state=2024)

mymodel = DecisionTreeClassifier(random_state=2024)
mymodel.fit(df_train.drop('y', axis=1), df_train['y'])
y_pred = mymodel.predict(df_test.drop('y', axis=1))
print(accuracy_score(df_test['y'], y_pred))
print(str(df_train.drop('y', axis=1).columns.tolist()))

try:
    joblib.dump(mymodel, 'model.joblib')
except Exception as e:
    print(e)