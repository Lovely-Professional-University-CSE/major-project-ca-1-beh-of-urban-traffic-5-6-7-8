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


#using trapmf(Trapizoidal membership Function)
Physics['Excellent'] = fuzzy.trapmf(Physics.universe,[70,85,100,100])
Physics['Good'] = fuzzy.trapmf(Physics.universe,[55,70,75,75])
Physics['Average'] = fuzzy.trapmf(Physics.universe,[38,55,60,60])
Physics['Poor'] = fuzzy.trapmf(Physics.universe,[25,30,40,40])
Physics['Very_Poor'] = fuzzy.trapmf(Physics.universe,[0,15,25,25])

Maths['Excellent'] = fuzzy.trapmf(Maths.universe,[70,85,100,100])
Maths['Good'] = fuzzy.trapmf(Maths.universe,[55,70,75,75])
Maths['Average'] = fuzzy.trapmf(Maths.universe,[38,55,60,60])
Maths['Poor'] = fuzzy.trapmf(Maths.universe,[25,30,40,40])
Maths['Very_Poor'] = fuzzy.trapmf(Maths.universe,[0,15,25,25])

Chemistry['Excellent'] = fuzzy.trapmf(Chemistry.universe,[70,85,100,100])
Chemistry['Good'] = fuzzy.trapmf(Chemistry.universe,[55,70,75,75])
Chemistry['Average'] = fuzzy.trapmf(Chemistry.universe,[38,55,60,60])
Chemistry['Poor'] = fuzzy.trapmf(Chemistry.universe,[25,30,40,40])
Chemistry['Very_Poor'] = fuzzy.trapmf(Chemistry.universe,[0,15,25,25])

Biology['Excellent'] = fuzzy.trapmf(Biology.universe,[70,85,100,100])
Biology['Good'] = fuzzy.trapmf(Biology.universe,[55,70,75,75])
Biology['Average'] = fuzzy.trapmf(Biology.universe,[38,55,60,60])
Biology['Poor'] = fuzzy.trapmf(Biology.universe,[25,30,40,40])
Biology['Very_Poor'] = fuzzy.trapmf(Biology.universe,[0,15,25,25])


#Adding Profession and their consequrnt function
Engineering = ctrl.Consequent(np.arange(0,1.1,0.1),'Engineering')
Medicine = ctrl.Consequent(np.arange(0,1.1,0.1),'Medicine')
Management = ctrl.Consequent(np.arange(0,1.1,0.1),'Management')
Hospitality = ctrl.Consequent(np.arange(0,1.1,0.1),'Hospitality')
Chief = ctrl.Consequent(np.arange(0,1.1,0.1),'Chief')
Teacher = ctrl.Consequent(np.arange(0,1.1,0.1),'Teacher')
Researcher = ctrl.Consequent(np.arange(0,1.1,0.1),'Researcher')
Architect = ctrl.Consequent(np.arange(0,1.1,0.1),'Architect')
Artist = ctrl.Consequent(np.arange(0,1.1,0.1),'Artist')
Athlete = ctrl.Consequent(np.arange(0,1.1,0.1),'Athlete')
Fitness_trainer = ctrl.Consequent(np.arange(0,1.1,0.1),'Fitness_trainer')
Politician = ctrl.Consequent(np.arange(0,1.1,0.1),'Politician')
Archeologist = ctrl.Consequent(np.arange(0,1.1,0.1),'Archeologist')
Poet = ctrl.Consequent(np.arange(0,1.1,0.1),'Poet')
Writer = ctrl.Consequent(np.arange(0,1.1,0.1),'Writer')
chemist = ctrl.Consequent(np.arange(0,1.1,0.1),'chemist')
Singer= ctrl.Consequent(np.arange(0,1.1,0.1),'Singer')
Bankmanager= ctrl.Consequent(np.arange(0,1.1,0.1),'Bankmanager')
psychologist= ctrl.Consequent(np.arange(0,1.1,0.1),'psychologist')
Physician= ctrl.Consequent(np.arange(0,1.1,0.1),'Physician')
Civilengineer= ctrl.Consequent(np.arange(0,1.1,0.1),'Civilengineer')
Insuranceagent= ctrl.Consequent(np.arange(0,1.1,0.1),'Insuranceagent')
Realestate= ctrl.Consequent(np.arange(0,1.1,0.1),'Realestate')
Telemarketer= ctrl.Consequent(np.arange(0,1.1,0.1),'Telemarketer')
work_around = ctrl.Consequent(np.arange(0,1.1,0.1),'work_around')

Engineering.automf(names=['Not_good','Good','Excellent'])
Medicine.automf(names=['Not_good','Good','Excellent'])
Hospitality.automf(names=['Not_good','Good','Excellent'])
Management.automf(names=['Not_good','Good','Excellent'])
Chief.automf(names=['Not_good','Good','Excellent'])
Teacher.automf(names=['Not_good','Good','Excellent'])
Researcher.automf(names=['Not_good','Good','Excellent'])
Architect.automf(names=['Not_good','Good','Excellent'])
Artist.automf(names=['Not_good','Good','Excellent'])
Athlete.automf(names=['Not_good','Good','Excellent'])
Fitness_trainer.automf(names=['Not_good','Good','Excellent'])
Politician.automf(names=['Not_good','Good','Excellent'])
Archeologist.automf(names=['Not_good','Good','Excellent'])
Poet.automf(names=['Not_good','Good','Excellent'])
Writer.automf(names=['Not_good','Good','Excellent'])
chemist.automf(names=['Not_good','Good','Excellent'])
Singer.automf(names=['Not_good','Good','Excellent'])
Bankmanager.automf(names=['Not_good','Good','Excellent'])
psychologist.automf(names=['Not_good','Good','Excellent'])
Physician.automf(names=['Not_good','Good','Excellent'])
Civilengineer.automf(names=['Not_good','Good','Excellent'])
Insuranceagent.automf(names=['Not_good','Good','Excellent'])
Realestate.automf(names=['Not_good','Good','Excellent'])
Telemarketer.automf(names=['Not_good','Good','Excellent'])
work_around.automf(names=['DUD'])

Engineering.view()
Medicine.view()
Management.view()
Hospitality.view()
Chief.view()
Teacher.view()
Researcher.view()
Architect.view()
Artist.view()
Athlete.view()
Fitness_trainer.view()
Politician.view()
Archeologist.view()
Poet.view()
Writer.view()
chemist.view()
Singer.view()
Bankmanager.view()
psychologist.view()
Physician.view()
Civilengineer.view()
Insuranceagent.view()
Realestate.view()
Telemarketer.view()
work_around.view()
