"""Evaluate SemTab-2023-CQA predicions

Usage:
    python3 evaluate.py solution_csv prediction_csv
"""
import csv

def score(solution_csv, prediction_csv):
    gold_rows = csv.reader(open(solution_csv).readlines()[1:])
    gold = {
        (f, sc, oc, qc): (p, q)
        for f, sc, oc, qc, p, _, q, _ in gold_rows
    }
    pred_rows = csv.reader(open(prediction_csv).readlines()[1:])
    pred = {
        (f, sc, oc, qc): (p, q)
        for f, sc, oc, qc, p, _, q, _ in pred_rows
    }
    n_correct = sum(int(pred.get(g) == pq) for g, pq in gold.items())
    return n_correct / len(gold)
    

if __name__ == '__main__':
    import sys
    try:
        _, solution_csv, prediction_csv = sys.argv
        print(score(solution_csv, prediction_csv))
        
    except:
        print(__doc__)