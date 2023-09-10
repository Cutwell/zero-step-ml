# <img src="./zero-step-ml.png" style="width:128px;padding-right:20px;margin-bottom:-8px;">Zero Step ML
 Fully automated machine learning using LLMs.

## How it works

1. LLM analyses the column headers and predicts A) ML task (classification/regression), B) feature columns, C) target column.
2. Data is preprocessed and trained according to identified task type.
3. Model metrics are analysed and summarised in natural language.

## Install

1. Clone this repository locally.
2. Create `.envrc` and set `OPENAI_API_KEY`.
3. Install with poetry.

```bash
make install    # Install dependencies
make test       # Run unit tests to check installation
```

## Usage

1. Obtain your dataset (supported file types: CSV) (supported ML tasks: classification, regression).
2. Run `poetry run zero_step_ml --target="my_dataset.csv"`

## License

MIT
