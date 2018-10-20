#include <Python.h>

long long fib(int num) {
    long long result = 0;
    long long prev_results_0 = 0;
    long long prev_results_1 = 0;
    
    if (num == 0) {
        return 0;
    }

    if (num > 0) {
        for (int i = 0; i < num; i++) {
            result = prev_results_0 + prev_results_1;
            if (0 == result) {
                result = 1;
            }
            prev_results_0 = prev_results_1;
            prev_results_1 = result;
        }
        return result;
    }

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
