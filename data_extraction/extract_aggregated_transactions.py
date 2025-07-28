import os, json
import pandas as pd

def extract_aggregated_transactions(base_path):
    records = []
    for state in os.listdir(base_path):
        state_path = os.path.join(base_path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for quarter_file in os.listdir(year_path):
                file_path = os.path.join(year_path, quarter_file)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                for txn in data.get('data', {}).get('transactionData', []):
                    records.append({
                        "state": state,
                        "year": int(year),
                        "quarter": int(quarter_file.strip('q.json')),
                        "transaction_type": txn['name'],
                        "count": txn['paymentInstruments'][0]['count'],
                        "amount": txn['paymentInstruments'][0]['amount']
                    })
    return pd.DataFrame(records)

if __name__ == "__main__":
    path = "../pulse/data/aggregated/transaction/country/india/state"
    df = extract_aggregated_transactions(path)
    df.to_csv("../data/aggregated_transaction.csv", index=False)
    print("✅ Aggregated Transaction Data Saved.")
