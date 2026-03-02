import pandas as pd

# Gradient Descent Algorithm for Linear Regression

def gradient_descent(df, w0, w1, L, N):

    for _ in range(N):

        # Step 1: Calculate y_hat
        df['y_hat'] = w0 + w1 * df['x']

        # Step 2: Calculate delta for w0 and w1
        # Note that this is the derivative of the error/cost function wrt w0 and w1

        df['delta_w0'] = df['y'] - df['y_hat']

        df['delta_w1'] = (df['y'] - df['y_hat']) * df['x']

        delta_w0 = df['delta_w0'].mean()
        delta_w1 = df['delta_w1'].mean()

        # Step 3: Update w0 and w1
        w0 = w0 + L * delta_w0
        w1 = w1 + L * delta_w1

        print(f'w0: {round(w0,5)}, w1: {round(w1,5)}')

    return w0, w1


# Create dataframe: Start with dictionary -> pd.DataFrame() it

data = {'x': [3,6,7,2,4,12],
        'y': [4.5, 12, 14.5, 2, 7, 27]}

df = pd.DataFrame(data)

# Initializing hyperparameter learning rate (L) and number of iterations (N)
L = 0.01
N = 3

# Initializing parameters w0 and w1 to 0
w0 = 0
w1 = 0

# Run gradient descent for N iterations
w0, w1 = gradient_descent(df, w0, w1, L, N)