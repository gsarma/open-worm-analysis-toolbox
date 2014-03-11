# -*- coding: utf-8 -*-
"""
  config.py:
    wormpy module configuration settings
  
  @authors: @JimHokanson, @MichaelCurrie
  
  The original Schafer Lab code contained many hardcoded values.  These are
  tracked in a central location here.
  Some hardcoded values were not implemented in this open-source translation.
  these are shown here as being commented out.
  
  Best practice is to use this via "from wormpy import config", and then 
  reference the configuration settings like this: e.g. "config.FPS" rather
  than doing "from wormpy.config import *" and referencing "FPS"
  since the latter approach pollutes the global namespace.
  
"""

#__ALL__ = ['FPS', 'N_ECCENTRICITY']

""" DEBUG MODE TO RESTORE OLD SCHAFER LAB ERRORS """

MIMIC_OLD_BEHAVIOUR = False

""" FEATURE CONFIGURATION SETTINGS """

# Frames Per Second
# (must be a multiple of both 1/TIP_DIFF and 1/BODY_DIFF)
FPS = 20                 
VENTRAL_MODE = 0   # DEBUG: might not need to be here but used in Path code
    
# Grid size for estimating eccentricity, this is the
# max # of points that will fill the wide dimension.
# (scalar) The # of points to place in the long dimension. More points
# gives a more accurate estimate of the ellipse but increases
# the calculation time.
N_ECCENTRICITY = 50     

POSTURE_AMPLITURE_AND_WAVELENGTH = { \
  'N_POINTS_FFT': 512, 
  # NOTE: Unfortunately the distance is in normalized
  # frequency units (indices really), not in real frequency units
  'MIN_DIST_PEAKS': 5, 
  'WAVELENGTH_PCT_MAX_CUTOFF': 0.5,  # TODO: describe
  'WAVELENGTH_PCT_CUTOFF': 2}        # TODO: describe
  
POSTURE_AMPLITURE_AND_WAVELENGTH['HALF_N_FFT'] = \
  POSTURE_AMPLITURE_AND_WAVELENGTH['N_POINTS_FFT']/2

# used in get_velocity:
TIP_DIFF  = 0.25
BODY_DIFF = 0.5


# Used in get_motion_codes:

#   These are a percentage of the length ...
SPEED_THRESHOLD_PCT   = 0.05
DISTANCE_THRSHOLD_PCT = 0.05
PAUSE_THRESHOLD_PCT   = 0.025

#   These are times (s)
EVENT_FRAMES_THRESHOLD = 0.5    # Half a second
EVENT_MIN_INTER_FRAMES_THRESHOLD = 0.25

DATA_SUM_NAME       = 'distance'
INTER_DATA_SUM_NAME = 'interDistance'



