import pandas as pd
import re

PII_PATTERNS = {
    'email': r'\S+@\S+',
    'phone': r'\+?\d[\d\s()-]{7,}',
    'name': r'^[A-Z][a-z]+$'  # crude name match
}

def check_privacy(df):
    violations = {}
    for col in df.columns:
        sample = df[col].astype(str).str.cat(sep=' ')
        for label, pattern in PII_PATTERNS.items():
            if re.search(pattern, sample):
                violations[col] = label
                break
    score = 100 - (len(violations) * 20)
    return max(score, 0), violations
