#插件学习  失败重跑
#命令:pytest test_rerun.py --reruns 5 -vs  当前文件失败重跑5次
#pytest test_rerun.py --reruns 5 --rerun-dalay 1 -vs   失败等待1秒继续重跑
import pytest


#@pytest.mark.flaky(reruns = 5 ,reruns_delay=1)
def test_re():
    pytest.assume(1==1)
    pytest.assume(1 == 2)
    pytest.assume(1 == 3)