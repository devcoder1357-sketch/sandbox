import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Print first 10 rows of an Excel file")
    parser.add_argument("file", help="Path to Excel file (.xlsx, .xls)")
    parser.add_argument("--sheet", default=0, help="Sheet name or index (default: 0)")
    args = parser.parse_args()

    try:
        import pandas as pd
    except ImportError:
        print("Missing dependency: pandas. Install with: pip install pandas openpyxl", file=sys.stderr)
        sys.exit(1)

    try:
        df = pd.read_excel(args.file, sheet_name=args.sheet, engine="openpyxl")
    except Exception as e:
        print(f"Failed to read Excel file: {e}", file=sys.stderr)
        sys.exit(1)

    print(df.head(10).to_string(index=False))

if __name__ == "__main__":
    main()