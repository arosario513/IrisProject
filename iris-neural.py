import numpy as np

w1 = -0.5
w2 = 0.1
w3 = 0.6
w4 = 0.5
b = 0


def softplus(n):
    return np.log(1 + np.exp(n))


def predict(x, y, z, a):
    layer1 = np.dot(x, w1) + np.dot(y, w2) + np.dot(z, w3) + np.dot(a, w4) + b
    prediction = softplus(layer1)
    return prediction


try:

    j, k, l, m, = input('NOTE: If the output does not appear, it is because the measurements are not realistic.\n'
                        '\nPlease type 4 numbers spaced out.\nExample: 2.1 3.2 0.4 1.2\n\nNumbers: ').split()

    j, k, l, m = float(j), float(k), float(l), float(m)

    output = round(predict(j, k, l, m))

    if output == 0:
        print('\nSetosa')
    elif output == 1:
        print('\nVersicolor')
    elif output == 2:
        print('\nVirginica')

except KeyboardInterrupt:
    print('\nProgram terminated!')

except ValueError:
    print('\nPlease add the values as asked.')
