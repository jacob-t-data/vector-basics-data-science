# Vector Similarity Fundamentals for Data Science

This project is part of my journey learning data science in public.

---

## Overview

This project explores vector operations using Python and NumPy.

Topics include:
- Vector addition
- Dot products
- Magnitude
- Cosine similarity

---

## Features

This project allows users to:

- Create and manipulate vectors using NumPy
- Compute vector addition
- Calculate dot products
- Measure vector magnitude
- Compare vectors using cosine similarity

The recommendation example allows users to modify preference vectors and compare similarity scores between different items.

---

## Example Use Case

Below is a simple recommendation system example:

The program compares:
- a user preference vector
- against multiple movie feature vectors

It then calculates cosine similarity scores and recommends the closest match.

Example:

```python

import numpy as np

user = np.array([5, 3, 0])
movie_1 = np.array([4, 3, 0])
movie_2 = np.array([1, 0, 5])
```

Output:

```text
Movie 1 similarity: 0.995
Movie 2 similarity: 0.168
Recommended: Movie 1
```

---

## Customization

Users can modify the vectors in the recommendation example to test different similarity scenarios.

Example:

```python
user = np.array([YOUR_VALUES])
```

This allows experimentation with:
- recommendation systems
- similarity measurements
- vector relationships

---

## Tools Used

- Python
- NumPy
- Jupyter Notebook

---

## Project Structure

```text
vector-basics-data-science/
│
├── README.md
├── requirements.txt
├── vector_utils.py
├── vector_project.ipynb
│
└── examples/
    └── recommendation_example.py
```

---

## How to Run This Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Open the Jupyter Notebook:

```bash
jupyter notebook vector_project.ipynb
```

Run the recommendation example:

```bash
python examples/recommendation_example.py
```


---

## Future Improvements

- Add data visualizations
- Add user input directly from terminal
- Expand recommendation system complexity
- Connect vector similarity to machine learning workflows