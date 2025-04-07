from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import os

ext_modules = [
        Extension(
        "fourier_integrals",
        ["fourier_integrals.pyx"],
        libraries=["m"],
        extra_compile_args=['-Xpreprocessor', '-fopenmp', '-I/usr/local/opt/libomp/include'],
        extra_link_args=['-L/usr/local/opt/libomp/lib', '-lomp'],
    )
]

setup(
    name='Cython routines for LODE power spectrum evaluation',
    ext_modules=cythonize(ext_modules),
)
