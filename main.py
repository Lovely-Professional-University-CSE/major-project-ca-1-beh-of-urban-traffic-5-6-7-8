#importing library

import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# adding antecedent function
Physics = ctrl.Antecedent(np.arange(0,101,1),'Physics')
Maths = ctrl.Antecedent(np.arange(0,101,1),'Maths')
Chemistry = ctrl.Antecedent(np.arange(0,101,1),'Chemistry')
Biology = ctrl.Antecedent(np.arange(0,101,1),'Biology')





# Adding profession

Engineering = ctrl.Consequent(np.arange(0,1.1,0.1),'Engineering')
Medicine = ctrl.Consequent(np.arange(0,1.1,0.1),'Medicine')
Management = ctrl.Consequent(np.arange(0,1.1,0.1),'Management')
Hospitality = ctrl.Consequent(np.arange(0,1.1,0.1),'Hospitality')
Chief = ctrl.Consequent(np.arange(0,1.1,0.1),'Chief')
Teacher = ctrl.Consequent(np.arange(0,1.1,0.1),'Teacher')
Researcher = ctrl.Consequent(np.arange(0,1.1,0.1),'Researcher')
Architect = ctrl.Consequent(np.arange(0,1.1,0.1),'Architect')
