#!/usr/bin/env python

scoreInfo=[
{'name':'Lucy','en_score': 89.6,'math_scroe':94.1},
{'name':'Bob','en_score': 72.4,'math_scroe':84.2},
{'name':'LiLei','en_score': 82.6,'math_scroe':74.1},
{'name':'HanMeimei','en_score': 65.6,'math_scroe':86.9},
{'name':'Lily','en_score': 78.1,'math_scroe':65.8},
{'name':'Tracy','en_score': 72.6,'math_scroe':65.4}
]

t_scoreInfo = sorted([item for item in scoreInfo], key=lambda x: x['en_score'], reverse=True)
print t_scoreInfo
