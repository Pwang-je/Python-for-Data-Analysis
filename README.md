```python
import pandas as pd
user_names = ['user_id', 'gender', 'title']
users = pd.read_csv(파일경로, sep='', header=None, names=user_names, encoding='utf-8')
```
컬럼의 이름을 넣어줄 때, names 부분에다가 넣으면 되는데 그렇게 하지 않고도 네임변수를 만든 후 그걸 넣어줘도 된다.


```md
%s	문자열 (파이썬 객체를 str()을 사용하여 변환)
%r	문자열 (파이썬 객체를 repr()을 사용하여 변환)
%c	문자(char)
%d 또는 %i	정수 (int)
%f 또는 %F	부동소수 (float) (%f 소문자 / %F 대문자)
%e 또는 %E	지수형 부동소수 (소문자 / 대문자)
%g 또는 %G	일반형: 값에 따라 %e 혹은 %f 사용 (소문자 / 대문자)
%o 또는 %O	8진수 (소문자 / 대문자)
%x 또는 %X	16진수 (소문자 / 대문자)
%%	% 퍼센트 리터럴
```


