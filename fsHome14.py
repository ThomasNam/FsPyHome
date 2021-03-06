from pandas import DataFrame

source_data = {
    'name': ['수도권', '경기', '서울', '부산', '경남', '인천', '경북', '대구', '충남', '전북', '전남', '충북', '대전', '강원', '광주', '울산', '제주', '세종'],
    '2013': [24946, 12126, 9990, 3456, 3278, 2830, 2661, 2476, 2062, 1821, 1784, 1565, 1545, 1506, 1504, 1137, 570, 118],
    '2014': [25119, 12282, 9975, 3452, 3307, 2862, 2671, 2475, 2088, 1829, 1792, 1578, 1553, 1510, 1606, 1151, 583, 132],
    '2015': [25247, 12423, 9941, 3452, 3330, 2883, 2678, 2469, 2103, 1835, 1797, 1589, 1542, 1517, 1506, 1164, 599, 187],
    '2016': [25371, 12612, 9852, 3447, 3346, 2907, 2686, 2465, 2123, 1833, 1800, 1596, 1535, 1520, 1504, 1169, 619, 233],
    '2017': [25509, 12809, 9776, 3429, 3355, 2923, 2681, 2465, 2148, 1830, 1796, 1605, 1531, 1521, 1501, 1166, 634, 276],
}

df = DataFrame(source_data)
df.index.name = "통계표명"
print(df)

# 인구수가 2017년기준 3000(천명)이하인 지역을 출력하세요.
p3000underDf = df[df['2017'] < 3000][['name', '2017']]
p3000underDf.index.name = "인구수가 2017년기준 3000(천명)이하인 지역을 출력하세요."

print(p3000underDf)


def value_to_dangerstr(val):
    if val <= 1000:
        return "위험"
    elif val <= 5000:
        return "주위"
    else:
        return "안정"


# 각 년도별로 인구수가 1000(천명)이하는 ‘위험’, 5000(천명)이하 ‘주의’ 그 이상은 ‘안정’ 이라는 데이터를 가지도록 조작하세요
for year in range(2013, 2017+1):
    data = df[str(year)]
    idx = 0
    for v in data:
        df.loc[idx, str(year)] = value_to_dangerstr(v)
        idx += 1

print(df)

