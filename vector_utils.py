import numpy as np


def vector_addition(v1, v2):
    return np.array(v1) + np.array(v2)


def dot_product(v1, v2):
    return np.dot(np.array(v1), np.array(v2))


def magnitude(v):
    return np.linalg.norm(np.array(v))


def cosine_similarity(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)

    v1_magnitude = np.linalg.norm(v1)
    v2_magnitude = np.linalg.norm(v2)

    if v1_magnitude == 0 or v2_magnitude == 0:
        return 0

    return np.dot(v1, v2) / (v1_magnitude * v2_magnitude)