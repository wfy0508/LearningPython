import pandas as pd
import json
import seaborn as sns

data = []
with open('./examples/example.txt') as f:
    for line in f:
        data.append(line)

records = [json.loads(data[i]) for i in range(0, len(data))]

records_df = pd.DataFrame(records)
clean_tz = records_df.tz.fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
subset = clean_tz.value_counts()
sns.barplot(y=subset.index, x=subset.values)
