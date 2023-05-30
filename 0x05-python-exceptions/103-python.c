#include <Python.h>

void print_python_list(PyObject *p)
{
  Py_ssize_t size, i;
  PyObject *item;

  if (!PyList_Check(p))
    {
      printf("[ERROR] Invalid List Object\n");
      return;
    }

  size = PyList_Size(p);
  printf("[*] Python list info\n[*] Size of the Python List = %zd\n[*] Allocated = %zd\n", size, ((PyListObject *)p)->allocated);

  for (i = 0; i < size; i++)
    {
      item = PyList_GetItem(p, i);
      printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
  Py_ssize_t size, i;
  char *bytes_str;

  if (!PyBytes_Check(p))
    {
      printf("[ERROR] Invalid Bytes Object\n");
      return;
    }

  size = PyBytes_Size(p);
  bytes_str = PyBytes_AsString(p);

  printf("[.] bytes object info\n  size: %zd\n  trying string: %s\n", size, bytes_str);

  printf("first %d bytes:", (int)((size < 10) ? size : 10));
  for (i = 0; i < size && i < 10; i++)
    printf(" %.2x", (unsigned char)bytes_str[i]);
  printf("\n");
}

void print_python_float(PyObject *p)
{
  double value;

  if (!PyFloat_Check(p))
    {
      printf("[ERROR] Invalid Float Object\n");
      return;
    }

  value = PyFloat_AS_DOUBLE(p);
  printf("[.] float object info\n  value: %f\n", value);
}
