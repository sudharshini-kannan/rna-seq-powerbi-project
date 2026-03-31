import pandas as pd

# Load data
df = pd.read_csv('data/gene_expression.csv')
# Add significance column
df['significant'] = df['pvalue'] < 0.05

# Sort by fold change
df = df.sort_values(by='log2FoldChange', ascending=False)

# Save cleaned file
df.to_csv('output/cleaned_gene_expression.csv', index=False)

print("Data processed successfully!")