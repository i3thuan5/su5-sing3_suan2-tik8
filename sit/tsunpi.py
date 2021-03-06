from 臺灣言語工具.斷詞.國教院斷詞用戶端 import 國教院斷詞用戶端
from 臺灣言語工具.翻譯.摩西工具.語句編碼器 import 語句編碼器
from 臺灣言語工具.翻譯.摩西工具.摩西用戶端 import 摩西用戶端


class 準備語料:
    def __init__(self, 編碼器=語句編碼器):
        self._編碼器 = 編碼器

    def 台華翻譯(self, 句物件):
        華語句物件, 台語新結構句物件, _分數 = (
            摩西用戶端(位址='huanik', 編碼器=self._編碼器).翻譯分析(句物件)
        )
        台語詞陣列 = 台語新結構句物件.網出詞物件()
        華語詞陣列 = 華語句物件.網出詞物件()
        moses翻譯結果 = 華語句物件.看分詞()
        moses對應華語目標陣列 = self._翻譯對應物件轉編號(台語詞陣列, 華語詞陣列, '翻譯目標詞陣列')
        moses對應台語來源陣列 = self._翻譯對應物件轉編號(華語詞陣列, 台語詞陣列, '翻譯來源詞陣列')
        有換位無 = False
        這馬 = -1
        for 陣列 in moses對應華語目標陣列:
            if 陣列[-1] < 這馬:
                有換位無 = True
                break
            這馬 = 陣列[-1]
        return {
            'moses翻譯結果': moses翻譯結果,
            'moses對應台語陣列': moses對應台語來源陣列,
            'moses對應華語陣列': moses對應華語目標陣列,
            'moses有換位無': 有換位無,
        }

    def 斷詞(self, 華語句物件):
        斷詞結果 = 國教院斷詞用戶端.語句斷詞做陣列(華語句物件.看型(' ', ' '))
        相仝 = True
        for guan, tng in zip(華語句物件.網出詞物件(), 斷詞結果):
            if guan.看型() != tng[0]:
                相仝 = False
        return {
            '國教院斷詞': 斷詞結果,
            '國教院斷詞kah翻譯有仝無': 相仝,
        }

    def _翻譯對應物件轉編號(self, 台語詞陣列, 華語詞陣列, 翻譯欄位):
        moses對應華語目標陣列 = []
        for 詞物件 in 台語詞陣列:
            對應編號 = []
            所在 = 0
            for 華語詞物件 in getattr(詞物件, 翻譯欄位):
                while 華語詞陣列[所在] is not 華語詞物件:
                    所在 += 1
                對應編號.append(所在)
                所在 += 1
            moses對應華語目標陣列.append(對應編號)
        return moses對應華語目標陣列
