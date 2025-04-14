from fairlearn.metrics import MetricFrame, selection_rate
import pandas as pd

def check_bias(df, sensitive_col='gender', label_col='hired'):
    y_true = df[label_col]
    y_pred = df[label_col]  # Assuming no model, just using output as prediction for demo
    metric = MetricFrame(metrics=selection_rate,
                         y_true=y_true,
                         y_pred=y_pred,
                         sensitive_features=df[sensitive_col])
    disparity = metric.difference()
    score = max(0, 100 - disparity * 100)
    return score, metric.by_group.to_dict()
