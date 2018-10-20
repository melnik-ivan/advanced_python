#include <Python.h>

long fib(long x) {
    if (x == 0)
        return 0;

    if (x == 1)
        return 1;

    if (x > 0)
        return fib(x-1)+fib(x-2);

    return -1;
}

static PyObject *
fibonacci_n(PyObject *self, PyObject *args)
{
    long num;

    if (!PyArg_ParseTuple(args, "l", &num))
    {
        return NULL;
    }

    return PyLong_FromLong(fib(num));
}

static PyMethodDef FibMethods[] = {
    {"fibonacci_n", fibonacci_n, METH_VARARGS, "Calculate n-th Fibonacci number"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef fibonacci =
{
    PyModuleDef_HEAD_INIT,
    "fibonacci_n", "", -1, FibMethods
};

PyMODINIT_FUNC PyInit_fibonacci(void)
{
    return PyModule_Create(&fibonacci);
}
