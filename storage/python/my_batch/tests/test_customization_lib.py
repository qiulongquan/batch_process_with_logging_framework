from lib.customization_lib import MyLib
import sys
import os
import unittest

# 已经通过 import MyLib导入了 MyLib包，不需要下面的sys.path添加路径了
# ../libをロードパスに入れる
# app_home = os.path.abspath(os.path.join(
#     os.path.dirname(os.path.abspath(__file__)), ".."))
# sys.path.append(os.path.join(app_home, "lib"))

# ../テスト対象のライブラリのロード


class TestMyLib(unittest.TestCase):

    def test_get_name(self):
        ml = MyLib()
        self.assertEqual("my_lib", ml.get_name())


if __name__ == '__main__':
    unittest.main()
