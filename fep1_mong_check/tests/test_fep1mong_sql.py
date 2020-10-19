from ..fep1_mong_check import model_path, FEP1MongCheck
from acis_thermal_check.regression_testing import \
    RegressionTester, all_loads
import pytest


@pytest.fixture(autouse=True, scope='module')
def fm_rt(test_root):
    # SQL state builder tests
    rt = RegressionTester(FEP1MongCheck, model_path, 
                          "fep1_mong_test_spec.json",
                          test_root=test_root, sub_dir='sql')
    rt.run_models(state_builder='sql')
    return rt

# Prediction tests

@pytest.mark.parametrize('load', all_loads)
def test_prediction(fm_rt, answer_store, load):
    if not answer_store:
        fm_rt.run_test("prediction", load)
    else:
        pass

# Validation tests

@pytest.mark.parametrize('load', all_loads)
def test_validation(fm_rt, answer_store, load):
    if not answer_store:
        fm_rt.run_test("validation", load)
    else:
        pass
