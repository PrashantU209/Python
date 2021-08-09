import numpy
from numpy.lib.function_base import median
from scipy import stats
import scipy
from scipy.stats.stats import mode
# def stats_values(arr):
my_array=[]
n=int(input())
for i in range(n):
    my_array.append(float(input()))
    arr=numpy.array(my_array)
# print(arr)
# stats_values()
def stats_values(arr):
    mean1=numpy.mean(arr, axis=0)
    print(mean1)
    median2=numpy.median(arr, axis=0)
    print(median2)
    standarddev=numpy.std(arr, axis=0)
    print(round(standarddev,2))
    var1=numpy.var(arr, axis=0)
    print(var1)
    mode1=stats.mode(arr)
    print(round(mode1[0][0],2))
    # x=mode1[0]
    # res=str(x)[1:-1]
    # print(res)
    intqr=stats.i
stats_values(arr)
