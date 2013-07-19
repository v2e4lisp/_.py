import unittest
import sys
from test_list import TestUnderscoreList as t_list
from test_dict import TestUnderscoreDict as t_dict
from test_number import TestUnderscoreNumber as t_num
from test_function import TestUnderscoreFunction as t_func
from test_set import TestUnderscoreSet as t_set

if __name__ == '__main__':
    v = sys.version_info
    version = str(v.major) + '.' + str(v.minor) + '.' + str(v.micro)
    print('*' * 80)
    print('* Tested by python-' + version)
    print('*' * 80)
    print('')

    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(t_list))
    suite.addTests(unittest.makeSuite(t_dict))
    suite.addTests(unittest.makeSuite(t_num))
    suite.addTests(unittest.makeSuite(t_func))
    suite.addTests(unittest.makeSuite(t_set))
    # suite = unittest.TestLoader().loadTestsFromTestCase(t_list, t_dict, t_num, t_func)
    unittest.TextTestRunner(verbosity=2).run(suite)

