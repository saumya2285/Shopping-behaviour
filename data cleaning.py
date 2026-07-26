import pandas as pd
from pathlib import Path

BASE = Path(__file__).parent
INPUT = BASE / 'customer_shopping_behavior.csv'

try:
    df = pd.read_csv(INPUT)
except FileNotFoundError:
    print(f'File not found: {INPUT}')
    raise

print(df.head())
print(df.info())
print(df.describe(include='all'))
print(df.isnull().sum())
df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.mean()))

df.columns=df.columns.str.strip().str.replace(' ', '_').str.lower()
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)

labels=['young adult','adult','middle aged','senior']
df['age_group']=pd.qcut(df['age'], q=4, labels=labels)
print(df[['age','age_group']].head(10))

frequency_mapping={
    'Fortnightly':14,
    'Monthly':30,
    'Quarterly':90,
    'Weekly':7,
    'Annually':365,
    'Bi-Weekly':14,
    'Every 3 Months':90
}
df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)
print(df[['frequency_of_purchases','purchase_frequency_days']].head(10))

df=df.drop('promo_code_used',axis=1)
                    

# Example modification and save
df['processed'] = True
OUTPUT = BASE / 'customer_shopping_behavior_modified.csv'
df.to_csv(OUTPUT, index=False)
print('Saved modified CSV to', OUTPUT)


