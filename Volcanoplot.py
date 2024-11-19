import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

# 数据读取
result =pd.read_csv("./result.csv",index_col=0)
result 
# result.columns
# result.index
result = result.loc[:, result.columns != "change"]

# 数据整理
result.sort_values(by='log2FoldChange', ascending=False, inplace=True)
result


result['change'] = 'State'
result.loc[(result['log2FoldChange'] > 1.5) & (result['padj'] < 0.05), 'change'] = 'Up'
result.loc[(result['log2FoldChange'] < -1.5) & (result['padj'] < 0.05), 'change'] = 'Down'

result

## 可视化
# 计算 -log10(padj)
result['-log10(padj)'] = -np.log10(result['padj'])

result['-log10(padj)'].describe()
result['log2FoldChange'].describe()

# 设置绘图风格
sns.set(style="whitegrid")
# 创建火山图
plt.figure(figsize=(9, 9))
# 用不同颜色标记 Up, Down 和 State 基因
sns.scatterplot(data=result, x='log2FoldChange', y='-log10(padj)', hue='change', 
                palette={'Up': '#8d2f25', 'Down': '#3e608d', 'State': 'gray'}, 
                s=5, edgecolor=None)
# 设置图的标题和轴标签
plt.title('Volcano Plot', fontsize=16)
plt.xlabel('Log2 Fold Change', fontsize=14)
plt.ylabel('-Log10(padj)', fontsize=14)
plt.xlim(-8,8)
plt.ylim(0,40)
# 添加阈值线（可选）
plt.axhline(y=-np.log10(0.05), color='black', linestyle='--')
plt.axvline(x=1.5, color='#8d2f25', linestyle='--')
plt.axvline(x=-1.5, color='#3e608d', linestyle='--')
# 显示图例
plt.legend()
# plt.tight_layout()
# 保存文件
plt.savefig("volcano_plot.tiff", format="tiff", dpi=300)

