#include "lists.h"
#include "Python.h"

void print_python_list_info(PyObject *p)
{
	int i = 0;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject*)(p))->allocated);

	while (i < Py_SIZE)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		i++;
	}
}
