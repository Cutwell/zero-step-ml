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

## Testing

Performance on popular datasets:

|Dataset|Identified task|Identified features|Identified target|Model|Metrics|LLM metric summary|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|[Auto insurance in Sweden](https://college.cengage.com/mathematics/brase/understandable_statistics/7e/students/datasets/slr/frames/slr06.html)|Regression|`['number of claims']`|`'total payment for all the claims in thousands of Swedish Kronor'`|Linear Regression|`{'MAE': 26.41490933996047, 'MSE': 875.0434234424166, 'R2 Score': 0.89508194939184}`|The model was tested on a regression task and achieved an MAE of 26.41490933996047, an MSE of 875.0434234424166, and an R2 Score of 0.89508194939184. This indicates that the model is performing well, as the MAE is relatively low and the R2 Score is close to 1, indicating a strong correlation between the predicted and actual values.|
|[Pima Indians Diabetes](https://github.com/jbrownlee/Datasets/blob/master/pima-indians-diabetes.csv)|Classification|`['Number of times pregnant', 'Plasma glucose concentration a 2 hours in an oral glucose tolerance test', 'Diastolic blood pressure (mm Hg)', 'Triceps skinfold thickness (mm)', '2-Hour serum insulin (mu U/ml)', 'Body mass index (weight in kg/(height in m)^2)', 'Diabetes pedigree function', 'Age (years)']`|`'Class variable (0 or 1)'`|Decision Tree Classifier|`{'Accuracy': 0.7597402597402597, 'Precision': 0.65, 'Recall': 0.7090909090909091, 'F1 Score': 0.6782608695652174}`|The model achieved an accuracy of 0.7597402597402597, which indicates that it was able to correctly classify 75.97% of the data. The precision of the model was 0.65, meaning that 65% of the predictions made by the model were correct. The recall of the model was 0.7090909090909091, meaning that it was able to correctly identify 70.91% of the positive cases. Finally, the F1 score of the model was 0.6782608695652174, which is a measure of the model's accuracy and precision combined. Overall, the model performed well, with a good balance of accuracy and precision.|
|[Banknote authentication](https://archive.ics.uci.edu/dataset/267/banknote+authentication)|Classification|`['Variance of Wavelet Transformed image (continuous)', 'Skewness of Wavelet Transformed image (continuous)', 'Kurtosis of Wavelet Transformed image (continuous)', 'Entropy of image (continuous)']`|`'Class (0 for authentic and 1 for inauthentic)'`|Decision Tree Classifier|`{'Accuracy': 0.9781818181818182, 'Precision': 0.991869918699187, 'Recall': 0.9606299212598425, 'F1 Score': 0.976}`|The model achieved an accuracy of 0.978, precision of 0.991, recall of 0.961, and an F1 score of 0.976 on the classification task. This indicates that the model is performing well, as all of the metrics are above 0.9. The accuracy score indicates that the model is correctly classifying the data with a high degree of accuracy. The precision score indicates that the model is correctly identifying the positive class with a high degree of accuracy. The recall score indicates that the model is correctly identifying the positive class with a high degree of accuracy. Finally, the F1 score indicates that the model is performing well overall, as it is a combination of the precision and recall scores.|

## License

MIT
