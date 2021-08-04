# Note: The order of the imports here is crucial because in distutils-land, everything
# is about monkey-patching each others' work.
from setuptools.dist import Distribution
from setuptools import setup
from distutils.extension import Extension
from pythran.dist import PythranExtension, PythranBuildExt
from Cython.Build import cythonize
from setuptools_rust import Binding, RustExtension

Distribution(dict(setup_requires="pythran"))

setup(
    ext_modules=[PythranExtension("collatzpythran", ["collatzpythran.py"])]
    + cythonize(
        Extension("collatzcython", ["collatzcython.pyx"], extra_compile_args=["-O3"])
    ),
    rust_extensions=[
        RustExtension(
            "collatzpyo3", path="collatzpyo3/Cargo.toml", binding=Binding.PyO3
        )
    ],
)
