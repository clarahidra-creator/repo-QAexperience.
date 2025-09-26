import argparse
import pandas as pd

def non_null(df, cols):
    for c in cols:
        if df[c].isna().any():
            raise AssertionError(f"Nulls found in column: {c}")

def unique(df, col):
    dups = df[df.duplicated(col, keep=False)]
    if not dups.empty:
        raise AssertionError(f"Duplicate {col} values found: {dups[col].tolist()}")

def reconcile(staging, warehouse, key='order_id', tol=0.01):
    # Missing in warehouse
    missing = staging[~staging[key].isin(warehouse[key])]
    if not missing.empty:
        raise AssertionError(f"Orders missing in warehouse: {missing[key].tolist()}")
    # Amount deltas
    merged = staging.merge(warehouse, on=key, how='inner')
    if 'amount' in merged.columns and 'amount_usd' in merged.columns:
        deltas = (merged['amount'] - merged['amount_usd']).abs() > tol
        if deltas.any():
            bad = merged.loc[deltas, key].tolist()
            raise AssertionError(f"Amount mismatches over tolerance for orders: {bad}")

def main(args):
    stg = pd.read_csv(args.staging, parse_dates=['order_date'])
    wh = pd.read_csv(args.warehouse, parse_dates=['order_date'])

    # Basic gates
    non_null(stg, ['order_id', 'order_date', 'amount'])
    unique(stg, 'order_id')

    # Business rules
    if (stg['amount'] <= 0).any():
        raise AssertionError("Found non-positive amounts in staging")

    # Reconciliation
    reconcile(stg, wh)

    print("✅ Data quality checks passed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--staging", required=True)
    parser.add_argument("--warehouse", required=True)
    args = parser.parse_args()
    main(args)