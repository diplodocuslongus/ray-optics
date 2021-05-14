# standalone script, based on the imports modules in rayoptics/src/environment.py
# only import what's needed for this test
# Ludo 14052021


## initialization
#import math
#import numpy as np
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from pathlib import Path
#import pandas as pd
#
#
## ray-optics
##import rayoptics
##from rayoptics.gui.appmanager import AppManager, ModelInfo
##from rayoptics.gui.appcmds import create_new_model, open_model
#
## optical model
#from rayoptics.optical.opticalmodel import OpticalModel
#
#import rayoptics.elem.surface as srf
#from rayoptics.seq.gap import Gap
#from rayoptics.elem import elements
#from rayoptics.oprops.thinlens import ThinLens
#from rayoptics.elem.profiles import (Spherical, Conic, EvenPolynomial,
#                                     RadialPolynomial)
#from rayoptics.raytr.opticalspec import (WvlSpec, FieldSpec, Field,
#                                         PupilSpec, FocusRange)
#from rayoptics.optical.model_enums import (DimensionType, DecenterType)
#
## ray-optics first and third order
#import rayoptics.parax.firstorder as fo
#from rayoptics.parax.firstorder import compute_first_order
#import rayoptics.parax.thirdorder as to
#from rayoptics.parax.thirdorder import compute_third_order
#
## ray tracing
#from rayoptics.raytr.trace import (RayPkg, RaySeg, list_ray,
#                                   trace, trace_base, trace_with_opd,
#                                   trace_astigmatism)
#import rayoptics.raytr.raytrace as rt
#from rayoptics.raytr import analyses
#
## paraxial design
#import rayoptics.optical.model_constants as mc
#
#from rayoptics.mpl.interactivediagram import InteractiveDiagram
#
## axis array figures
#from rayoptics.mpl.axisarrayfigure import Fit
#from rayoptics.mpl.axisarrayfigure import RayFanFigure
#from rayoptics.mpl.axisarrayfigure import SpotDiagramFigure
#from rayoptics.mpl.axisarrayfigure import WavefrontFigure
#
#from rayoptics.mpl.analysisfigure import (AnalysisFigure,
#                                          RayFanPlot, RayGeoPSF,
#                                          Wavefront, DiffractionPSF)
#
#from rayoptics.mpl import analysisplots
#
## lens layout
#from rayoptics.mpl.interactivelayout import InteractiveLayout
#
## opticalglass
#from opticalglass.glassfactory import create_glass
#from opticalglass.spectral_lines import get_wavelength

isdark = False

# from rayoptics import *
from rayoptics.environment import *
opm = OpticalModel()
sm  = opm.seq_model
osp = opm.optical_spec
pm = opm.parax_model

osp.pupil = PupilSpec(osp, key=['object', 'pupil'], value=12.5)
osp.field_of_view = FieldSpec(osp, key=['object', 'angle'], flds=[0., 10.0, 14.0])
osp.spectral_region = WvlSpec([(486.10, 1.0), (587.5618, 1.0), (656.30, 1.0)], ref_wl=1)
opm.radius_mode = True
opm.system_spec.dimensions = 'MM'
# sm = sequential model
sm.gaps[0].thi=1e10 # object at infinity

sm.add_surface([56.20238, 8.75, 'N-SSK2', 'Schott'])
sm.add_surface([152.28580, 0.5]) # air after the surface so no glass specification
sm.add_surface([37.68262, 12.5, 'N-SK2','Schott'])
sm.add_surface([0, 3.8, 'F5','Schott']) 
# sm.add_surface([10000000, 3.8, 'F5','Schott']) 
sm.add_surface([24.23130,16.369445]) # air after the surface so no glass specification
sm.add_surface([0, 13.757957]) 
# sm.add_surface([10000000, 13.757957]) 
sm.set_stop() #sets the stop surface to the current surface
sm.add_surface([-28.37731,3.8, 'F5','Schott']) 
# sm.add_surface([10000000, 11,'N-SK16','Schott']) 
sm.add_surface([0, 11,'N-SK16','Schott']) 
sm.add_surface([-37.92546, 0.5])
sm.add_surface([177.41176,7,'N-SK16','Schott']) 
sm.add_surface([-79.41143,61.487536])
# sm.add_surface([10000000, 0])
# sm.add_surface([0, 0])

opm.update_model()

sm.list_model()
#layout_plt = plt.figure(FigureClass=InteractiveLayout, opt_model=opm, is_dark=isdark)
#layout_plt.plot()
#pouet
#layout_plt = plt.figure(FigureClass=InteractiveLayout, opt_model=opm, is_dark=isdark).plot()
#layout_plt.show()
#pouet
#layout_plt = plt.figure(FigureClass=InteractiveLayout, opt_model=opm, is_dark=isdark)
#layout_plt.plot().show()
#pouet
# shows a very small image in the bottom left corner
#layout_plt = plt.figure(FigureClass=InteractiveLayout, opt_model=opm, is_dark=isdark)
#plt.show()
#pouet
# error: 'list' object has no attribute 'show'
#layout_plt = plt.figure(FigureClass=InteractiveLayout, opt_model=opm, is_dark=isdark)
#plt.plot().show()
#pouet
# doesn't show anything
#layout_plt = plt.figure(FigureClass=InteractiveLayout, opt_model=opm, do_draw_rays=True, do_paraxial_layout=False, is_dark=False)
#layout_plt.show()
#pouet
# doesn't show anything
#layout_plt = plt.figure(FigureClass=InteractiveLayout, opt_model=opm, do_draw_rays=True, do_paraxial_layout=False, is_dark=False)
#layout_plt.plot().show()
#pouet
# shows a very small image in the bottom left corner
#layout_plt = plt.figure(FigureClass=InteractiveLayout, opt_model=opm, do_draw_rays=True, do_paraxial_layout=False, is_dark=False)
#plt.show()
#pouet
# OK
layout_plt = plt.figure(FigureClass=InteractiveLayout, opt_model=opm, do_draw_rays=True, do_paraxial_layout=False, is_dark=False).plot()
#plt.show() # without this no plot is shown
pm.first_order_data()
# OK TOO
#layout_plt = plt.figure(FigureClass=InteractiveLayout, opt_model=opm, is_dark=isdark)
#layout_plt.plot()
#plt.show()
#pouet

# opm.optical_spec.parax_data.fod.list_first_order_data()
# pm.fod.efl()
opm.optical_spec.parax_data.fod.efl

abr_plt = plt.figure(FigureClass=RayFanFigure, opt_model=opm, data_type='Ray', scale_type=Fit.All_Same, is_dark=False)
# plt.title('jojo')
abr_plt.plot()
#abr_plt.plot().show()
plt.show()
