import pandas as pd
import re

def load_google_sheet(spreadsheet_url: str, sheet_names: list[str]) -> dict[str, pd.DataFrame]:
    """
    Given a Google Sheets share link and list of sheet names,
    fetch each sheet as CSV and return dict of DataFrames.
    """
    match = re.search(r"/spreadsheets/d/([a-zA-Z0-9-_]+)", spreadsheet_url)
    if not match:
        raise ValueError("Invalid Google Sheets URL")
    spreadsheet_id = match.group(1)

    sheets = {}
    for sheet in sheet_names:
        export_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?tqx=out:csv&sheet={sheet}"
        df = pd.read_csv(export_url)
        sheets[sheet] = df
    return sheets

