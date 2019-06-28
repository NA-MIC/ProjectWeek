# Slicer FEniCS Installation

## Variables

Set paths to Slicer and FEniCS

    MY_SLICER_DIR=/opt/slicer/Slicer-4.11.0-2019-06-24-linux-amd64/
    MY_FENICS_SRC=~/projects/fenics/fenics-2019.1.0/
    MY_FENICS_DIR=/opt/fenics/fenics-2019.1.0/

## Install Python header files

Use this to check your Slicer Python version

    ${MY_SLICER_DIR}/bin/PythonSlicer --version

Download and install Python header files

    wget -P ${MY_SLICER_DIR}/lib/Python/include/python3.6m/ https://github.com/python/cpython/archive/v3.6.7.tar.gz
    cd ${MY_SLICER_DIR}/lib/Python/include/python3.6m/
    tar --strip-components=2 -zxf v3.6.7.tar.gz cpython-3.6.7/Include

## Install FEniCS in Slicer

The following instructions assume that FEniCS has been installed in
`${MY_FENICS_DIR}`.

Set DOLFIN environment variables

    source ${MY_FENICS_DIR}/share/dolfin/dolfin.conf

Install FEniCS Python components from source

    ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install ${MY_FENICS_SRC}/fiat
    ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install ${MY_FENICS_SRC}/dijitso
    ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install ${MY_FENICS_SRC}/ufl
    ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install ${MY_FENICS_SRC}/ffc
    ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install ${MY_FENICS_SRC}/dolfin/python
    ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install ${MY_FENICS_SRC}/mshr/python

## Run Slicer

    ${MY_SLICER_DIR}/Slicer
