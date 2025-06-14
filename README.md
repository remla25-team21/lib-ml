# lib-ml

A machine learning library for REMLA project that provides text preprocessing functionality for sentiment analysis.

## Installation

```bash
pip install git+https://github.com/remla25-team21/lib-ml.git@v1.0.0
```

Check for the latest release version.

## Usage

```python
from libml.preprocessing import preprocess_train, preprocess_inference

# For training
X_train, X_test, y_train, y_test = preprocess_train(
    dataset_filepath="data.tsv", 
    test_size=0.2,
    random_state=0
)

# For inference
processed_data = preprocess_inference("data.tsv", "c1_BoW_Sentiment_Model.pkl")
```

## Development

This project uses modern Python packaging with `pyproject.toml`. To set up for development:

```bash
# Clone the repository
git clone https://github.com/remla25-team21/lib-ml.git

# Change to the project directory
cd lib-ml

# Install in development mode with dev dependencies
pip install -e ".[dev]"
```
