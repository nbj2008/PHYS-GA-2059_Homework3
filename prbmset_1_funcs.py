import numpy as np

#### Create Arrays

def generate_mats(data, *cols):
    cols = [x for x in cols if x is not None]
    A = np.stack((np.ones(data.shape[0]), *data[cols].T.values))
    y = np.array(data.y)
    c = np.array(1/data.σy**2)
    return A, y, c

#### Evaluate Best Fit Parameters from Equation 5

def calc_params(A, y, c):
    return np.linalg.solve(A @ (A * c).T, A @ (c * y).T)

#### Fit Data

def fit_data(params, span, num=100, span_funcs=(np.ones_like, lambda x: x)):
    low, high = span
    rang = np.linspace(low, high, num=num)
    fit = params @ np.stack([func(rang) for func in span_funcs])
    return rang, fit

#### Make Plots

def plot_fit(data, fit_data):
    rang, fit = fit_data
    _ = plt.scatter('x', 'y', data=data,label=None)
    _ = plt.errorbar('x', 'y', fmt='none', yerr='σy', capsize=2, data=data,label=None)
    _ = plt.plot(rang, fit, 'k')
    plt.xlim([0,rang[-1]])
    plt.ylim([0,700])
    
# Error Covariance Matrix
def errors(A, c):
    return np.linalg.inv(A @(A * c).T)