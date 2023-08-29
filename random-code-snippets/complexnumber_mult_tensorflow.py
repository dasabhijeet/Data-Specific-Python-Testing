# tensorflow 2.0 code

# importing the library
import tensorflow as tf

# Initializing the input tensor
a = tf.constant([-2 + 3j, -5 + 4j, 7 + 2j, 1 + 7j], dtype = tf.complex128)
b = tf.constant([-1 + 2j, -6 + 8j, 8 + 2j, 0 + 1j], dtype = tf.complex128)

print("\n\n\n\n\n")
# Printing the input tensor
print('a: ', a)
print('b: ', b)

# Calculating result
res = tf.math.multiply(x = a, y = b)

# Printing the result
print('Result: ', res)