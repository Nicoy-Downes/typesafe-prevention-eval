import pandas as pd
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay,
)
import matplotlib.pyplot as plt
from config import OPTION_A_MAP, OPTION_B_MAP, HUMAN_LABELS, OPTION_B_LABELS

EXCEL_PATH = "../Prevention_dataset evaluation.xlsx"



def plot_and_print(y_true, y_pred, labels, title, filename):
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    print(f"  {title}")
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, labels=labels, zero_division=0))

    fig, ax = plt.subplots(figsize=(max(6, len(labels) * 1.5), max(5, len(labels) * 1.2)))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot(ax=ax, colorbar=True, xticks_rotation=30)
    ax.set_title(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
    print(f"Saved plot: {filename}")


def main():
    print("Loading Excel file...")
    df = pd.read_excel(EXCEL_PATH)
    print(f"Loaded {len(df)} rows.\n")

    required = {"Prevention Code", "typesafe_optiona", "typesafe_optionb"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(
            f"Missing columns: {missing}. Run experiment.py first to generate typesafe labels."
        )

    y_human = df["Prevention Code"].astype(str)

    # --- Option A vs Human (direct mapping) ---
    y_a = df["typesafe_optiona"].astype(str).map(OPTION_A_MAP)
    unmapped_a = y_a.isna().sum()
    if unmapped_a:
        print(f"Warning: {unmapped_a} Option A labels could not be mapped and will be dropped.")
    mask_a = y_a.notna()
    plot_and_print(
        y_human[mask_a],
        y_a[mask_a],
        HUMAN_LABELS,
        "Option A vs Human Labels",
        "confusion_matrix_optiona.png",
    )

    # --- Option B vs Human (collapsed to 4-class scheme) ---
    y_b_collapsed = df["typesafe_optionb"].astype(str).map(OPTION_B_MAP)
    unmapped_b = y_b_collapsed.isna().sum()
    if unmapped_b:
        print(f"Warning: {unmapped_b} Option B labels could not be mapped and will be dropped.")
    mask_b = y_b_collapsed.notna()
    plot_and_print(
        y_human[mask_b],
        y_b_collapsed[mask_b],
        HUMAN_LABELS,
        "Option B (collapsed) vs Human Labels",
        "confusion_matrix_optionb_collapsed.png",
    )

    # --- Option B fine-grained (raw 5-class labels vs human, where human acts as reference) ---
    # Shows how the 5 Option B categories distribute across human labels
    y_b_raw = df["typesafe_optionb"].astype(str)
    present_b_labels = [l for l in OPTION_B_LABELS if l in y_b_raw.values]
    present_human_labels = [l for l in HUMAN_LABELS if l in y_human.values]

    print("  Option B raw label distribution vs Human Labels")
    cross_tab = pd.crosstab(
        y_human, y_b_raw, rownames=["Human"], colnames=["Option B"]
    )
    print(cross_tab.to_string())
    cross_tab.to_csv("optionb_crosstab.csv")
    print("\nSaved cross-tabulation: optionb_crosstab.csv")

    #Summary of agreement
    print("  Summary")
    agree_a = (y_human[mask_a].values == y_a[mask_a].values).mean()
    agree_b = (y_human[mask_b].values == y_b_collapsed[mask_b].values).mean()
    print(f"Option A overall accuracy: {agree_a:.1%}")
    print(f"Option B overall accuracy (collapsed): {agree_b:.1%}")


if __name__ == "__main__":
    main()
