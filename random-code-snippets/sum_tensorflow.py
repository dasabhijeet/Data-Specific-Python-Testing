#import tensorflow as tf

# Tensorflow version 1 code in tensorflow 2 code:

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

h = tf.constant("Hello")
w = tf.constant(" World!")
hw = h + w
with tf.Session() as sess:
   ans = sess.run(hw)
   print(ans)


# Tensorflow version 2

import tensorflow as tf
msg = tf.constant('Hello, TensorFlow 2')
tf.print(msg)