from zero_step_ml.src.main import analyse_schema


TEST_DATASET_NAME = "seeds_dataset.csv"
TEST_SCHEMA = [
    "Area",
    "Perimeter",
    "Compactness",
    "Length of kernel",
    "Width of kernel",
    "Asymmetry coefficient",
    "Length of kernel groove",
    "Class (1, 2, 3)",
]


def test_analyse_schema():
    print("\ntest_analyse_schema: ")

    analysis = analyse_schema(dataset_name=TEST_DATASET_NAME, schema=TEST_SCHEMA)

    print(analysis)
