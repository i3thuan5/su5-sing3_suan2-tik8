from unittest.case import TestCase, skip


@skip('先規劃，上尾來檢查')
class 欄位試驗(TestCase):
    @classmethod
    def setUpClass(cls):
        self.語料 = 準備語料().詞性句法('我愛豬仔。', 'gua2 ai3 ti1-a2')

    def test_有原本資料(self):
        self.assertIn('漢字', self.語料)
        self.assertIn('羅馬字', self.語料)

    def test_有moses資料(self):
        self.assertIn('moses詞對應陣列', self.語料)
        self.assertIn('moses翻譯結果', self.語料)
        self.assertIn('moses有換位無', self.語料)

    def test_有斷詞資料(self):
        self.assertIn('國教院斷詞', self.語料)
        self.assertIn('國教院斷詞kah翻譯有仝無', self.語料)

    def test_有句法資料(self):
        self.assertIn('Stanford句法', self.語料)

    def test_有整合資料(self):
        self.assertIn('Stanford對應有合法無', self.語料)
        self.assertIn('台語句法', self.語料)
