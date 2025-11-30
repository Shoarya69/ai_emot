# setup.py
from setuptools import setup, Extension
import pybind11

ext = Extension(
    "esp32_module",
    ["conn_esp32.cpp"],
    include_dirs=[pybind11.get_include()],
    language="c++"
)

setup(
    name="esp32_conn",
    ext_modules=[ext],
)
