import pandas as pd

data = {'x': [3,6,7,2,4,12],
        'y': [4.5, 12, 14.5, 2, 7, 27]}

df = pd.DataFrame(data)

# Closed Form Solution for Linear Regression

def closed_form_solution(df):

    # Calculate w1 and w0 using the closed form solution formula
    w1 = ((df['x'] - df['x'].mean()) * (df['y'] - df['y'].mean())).sum() / ((df['x'] - df['x'].mean())**2).sum()

    w0 = df['y'].mean() - w1 * df['x'].mean()

    return w0, w1

w0, w1 = closed_form_solution(df)

print(f'w0: {round(w0,2)}, w1: {round(w1,2)}')

print(f'Best fit line eqn: y = {round(w0,2)} + {round(w1,2)}x')