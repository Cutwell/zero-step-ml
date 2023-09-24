from zero_step_ml.src.main import analyse_ml_metrics


TEST_TASK = "classification"
TEST_METRICS = {
    "Accuracy": 0.7142857142857143,
    "Precision": 0.5846153846153846,
    "Recall": 0.6909090909090909,
    "F1 Score": 0.6333333333333333,
}


def test_analyse_ml_metrics():
    print("\ntest_analyse_ml_metrics: ")
    summary = analyse_ml_metrics(task=TEST_TASK, metrics=TEST_METRICS)
    print(summary)
