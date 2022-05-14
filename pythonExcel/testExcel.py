from pathlib import Path

import pandas as pd
import xlrd

# 获取当前文件目录
this_dir = Path(__file__).resolve().parent
# 获取数据目录
data_dir = this_dir / "data/sales_data"

parts = []
for path in data_dir.rglob("*.xls*"):
    parts.append(pd.read_excel(path, index_col="transaction_id"))
# 将列表中的DataFrame连接起来
df = pd.concat(parts)
# 透视汇总数据
pivot = pd.pivot_table(df,
                       values="amount",
                       index="transaction_date",
                       columns="store",
                       aggfunc=sum)
# 采样汇总到月
summary = pivot.resample('M').sum()
summary.index.name = 'Month'
summary.to_excel(data_dir / "sales_summary.xlsx")
