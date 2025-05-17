import pandas as pd
df = pd.read_excel(r"C:\Users\SOURANIL\OneDrive\Desktop\data analytics\Churn Analysis\cleaned_churn.xlsx")

print("\nChurn count:\n", df['Churn'].value_counts())
print("\nChurn percentage:\n", df['Churn'].value_counts(normalize=True) * 100)

print("\nChurn by Gender:\n", pd.crosstab(df['Gender'], df['Churn'], normalize='index') * 100)

print("\nAge Summary:\n", df['Age'].describe())
print("\nAverage Age by Churn:\n", df.groupby('Churn')['Age'].mean())

print("\nTenure Summary:\n", df['Tenure'].describe())
print("\nAverage Tenure by Churn:\n", df.groupby('Churn')['Tenure'].mean())

print("\nChurn by Usage Frequency:\n", pd.crosstab(df['Usage Frequency'], df['Churn'], normalize='index') * 100)

print("\nSupport Calls Summary:\n", df['Support Calls'].describe())
print("\nAverage Support Calls by Churn:\n", df.groupby('Churn')['Support Calls'].mean())

print("\nPayment Delay Summary:\n", df['Payment Delay'].describe())
print("\nAverage Payment Delay by Churn:\n", df.groupby('Churn')['Payment Delay'].mean())

print("\nChurn by Subscription Type:\n", pd.crosstab(df['Subscription Type'], df['Churn'], normalize='index') * 100)

print("\nContract Length Summary:\n", df['Contract Length'].describe())
print("\nChurn by Contract Length:\n", pd.crosstab(df['Contract Length'], df['Churn'], normalize='index') * 100)


print("\nTotal Spend Summary:\n", df['Total Spend'].describe())
print("\nAverage Total Spend by Churn:\n", df.groupby('Churn')['Total Spend'].mean())


