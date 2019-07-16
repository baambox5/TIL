### pprint

```python
from pprint import pprint

pprint(data)

# 결과(아래와 같이 정렬해준다.)
{'24H_fluctate': '943000',
 '24H_fluctate_rate': '7.65',
 'average_price': '12512589.9129',
 'buy_price': '13264000',
 'closing_price': '13269000',
 'date': '1563235506766',
 'max_price': '13451000',
 'min_price': '11879000',
 'opening_price': '12326000',
 'sell_price': '13269000',
 'units_traded': '14704.91767059',
 'volume_1day': '14704.91767059',
 'volume_7day': '90812.44165705'}
```

-----

### get(key[, default])

   - key가 딕셔너리에 있는 경우 key에 대응하는 value를 돌려주고, 그렇지 않으면 default를 돌려줍니다.
   - default를 따로 작성하지 않으면 기본값 `None`이 사용됩니다. 그래서 이 메서드는 절대로 keyerror를 일으키지 않습니다.
   - 결국 key가 없을 때, None이 아닌 다른 값을 받길 원한다면 `/get(key, 3)` 처럼 사용할 수 있다.



------

### break, continue, else

- 에러 처리에 사용할 예정