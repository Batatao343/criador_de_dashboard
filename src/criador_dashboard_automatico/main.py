#!/usr/bin/env python
import sys
import warnings
import pandas as pd
from datetime import datetime
from criador_dashboard_automatico.crew import CriadorDashboardAutomatico

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(file_path: str):
    """
    Run the crew.
    """
    try:
        output = CriadorDashboardAutomatico().crew().kickoff(inputs={"file_path": file_path})
        print("Crew Output:")
        return output
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train(file_path: str):
    """
    Train the crew for a given number of iterations.
    """
    try:
        CriadorDashboardAutomatico().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs={"file_path": file_path}
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay(file_path: str):
    """
    Replay the crew execution from a specific task.
    """
    try:
        CriadorDashboardAutomatico().crew().replay(
            task_id=sys.argv[1],
            inputs={"file_path": file_path}
        )
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test(file_path: str):
    """
    Test the crew execution and return the results.
    """
    try:
        CriadorDashboardAutomatico().crew().test(
            n_iterations=int(sys.argv[1]),
            openai_model_name=sys.argv[2],
            inputs={
                "current_year": str(datetime.now().year),
                "file_path": file_path
            }
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    mode = sys.argv[1]
    file_path = sys.argv[2]

    if mode == "run":
        print(run(file_path))
    elif mode == "train":
        train(file_path)
    elif mode == "replay":
        replay(file_path)
    elif mode == "test":
        test(file_path)
    else:
        print("Modo invalido. Use: run | train | replay | test")


