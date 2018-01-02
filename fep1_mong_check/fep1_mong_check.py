#!/usr/bin/env python

"""
========================
fep1_mong_check
========================

This code generates backstop load review outputs for checking the ACIS
FEP1 Mongoose temperature. It also generates FEP1 Mongoose model validation
plots comparing predicted values to telemetry for the previous three
weeks.
"""
from __future__ import print_function

# Matplotlib setup                                                                                                                                              
# Use Agg backend for command-line (non-interactive) operation                                                                                                   
import matplotlib
matplotlib.use('Agg')

import numpy as np
import xija
import sys
from acis_thermal_check import \
    ACISThermalCheck, \
    calc_off_nom_rolls, \
    get_options, \
    make_state_builder, \
    get_acis_limits
import os

model_path = os.path.abspath(os.path.dirname(__file__))

yellow_hi, red_hi = get_acis_limits("tmp_fep1_mong")

MSID = {"fep1_mong":'TMP_FEP1_MONG'}
YELLOW = {"fep1_mong": yellow_hi}
MARGIN = {"fep1_mong": 2.0}
VALIDATION_LIMITS = {'TMP_FEP1_MONG': [(1, 2.0), (50, 1.0), (99, 2.0)],
                     'PITCH': [(1, 3.0), (99, 3.0)],
                     'TSCPOS': [(1, 2.5), (99, 2.5)]
                     }
HIST_LIMIT = [20.]

def calc_model(model_spec, states, start, stop, T_fep=None, T_fep_times=None):
    model = xija.ThermalModel('fep1_mong', start=start, stop=stop,
                              model_spec=model_spec)
    times = np.array([states['tstart'], states['tstop']])
    model.comp['sim_z'].set_data(states['simpos'], times)
    model.comp['eclipse'].set_data(False)
    model.comp['tmp_fep1_mong'].set_data(T_fep, T_fep_times)
    model.comp['roll'].set_data(calc_off_nom_rolls(states), times)
    for name in ('ccd_count', 'fep_count', 'vid_board', 'clocking', 'pitch'):
        model.comp[name].set_data(states[name], times)

    model.make()
    model.calc()
    return model

def main():
    args = get_options("fep1_mong", model_path)
    state_builder = make_state_builder(args.state_builder, args)
    fep1_mong_check = ACISThermalCheck("tmp_fep1_mong", "fep1_mong", MSID,
                                       YELLOW, MARGIN, VALIDATION_LIMITS,
                                       HIST_LIMIT, calc_model)
    try:
        fep1_mong_check.driver(args, state_builder)
    except Exception as msg:
        if args.traceback:
            raise
        else:
            print("ERROR:", msg)
            sys.exit(1)

if __name__ == '__main__':
    main()
