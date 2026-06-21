# Raw-KNN: Software Defect Prediction from Scratch

This repository contains a raw, zero-dependency implementation of the **K-Nearest Neighbors (KNN)** algorithm built entirely from scratch using Python. The primary objective of this project is to demonstrate a fundamental understanding of machine learning architectures, spatial distance computations, and lazy learning paradigms without relying on high-level abstraction libraries like `scikit-learn`.

The model is utilized to perform software defect prediction based on static code metrics.

## Core Features
* **Zero External ML Dependencies:** Built using only Python's standard libraries (`csv`, `math`, `random`).
* **Custom Spatial Calculation:** Implements the Euclidean distance (L2 Norm) mathematical function from scratch.
* **Algorithmic Voting System:** Uses majority voting to determine the final classification of K nearest neighbors.
* **Modular Architecture:** Adheres to the Separation of Concerns (SoC) principle by splitting mathematical utilities, machine learning logic, and the execution pipeline into distinct modules.

## Dataset: NASA PROMISE (KC2)
The model is trained and evaluated on the **KC2 dataset** from the empirical software engineering repository, NASA PROMISE. 
* **Source:** [NASA PROMISE Dataset Repository on Kaggle](https://www.kaggle.com/datasets/shaily20/nasa-promise-dataset-repository-main)
* **Domain:** Science data processing subsystem (C++).
* **Total Instances:** 522 modules.
* **Features:** Numerical static code metrics (e.g., McCabe's Cyclomatic Complexity, Halstead metrics).
* **Target Label:** Binary classification (`1` = Defective/Bug-prone, `0` = Clean/Safe).

> **Note on Data Preprocessing:** The original dataset utilizes `true`/`false` strings for its target labels and semicolons (`;`) as delimiters. The dataset used in this repository has been manually preprocessed: boolean text is mapped to binary integers (`1` and `0`) to facilitate mathematical voting computations.

## Repository Structure
* `kc2.csv` : Preprocessed NASA PROMISE dataset
* `math_utils.py` : Low-level mathematical operations (Euclidean Distance)
* `knn_model.py` : Core KNN algorithm (Lazy learning, distance sorting, voting)
* `main.py` : Main execution controller, data parser, and evaluation pipeline
* `README.md` : Project documentation

## Installation & Usage

Since this project requires no external dependencies (like `numpy` or `pandas`), the setup process is straightforward. Ensure you have Python 3.x installed on your system.

1. Clone the repository:
   git clone https://github.com/Kuzhano/ProjectBase_NearestNeighbour.git
   cd ProjectBase_NearestNeighbour

2. Run the evaluation pipeline:
   python main.py

## Evaluation & Results
The algorithm performs a random shuffle and splits the dataset into an 80:20 ratio (Training and Testing). The K hyperparameter is set to **5** to prevent tie votes during classification. 

Based on the execution benchmark, the model achieves the following metrics:
* **Total Training Data:** 417 rows
* **Total Testing Data:** 105 rows
* **Correct Predictions:** 85 instances
* **Global Accuracy:** 80.95%
* **Execution Time:** ~0.94 seconds

## Algorithmic Detail
The core of this model relies on the **Euclidean Distance** formula to map the spatial similarity between the unclassified code metrics (test data) and historical code metrics (training data). 

The mathematical implementation in `math_utils.py` mirrors the standard Euclidean distance equation for multi-dimensional space, calculating the square root of the sum of the squared differences between corresponding features.
