from widget import Widget
import unittest
import numpy as np

# python 单元test内容参考
# https://www.cnblogs.com/liyuanhong/articles/5306918.html


# 执行测试的类
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()

    def tearDown(self):
        self.widget = None

    def testSize(self):
        self.assertEqual(self.widget.getSize(), (10, 40))

    def testResize(self):
        self.widget.resize(200, 100)
        self.assertEqual(self.widget.getSize(), (200, 100))

    def testcomparenan(self):
        self.assertEqual('', '')


# 构造测试集
# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(WidgetTestCase("testSize"))
#     # suite.addTest(WidgetTestCase("testResize"))
#     return suite

# 测试
if __name__ == "__main__":
    # 写在main里面后 def suite():就不需要了
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    suite.addTest(WidgetTestCase("testResize"))
    suite.addTest(WidgetTestCase("testcomparenan"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

    # ================================
    # unittest.main(defaultTest='suite')
