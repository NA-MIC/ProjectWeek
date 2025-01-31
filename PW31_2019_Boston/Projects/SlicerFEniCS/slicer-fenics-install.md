# Slicer FEniCS Installation

The following instructions assume that the FEniCS C++ components have been installed in
`${MY_FENICS_DIR}`.
For FEniCS installation instructions see:
- <https://gitlab.com/benzwick/fenics-debian>
- <https://fenicsproject.org/download>
- <https://fenics.readthedocs.io/en/latest/installation.html>

## Variables

Set paths to Slicer and FEniCS

    MY_SLICER_DIR=/opt/slicer/Slicer-4.11.0-2019-06-24-linux-amd64/
    MY_FENICS_SRC=~/projects/fenics/fenics-2019.1.0/
    MY_FENICS_DIR=/opt/fenics/fenics-2019.1.0/

Set Python dependency versions

    MPI4PY_VERSION="==3.0.1"
    PETSC4PY_VERSION="==3.11.0"
    SLEPC4PY_VERSION="==3.11.0"

## Install Python header files

Use this to check your Slicer Python version

    ${MY_SLICER_DIR}/bin/PythonSlicer --version

Download and install Python header files

    wget -P ${MY_SLICER_DIR}/lib/Python/include/python3.6m/ https://github.com/python/cpython/archive/v3.6.7.tar.gz
    cd ${MY_SLICER_DIR}/lib/Python/include/python3.6m/
    tar --strip-components=2 -zxf v3.6.7.tar.gz cpython-3.6.7/Include

## Install FEniCS in Slicer

Set DOLFIN environment variables

    source ${MY_FENICS_DIR}/share/dolfin/dolfin.conf

Install Python dependencies

    ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install mpi4py${MPI4PY_VERSION}
    ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install petsc4py${PETSC4PY_VERSION}
    ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install slepc4py${SLEPC4PY_VERSION}

Install FEniCS Python components from source

    ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install ${MY_FENICS_SRC}/fiat
    ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install ${MY_FENICS_SRC}/dijitso
    ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install ${MY_FENICS_SRC}/ufl
    ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install ${MY_FENICS_SRC}/ffc
    ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install ${MY_FENICS_SRC}/dolfin/python
    ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install ${MY_FENICS_SRC}/mshr/python

## Run Slicer

    source ${MY_FENICS_DIR}/share/dolfin/dolfin.conf
    ${MY_SLICER_DIR}/Slicer
