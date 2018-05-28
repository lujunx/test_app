import pytest


@pytest.fixture(params=[2,1,3])
def fix_data(request):
    return request.param


class Test_001:

    # def test_0011(self, fix_data):
    #     # fixture传参
    #     assert fix_data != 2
    # @pytest.mark.parametrize("test_data",[4,5,6])
    # def test_0022(self, test_data):
    #     # parametrize 单个参数
    #     assert  test_data == 5

    @pytest.mark.parametrize("a,b,c",[(1,2,3),(4,5,6)])
    def test_0033(self,b,a,c):
        # parametrize 单个参数
        assert a+b == c

if __name__ == '__main__':
    pytest.main("-s test_001.py")