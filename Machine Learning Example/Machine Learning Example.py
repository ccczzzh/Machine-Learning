import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

train_inp = np.array([[0,0,1],
                      [1,1,1],
                      [1,0,1],
                      [0,1,1],
                      [0,1,0]])

train_out = np.array([[0,1,1,0,0]]).T

#np.random.seed(1)

r = np.random.random((3,1))

synaptic_weights = 2 * r - 1

print('Random Starting synaptic weights: ')
print(synaptic_weights)

for iteration in range(10000):
    input_layer = train_inp

    out = sigmoid(np.dot(input_layer,synaptic_weights))

    error = train_out - out

    adjustments = error * sigmoid_derivative(out)

    synaptic_weights1 =np.dot(input_layer.T,adjustments)
    #print(synaptic_weights1)
    synaptic_weights += synaptic_weights1
print('Synaptic weights after training')
print(synaptic_weights)

print('Outputs after training: ')
print(out)

test_inp = ([[1,1,1],
             [1,0,0]])

test_out = sigmoid(np.dot(test_inp,synaptic_weights))

print('test Output is ')
print(test_out)