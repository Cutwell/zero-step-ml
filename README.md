<h1 align="center">
  <img src="logo.png" style="width:280px">
  <br/>
  Zero Step ML
</h1>

<p align="center">
   Fully automated machine learning using LLMs.
</p>

<br />

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
