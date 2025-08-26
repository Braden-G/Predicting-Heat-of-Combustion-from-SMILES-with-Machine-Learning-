# ML Prediction of Heat of Combustion for Chemical Compounds

This project demonstrates the use of machine learning to predict the heat of combustion for chemical compounds using molecular representations and a variety of regression models. It is designed to showcase best practices in data science, feature engineering, and model evaluation.

---

## Project Overview

- **Feature Engineering:**
  - ECFP4 fingerprints (RDKit)
  - chemBERTa embeddings (HuggingFace Transformers)
- **Models:**
  - Random Forest, XGBoost, SVM, Neural Networks (including CNN)
- **Evaluation:**
  - Cross-validation, test set evaluation, and metrics (MSE, MAE, R²)
- **Data:**
  - Synthetic and real datasets
  - Data cleaning and preparation scripts

---

## Professional Organization Plan

### 1. Repository Structure

```
.
├── data/                # Raw and processed datasets (with README)
├── notebooks/           # Jupyter notebooks (main and exploratory)
│   └── Model.ipynb
├── src/                 # Source code (feature extraction, modeling, utils)
├── scripts/             # Standalone scripts for data prep, training, etc.
├── embeddings/          # Precomputed embedding files
├── DataPrep/            # To be refactored into src/scripts
├── requirements.txt     # Python dependencies
├── README.md            # Project overview and instructions
├── LICENSE
└── .gitignore
```

### 2. Refactoring Plan

- **notebooks/**
  - Move `Model.ipynb` and any exploratory notebooks here.
  - Keep notebooks clean, focused, and well-commented.
- **src/**
  - Refactor reusable code (feature extraction, model training, evaluation) into Python modules.
  - Example: `src/features.py`, `src/models.py`, `src/utils.py`
- **scripts/**
  - Convert data preparation and processing notebooks/scripts in `DataPrep/ParsingScripts/` into standalone Python scripts.
  - Provide CLI arguments for flexibility.
- **data/**
  - Store only non-sensitive, non-proprietary sample data.
  - Add a README describing data sources and usage.
- **embeddings/**
  - Store precomputed embeddings for reproducibility.
- **requirements.txt**
  - List all dependencies (RDKit, scikit-learn, transformers, tensorflow, etc.).
- **README.md**
  - Add project description, setup instructions, usage examples, and results summary.
- **LICENSE**
  - Add an open-source license (e.g., MIT).
- **.gitignore**
  - Ignore large files, data, and environment files.

### 3. Documentation & Best Practices

- Add docstrings and comments to all scripts and modules.
- Use consistent naming conventions and code formatting (e.g., PEP8).
- Provide example commands for running scripts and notebooks.
- Summarize results and findings in the README.
- Optionally, add unit tests for core functions.

---

## Quick Start

1. Clone the repository
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the main notebook in `notebooks/Model.ipynb` or use scripts in `src/` and `scripts/` for modular workflows.

---

## Results Summary

See the main notebook for detailed results, including model performance metrics and visualizations.

---

## License

This project is licensed under the MIT License.
