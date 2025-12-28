import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve,
    auc
)


def evaluate_model(model, X_test, y_test):
    """
    Evaluate trained model and save metrics & figures
    """

    # Predictions
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # ---- Classification report ----
    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    report_df.to_csv("tables/classification_report.csv")

    print("Evaluation metrics saved")

    # ---- Confusion Matrix ----
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.title("Confusion Matrix")
    plt.savefig("figures/confusion_matrix.pdf", bbox_inches="tight")
    plt.close()

    # ---- ROC Curve (binary: default vs non-default) ----
    # Convert multiclass target to binary INSIDE the function
    y_test_binary = (y_test != "Fully Paid").astype(int)

    fpr, tpr, _ = roc_curve(y_test_binary, y_prob)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
    plt.plot([0, 1], [0, 1], linestyle="--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve (Default vs Non-default)")
    plt.legend()
    plt.savefig("figures/roc_curve.pdf", bbox_inches="tight")
    plt.close()

    print("Evaluation figures saved")
