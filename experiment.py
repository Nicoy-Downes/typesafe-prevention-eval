import pandas as pd
from config import OPTION_A_CRITERIA, OPTION_B_CRITERIA
from typesafe_sdk import Choice, TypeSafeClient

EXCEL_PATH = "../Prevention_dataset evaluation.xlsx"

def label_text(client: TypeSafeClient, text: str, criteria: dict, question_key: str) -> str:
    response = client.system_one(
        state={"text": text},
        questions={
            question_key: Choice(
                instructions="Which category best describes this research abstract in terms of disease prevention?",
                criteria=criteria,
            )
        },
    )
    return response.answers[question_key].choice


def run_option(df: pd.DataFrame, criteria: dict, column_name: str) -> pd.DataFrame:
    results = []
    total = len(df)
    with TypeSafeClient() as client:
        for i, row in df.iterrows():
            text = str(row["combined_summary"])
            label = label_text(client, text, criteria, "prevention_category")
            results.append(label)
            if (i + 1) % 10 == 0:
                print(f"  {i + 1}/{total} done")
    df[column_name] = results
    return df


def main():
    print("Loading Excel file...")
    df = pd.read_excel(EXCEL_PATH)
    print(f"Loaded {len(df)} rows.\n")

    print("Running Option A labeling...")
    df = run_option(df, OPTION_A_CRITERIA, "typesafe_optiona")
    print("Option A complete.\n")

    print("Running Option B labeling...")
    df = run_option(df, OPTION_B_CRITERIA, "typesafe_optionb")
    print("Option B complete.\n")

    print("Saving results to Excel...")
    df.to_excel(EXCEL_PATH, index=False)
    print(f"Saved to {EXCEL_PATH}")
    print("\nOption A value counts:")
    print(df["typesafe_optiona"].value_counts())
    print("\nOption B value counts:")
    print(df["typesafe_optionb"].value_counts())


if __name__ == "__main__":
    main()
