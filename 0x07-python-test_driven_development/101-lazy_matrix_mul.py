#!/usr/bin/python3
"""This defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This returns the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): This is the first matrix.
        m_b (list of lists of ints/floats): This is the second matrix.
    """

    return (np.matmul(m_a, m_b))
