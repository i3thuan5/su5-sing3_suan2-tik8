from unittest.case import TestCase
from unittest.mock import patch

from sit.tsunpi import 準備語料


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.翻譯.摩西工具.無編碼器 import 無編碼器


@patch('xmlrpc.client.ServerProxy')
class moses試驗(TestCase):
    def setUp(self):
        self.moses_value = {'nbest': [{
            'align': [
                {'src-end': 0, 'src-start': 0, 'tgt-start': 0},
                {'src-end': 1, 'src-start': 1, 'tgt-start': 1},
                {'src-end': 2, 'src-start': 2, 'tgt-start': 2},
                {'src-end': 3, 'src-start': 3, 'tgt-start': 3},
            ],
            'hyp': ' 我  喜歡  小豬  。  ',
            'totalScore': -458.9802856445312,
            'word-align': [
                {'source-word': 0, 'target-word': 0},
                {'source-word': 1, 'target-word': 1},
                {'source-word': 2, 'target-word': 2},
                {'source-word': 3, 'target-word': 3},
            ]
        }]}

    def test_有moses資料(self, xmlrpcMock):
        xmlrpcMock.return_value.translate.return_value = self.moses_value
        語料 = 準備語料(編碼器=無編碼器).台華翻譯(
            拆文分析器.建立句物件('我愛豬仔。', 'gua2 ai3 ti1-a2.'),
        )
        self.assertEqual(語料['moses對應華語陣列'], [[0], [1], [2], [3]])
        self.assertEqual(語料['moses對應台語陣列'], [[0], [1], [2], [3]])

    def test_有moses資料換位(self, xmlrpcMock):
        self.moses_value['nbest'][0]['word-align'] = [
            {'source-word': 0, 'target-word': 0},
            {'source-word': 1, 'target-word': 2},
            {'source-word': 2, 'target-word': 3},
            {'source-word': 3, 'target-word': 1},
        ]
        xmlrpcMock.return_value.translate.return_value = self.moses_value
        語料 = 準備語料(編碼器=無編碼器).台華翻譯(
            拆文分析器.建立句物件('我愛豬仔。', 'gua2 ai3 ti1-a2.'),
        )
        self.assertEqual(語料['moses對應華語陣列'], [[0], [2], [3], [1]])
        self.assertEqual(語料['moses對應台語陣列'], [[0], [3], [1], [2]])

    def test_翻譯結果(self, xmlrpcMock):
        xmlrpcMock.return_value.translate.return_value = self.moses_value
        語料 = 準備語料(編碼器=無編碼器).台華翻譯(
            拆文分析器.建立句物件('我愛豬仔。', 'gua2 ai3 ti1-a2.'),
        )
        self.assertEqual(語料['moses翻譯結果'], '我 喜-歡 小-豬 。')

    def test_無換位(self, xmlrpcMock):
        xmlrpcMock.return_value.translate.return_value = self.moses_value
        語料 = 準備語料(編碼器=無編碼器).台華翻譯(
            拆文分析器.建立句物件('我愛豬仔。', 'gua2 ai3 ti1-a2.'),
        )
        self.assertFalse(語料['moses有換位無'])

    def test_有換位(self, xmlrpcMock):
        self.moses_value['nbest'][0]['word-align'] = [
            {'source-word': 0, 'target-word': 0},
            {'source-word': 1, 'target-word': 2},
            {'source-word': 2, 'target-word': 1},
            {'source-word': 3, 'target-word': 3},
        ]
        xmlrpcMock.return_value.translate.return_value = self.moses_value
        語料 = 準備語料(編碼器=無編碼器).台華翻譯(
            拆文分析器.建立句物件('我愛豬仔。', 'gua2 ai3 ti1-a2.'),
        )
        self.assertTrue(語料['moses有換位無'])
