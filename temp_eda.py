import pandas as pd
df = pd.read_csv('raw_pre1.csv', sep='\s+', skiprows=[1,2,3,4], index_col=False)

df['Year'] = df['Year'].astype(int)
print("Year check: ", df['Year'].head().tolist())
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

df['Winter_Avg']       = df[['Jan', 'Feb', 'Dec']].mean(axis=1).round(4)
df['Summer_Avg']       = df[['Mar', 'Apr', 'May']].mean(axis=1).round(4)
df['Monsoon_Avg']      = df[['Jun', 'Jul', 'Aug', 'Sep']].mean(axis=1).round(4)
df['Post_Monsoon_Avg'] = df[['Oct', 'Nov']].mean(axis=1).round(4)
df['Annual_Avg']       = df[months].mean(axis=1).round(4)

threshold = df['Annual_Avg'].mean() + df['Annual_Avg'].std()
df['Is_Extreme'] = df['Annual_Avg'] > threshold

df['Decade'] = (df['Year'] // 10) * 10

print("\n=== Annual Avg (Fix 5) ===")
print(df[['Year', 'Annual_Avg']].head())

print("\n=== Decade Wise avg temp ===")
print(df.groupby('Decade')['Annual_Avg'].mean().round(4))

print("\n=== Top 10 Hottest and Coldest Years ===")
print(df[['Year', 'Annual_Avg']].nlargest(10, 'Annual_Avg').to_string(index=False))
print(df[['Year', 'Annual_Avg']].nsmallest(10, 'Annual_Avg').to_string(index=False))

print("\n=== Monthly Wise Historical Avg ===")
print(df[months].mean().round(4))

era1 = round(df[df['Year'] <= 1950]['Annual_Avg'].mean(), 4)
era2 = round(df[df['Year'] > 1950]['Annual_Avg'].mean(), 4)
diff = round(era2 - era1, 4)

print(f"\n1901-1950 Avg Temp : {era1} °C")
print(f"1951-2024 Avg Temp : {era2} °C")
print(f"Temerature Rise    : +{diff} °C")

df['Anomaly'] = (df['Annual_Avg'] - era1).round(4)

print("\n=== Anomaly Last 10 Years ===")
print(df[['Year', 'Annual_Avg']].tail(10))

print("\n=== Extreme Years (Above {threshold:.4f} °C) ===")
print(df[df['Is_Extreme']][['Year', 'Annual_Avg']].to_string(index=False))

df.to_csv('era_count.csv', index=False)
print("\nFile is Saved: era_count.csv") 
