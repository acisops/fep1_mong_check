from ..fep1_mong_check import validation_limits, \
    hist_limit, calc_model, model_path
from acis_thermal_check.regression_testing import \
    RegressionTester, all_loads
import pytest

f1m_rt = RegressionTester("tmp_fep1_mong", "fep1_mong", model_path,
                          validation_limits, hist_limit, calc_model)

# ACIS state builder tests

f1m_rt.run_models(state_builder='acis')

# Prediction tests

@pytest.mark.parametrize('load', all_loads)
def test_prediction_acis(answer_store, load):
    f1m_rt.run_test("prediction", answer_store, load)

# Validation tests

@pytest.mark.parametrize('load', all_loads)
def test_validation_acis(answer_store, load):
    f1m_rt.run_test("validation", answer_store, load)

