
import ctypes

dll = ctypes.CDLL("./module/program.dll")

dll.getVisiableProgram.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_wchar))
dll.getArrayLength.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_wchar))]
dll.getArrayLength.restype = ctypes.c_int
dll.freeArray.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_wchar))]

def getVisiableProgram() :
    data = dll.getVisiableProgram()
    program_list = []

    for i in range(dll.getArrayLength(data)) :
        program_list.append(ctypes.cast(data[i], ctypes.c_wchar_p).value)

    dll.freeArray(data)

    return program_list