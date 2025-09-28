"""
请求地址：
    https://fanyi.baidu.com/mtpe-individual/transText?query=python5&lang=en2zh
请求：
    post

{isAi: false, sseStartTime: 1756021801520, query: "python5", from: "en", to: "zh", reference: "",…}
corpusIds: []
detectLang: ""
domain: "common"
from: "en"
isAi: false
milliTimestamp: 1756021801608
needPhonetic: true
query: "python5"
reference: ""
sseStartTime: 1756021801520
to: "zh"
"""
from wsgiref import headers

import requests
import time

url = "https://fanyi.baidu.com/mtpe-individual/transText?query=python5&lang=en2zh"

headers = {
    "referer" :"https://fanyi.baidu.com/mtpe-individual/transText?query=python5&lang=en2zh",
    "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "cookie" : """BAIDUID_BFESS=AD46BAA0B2D4CB49608A4675E4082D38:FG=2025-8-30; ZFY=7dV18I1006QQqXv65NaaCIlqBIxAw5EVU1BwUNo7vrs:C; BIDUPSID=AD46BAA0B2D4CB49608A4675E4082D38; PSTM=1755603574; H_PS_PSSID=60272_62325_63148_63324_63947_64174_64365_64361_64364_64418_64437_64442_64450_64457_64481_64515_64086_64554_64590_64593_64597_64604; AIT_PERSONAL_VERSION=2025-8-30; AIT_ENTERPRISE_VERSION=2025-8-30; ab_sr=2025-8-30.0.1_NTZiYTA0ZTc0OTkxMGFmNWVmZWU1YmZmYjEwN2MxNDRjNWI0Y2U0ODk1Mzg3NTg1MWI3Y2Q0MmM0NmE1NjY5OTZjM2M4OWIzNmZhMjA3ZDYyMWM2ODc3NWMxNTIzYmI2ZTM0YTFhOTdmNGYwMTA1MjU1MzZhY2FlYjljY2NlNzE1NGI0MmQ3YTQ4OTRjZmFlZTYxN2M2N2Y0YWQ3NzY3NA==; ppfuid=FOCoIC3q5fKa8fgJnwzbE+YhNskVRU4HW930FeLFkOByMFn76lfGbpe1mvnbXASpprBSgAj8TeGH+O6o2VUDCfLdJ4BbXu0qA2r9fH5GA51vxNYIV7rYxWsNNjqUx/Yat+ovxzzsosXaoURHehskaVP+zepC4iWbDR2Yi+bbZlMYSKaPLcytcSlK4i2cjgoPl4cO6HjU76ZfRtkePN9nsosw2v2hEzUqslgg++Rnea5V3RYuoLikUtLUQT7BGPeQEmxXBeQZ0XbgCwRDcrlcFuH0QcBYM6DZPV6OmrSzZ4XL1qv+PnrpepYOhsag01+Z+loSFmmhv2V7ZvlAgR2JB7PQT1JWd15eR30RqakbQ9xeEtnXboI8UIgS6P+dZr5E/OD8JBX63f3pFxD5AHkHpNqyaA6snjSfrc6wpI6mhIumSUS1Mp/HmEdz2Pie6tGtPGsL6qYLHxcbOK07dryIA5VdVIYaeRQHuoDSSFKbaexDAGl2CptdRviVT7M0BXafQCS3JuGErGFF5GjyNk5euiduOnJo1kA02oQDiDUea10ea/+1VSNUTGfIG+NKu2s+7wiuely6KCk+Wvq7Ba3+WbtMsgoomoBJYa0xDrTXQSSavHh8BB7hQZ4vWoUsKQu5WypFMGih+vbX9AxVe4SUToixE0hZaCFZB3ct/iNiVK9GruSC60eiNRQEQ/ZSIdkqbKZYS8G+xdJdICS4FUVSdr0DmY2bfhk+6hFX7NjcWSHiO+V9CiVUNI5+8sTo0reDp+dJbyJ2fgXzV64OdwPB9O3Wqyafho53te3dbwaX51R1EZKW6ozgW4CAcK92ep8aedt7e+wercu4XumiZtPrlzSEkAqHpUSNAXSAARmPxkG/FHxo/g5cp6BkJsY8GIlZdPxdhLrn4nsOcYI4IJYcWj6sbLOnsdAsXwHWX01hPhUaSOgNH5tdxRuHdZQYpSialqSOUBaDX3vPxbS+3byEI0rDszStD9ydVVIpfdpD+csOZsGd4VDUV9m0ys7/q7aV2rtoc3z07Ju637GxzfwnojhZ3atWLnGsfyEaq93vs4m7Mfxf61vQ9X5ee7c0vV+aosiH5dwXp+fI8U9TG15C1u0vKL6CrnOjCDWgWPw78v2hWygrbZr2pSYz8eskxGwuLX4n1pJ3jb5fvx8MhmCQ+Hd6nMsu/BGacBuznP9X6OXc/eBWeXCb1t/CFoW2eEU3Z0dgDDuLhCGtd3NzvuKxeKX3Yc/LoBngyI5JW/R0UWAIBF37aBhyiPWPAOeYXBqA; RT="z=2025-8-30&dm=baidu.com&si=419f512d-e8a8-4085-9096-de783bda9d51&ss=mepds0oc&sl=a&tt=vg2&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=8k49&nu=9y8m6cy&cl=2f3x""",
}

params = {
"corpusIds": [],
"detectLang": "",
"domain": "common",
"from": "en",
"isAi": "false",
"milliTimestamp": 1756021801608,
"needPhonetic": "true",
"query": "python5",
"reference": "",
"sseStartTime": 1756021801520,
"to": "zh",
}

response = requests.post(url=url, data=params, headers=headers)
print(response.text)


