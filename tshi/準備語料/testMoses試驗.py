from unittest.case import TestCase, skip

from sit.tsunpi import 準備語料


from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


@skip('較等--咧來做')
class moses試驗(TestCase):

    def test_有moses資料(self):
        self.語料 = 準備語料().台華翻譯(
            拆文分析器.建立句物件('我愛豬仔。', 'gua2 ai3 ti1-a2.')
        )
        self.assertIn('moses詞對應陣列', self.語料)
        self.assertIn('moses翻譯結果', self.語料)
        self.assertIn('moses有換位無', self.語料)
