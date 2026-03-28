import pandas as pd

data = {
    "date": ["2026-03-01", "2026-03-01", "2026-03-02",
             "2026-04-01", "2026-04-02", "2026-04-02"],
    "sales": [100, 150, 200, 300, 250, 100]
}

df = pd.DataFrame(data)

# Convert to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)