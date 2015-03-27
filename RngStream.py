#load RngStream dll library
from ctypes import *
RngStream = CDLL("./RngStream.dll")

#def corresponding structure
class RngStream_InfoState(Structure):
    _fields_ =[('Cg',c_double),
               ('Bg',c_double),             
               ('Ig',c_double),
               ('Anti',c_int),
               ('IncPrec',c_int),
               ('name',c_char_p)]

#initialize with pointer
RngStream.RngStream_CreateStream.restype = POINTER(RngStream_InfoState)
g = RngStream.RngStream_CreateStream()

#uniform [0,1]
RngStream.RngStream_RandU01.restype = c_double
print RngStream.RngStream_RandU01(g)


#RandInt [20,30]
RngStream.RngStream_RandInt.restype = c_int
i = c_int(20)
j = c_int(30)
print RngStream.RngStream_RandInt(g, i, j)
