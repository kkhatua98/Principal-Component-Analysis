# -*- coding: utf-8 -*-
"""
Created on Mon May  3 09:50:41 2021

@author: kkhatua
"""

from scipy.special import kolmogorov
import numpy


n = 5
d = 0.326

n = 5
sample = [-1.2, 0.2, -0.6, 0.8, -1.0]

phi_sample = numpy.array([0.115, 0.159, 0.274, 0.580, 0.788])

DPlus = ((numpy.arange(1.0, n + 1) / n) - phi_sample).max()
DMinus = (phi_sample - (numpy.arange(0.0, n) / n)).max()

d = max([DPlus, DMinus])


scipy_value = kolmogorov(numpy.sqrt(n) * d)




def summer(x):
    arr = numpy.arange(1, 1001)
    constant_quantity = -2 * x * x
    power_array = constant_quantity * arr * arr
    alternate_array = numpy.array([1, -1] * 500)
    powered_array = numpy.exp(power_array)
    
    return 1 - (2 * sum(alternate_array * powered_array))

manually_calculated_value = 1 - summer(numpy.sqrt(n) * d)