import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('output/cleaned_gene_expression.csv')

# Barplot
sns.barplot(x='Gene', y='log2FoldChange', data=df)
plt.xticks(rotation=45)
plt.title("Gene Expression")
plt.tight_layout()
plt.savefig('output/gene_expression.png')