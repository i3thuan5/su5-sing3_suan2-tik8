from unittest.case import TestCase
from unittest.mock import patch

from sit.tsunpi import 準備語料


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 斷詞試驗(TestCase):
    @patch('臺灣言語工具.斷詞.國教院斷詞用戶端.國教院斷詞用戶端.語句斷詞做陣列')
    def test_有moses資料(self, 斷詞mock):
        斷詞mock.return_value = [['我', 'N'], ['愛', 'V'], ['小豬', 'N']]
        語料 = 準備語料().斷詞(
            拆文分析器.建立句物件('我 愛 小豬',)
        )
        self.assertEqual(語料['國教院斷詞'], [['我', 'N'], ['愛', 'V'], ['小豬', 'N']])

    @patch('臺灣言語工具.斷詞.國教院斷詞用戶端.國教院斷詞用戶端.語句斷詞做陣列')
    def test_斷有仝(self, 斷詞mock):
        斷詞mock.return_value = [['我', 'N'], ['愛', 'V'], ['小豬', 'N']]
        語料 = 準備語料().斷詞(
            拆文分析器.建立句物件('我 愛 小豬',)
        )
        self.assertTrue(語料['國教院斷詞kah翻譯有仝無'])

    @patch('臺灣言語工具.斷詞.國教院斷詞用戶端.國教院斷詞用戶端.語句斷詞做陣列')
    def test_斷無仝(self, 斷詞mock):
        斷詞mock.return_value = [['我', 'N'], ['愛', 'V'], ['小豬', 'N']]
        語料 = 準備語料().斷詞(
            拆文分析器.建立句物件('我 愛 小 豬',)
        )
        self.assertFalse(語料['國教院斷詞kah翻譯有仝無'])
