```python
import pandas as pd
user_names = ['user_id', 'gender', 'title']
users = pd.read_csv(파일경로, sep='', header=None, names=user_names, encoding='utf-8')
```
컬럼의 이름을 넣어줄 때, names 부분에다가 넣으면 되는데 그렇게 하지 않고도 네임변수를 만든 후 그걸 넣어줘도 된다.





