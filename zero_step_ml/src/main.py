import argparse
import os
import json
import pandas as pd
from zero_step_ml.src.training import perform_classification, perform_regression
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain


with open(file=os.path.join(os.getcwd(), "zero_step_ml/src/prompts/analyse_schema.txt"), mode="r") as file:
    ANALYSE_SCHEMA_PROMPT = PromptTemplate(template=file.read(), input_variables=["dataset_name", "schema"])

with open(file=os.path.join(os.getcwd(), "zero_step_ml/src/prompts/analyse_ml_metrics.txt"), mode="r") as file:
    ANALYSE_ML_METRICS_PROMPT = PromptTemplate(template=file.read(), input_variables=["task", "metrics"])


def analyse_schema(dataset_name: str, schema: list[str]):
    """
    Analyse a CSV (via dataset name and headers) to identify features and targets.

    Arguments:
        dataset_name (str): filename of dataset.
        schema (list[str]): list of headers for each column in dataset.

    Returns:
        analysis (dict): dictionary containing "task" (ML task: regression/classification), "feature_names" (list of features), "target_name" (target column).

    """
    
    llm = OpenAI(temperature=0)
    llm_chain = LLMChain(prompt=ANALYSE_SCHEMA_PROMPT, llm=llm)

    analysis_json = llm_chain.run(
        dataset_name=dataset_name,
        schema=schema
    )

    analysis = json.loads(analysis_json)

    return analysis


def analyse_ml_metrics(task: str, metrics: dict):
    """
    Summarise ML model performance metrics into natural language.

    Arguments:
        task (str): ML task (regression/classification).
        metrics (dict): ML model metrics.

    Returns:
        summary (str): summarisation of metrics, in natural language.

    """

    llm = OpenAI(temperature=0)
    llm_chain = LLMChain(prompt=ANALYSE_ML_METRICS_PROMPT, llm=llm)

    summary = llm_chain.run(
        task=task,
        metrics=metrics
    )

    return summary

def cli():
    """
    Parse CLI arguments.

    Arguments:
        None

    Returns:
        None

    """

    parser = argparse.ArgumentParser(
        description="Perform automated ML on a target dataset, using LLMs."
    )
    parser.add_argument("--target", type=str, help="Filepath to target CSV.")
    args = parser.parse_args()

    main(
        args.target
    )


def main(target_csv: str):
    """
    Analyse an input dataset and perform fully automated machine learning classification / regression training.

    Arguments:
        target_csv (str): target CSV dataset (must contain headers).

    Returns:
        model (object): trained ML model (DecisionTreeClassifier / LinearRegression).
        metrics (dict): model performance metrics.

    """

    df = pd.read_csv(target_csv)
    df = df.dropna()

    headers = df.columns.tolist()

    analysis = analyse_schema(
        dataset_name=target_csv,
        schema=headers
    )

    print(f"Analysed dataset!\nML task: {analysis['task']}\nFeatures: {analysis['feature_names']}\nTarget: {analysis['target_name']}")

    match analysis["task"]:
        case "classification":
            from sklearn.tree import DecisionTreeClassifier
            classifier = DecisionTreeClassifier  # TODO: replace with LLM decision
            model, metrics = perform_classification(
                data=df,
                feature_names=analysis["feature_names"],
                target_name=analysis["target_name"],
                classifier=classifier
            )
        case "regression":
            model, metrics = perform_regression(
                data=df,
                feature_names=analysis["feature_names"],
                target_name=analysis["target_name"]
            )
        case _:
            raise Exception(f"LLM analysis error: {analysis['task']} is not a valid ML task.")  

    summary = analyse_ml_metrics(
        task=analysis["task"],
        metrics=metrics
    )

    print(f"Trained model!\nModel class: {model}\nMetrics: {metrics}\nLLM Summary: {summary}")

    return model, metrics
