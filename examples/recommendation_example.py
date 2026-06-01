import sys
from pathlib import Path
import numpy as np

# Allow imports from parent directory
sys.path.append(str(Path(__file__).resolve().parents[1]))

from vector_utils import cosine_similarity

# User preference vector
user = np.array([5, 3, 0])

# Movie feature vectors
movie_1 = np.array([4, 3, 0])
movie_2 = np.array([1, 0, 5])

movie_1_score = cosine_similarity(user, movie_1)
movie_2_score = cosine_similarity(user, movie_2)

print("Movie 1 similarity:", round(movie_1_score, 3))
print("Movie 2 similarity:", round(movie_2_score, 3))

print("\nFinal Recommendation:\n")

if movie_1_score > movie_2_score:
    print("Recommended: Movie 1")
    print()
elif movie_2_score > movie_1_score:
    print("Recommended: Movie 2")
    print()
else:
    print("Both movies are equally similar.")
    print()