def precision(predicted, actual):
    return len(set(predicted) & set(actual)) / len(predicted) if predicted else 0

def recall(predicted, actual):
    return len(set(predicted) & set(actual)) / len(actual) if actual else 0

def f1_score(p, r):
    return (2 * p * r) / (p + r) if (p + r) else 0