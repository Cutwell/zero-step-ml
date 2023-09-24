from zero_step_ml.src.main import main


def test_auto_insurance_sweden():
    print("\ntest_auto_insurance_sweden: ")
    main("zero_step_ml/tests/AutoInsurSweden.csv")


def test_pima_indians_diabetes():
    print("\ntest_pima_indians_diabetes: ")
    main("zero_step_ml/tests/pima-indians-diabetes.csv")
