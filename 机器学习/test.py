# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/5/21  21:16 
# 名称：test.PY
# 工具：PyCharm
# import tensorflow as tf
import torch

x = torch.rand(5, 3)
print(x)
print(torch.cuda.is_available())

# print(tf.reduce_sum(tf.random.normal([1000, 1000])))
# hello = tf.constant('Hello tensorflow')
# sess = tf.compat.v1.Session()
# print(sess.run(hello))
