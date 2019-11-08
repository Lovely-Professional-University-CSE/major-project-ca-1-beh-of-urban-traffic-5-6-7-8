#importing library

import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

'''
What is Antecedent and Consequent?

A consequent is the second half of a hypothetical proposition.
In the standard form of such a proposition, it is the part that follows "then".
In an implication, if P implies Q,
then P is called the antecedent and Q is called the consequent. 
'''

# adding antecedent function
Physics = ctrl.Antecedent(np.arange(0,101,1),'Physics')
Maths = ctrl.Antecedent(np.arange(0,101,1),'Maths')
Chemistry = ctrl.Antecedent(np.arange(0,101,1),'Chemistry')
Biology = ctrl.Antecedent(np.arange(0,101,1),'Biology')
Business = ctrl.Antecedent(np.arange(0,101,1),'Business')
Accountancy = ctrl.Antecedent(np.arange(0,101,1),'Accountancy')
PE = ctrl.Antecedent(np.arange(0,101,1),'PE')
CS = ctrl.Antecedent(np.arange(0,101,1),'CS')
History = ctrl.Antecedent(np.arange(0,101,1),'History')
Geography = ctrl.Antecedent(np.arange(0,101,1),'Geography')
Politics = ctrl.Antecedent(np.arange(0,101,1),'Politics')
Economy = ctrl.Antecedent(np.arange(0,101,1),'Economy')
Literature = ctrl.Antecedent(np.arange(0,101,1),'Literature')
Language = ctrl.Antecedent(np.arange(0,101,1),'Language')
Art = ctrl.Antecedent(np.arange(0,101,1),'Art')

'''
What is membership fumction???

Membership functions allow us to graphically represent a fuzzy set.
The x axis represents the universe of discourse, whereas
the y axis represents the degrees of membership in the [0,1] interval.

'''


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

Business['Excellent'] = fuzzy.trapmf(Business.universe,[70,85,100,100])
Business['Good'] = fuzzy.trapmf(Business.universe,[55,70,75,75])
Business['Average'] = fuzzy.trapmf(Business.universe,[38,55,60,60])
Business['Poor'] = fuzzy.trapmf(Business.universe,[25,30,40,40])
Business['Very_Poor'] = fuzzy.trapmf(Business.universe,[0,15,25,25])

Accountancy['Excellent'] = fuzzy.trapmf(Accountancy.universe,[70,85,100,100])
Accountancy['Good'] = fuzzy.trapmf(Accountancy.universe,[55,70,75,75])
Accountancy['Average'] = fuzzy.trapmf(Accountancy.universe,[38,55,60,60])
Accountancy['Poor'] = fuzzy.trapmf(Accountancy.universe,[25,30,40,40])
Accountancy['Very_Poor'] = fuzzy.trapmf(Accountancy.universe,[0,15,25,25])

PE['Excellent'] = fuzzy.trapmf(PE.universe,[70,85,100,100])
PE['Good'] = fuzzy.trapmf(PE.universe,[55,70,75,75])
PE['Average'] = fuzzy.trapmf(PE.universe,[38,55,60,60])
PE['Poor'] = fuzzy.trapmf(PE.universe,[25,30,40,40])
PE['Very_Poor'] = fuzzy.trapmf(PE.universe,[0,15,25,25])

CS['Excellent'] = fuzzy.trapmf(CS.universe,[70,85,100,100])
CS['Good'] = fuzzy.trapmf(CS.universe,[55,70,75,75])
CS['Average'] = fuzzy.trapmf(CS.universe,[38,55,60,60])
CS['Poor'] = fuzzy.trapmf(CS.universe,[25,30,40,40])
CS['Very_Poor'] = fuzzy.trapmf(CS.universe,[0,15,25,25])

History['Excellent'] = fuzzy.trapmf(History.universe,[70,85,100,100])
History['Good'] = fuzzy.trapmf(History.universe,[55,70,75,75])
History['Average'] = fuzzy.trapmf(History.universe,[38,55,60,60])
History['Poor'] = fuzzy.trapmf(History.universe,[25,30,40,40])
History['Very_Poor'] = fuzzy.trapmf(History.universe,[0,15,25,25])

Geography['Excellent'] = fuzzy.trapmf(Geography.universe,[70,85,100,100])
Geography['Good'] = fuzzy.trapmf(Geography.universe,[55,70,75,75])
Geography['Average'] = fuzzy.trapmf(Geography.universe,[38,55,60,60])
Geography['Poor'] = fuzzy.trapmf(Geography.universe,[25,30,40,40])
Geography['Very_Poor'] = fuzzy.trapmf(Geography.universe,[0,15,25,25])

Economy['Excellent'] = fuzzy.trapmf(Economy.universe,[70,85,100,100])
Economy['Good'] = fuzzy.trapmf(Economy.universe,[55,70,75,75])
Economy['Average'] = fuzzy.trapmf(Economy.universe,[38,55,60,60])
Economy['Poor'] = fuzzy.trapmf(Economy.universe,[25,30,40,40])
Economy['Very_Poor'] = fuzzy.trapmf(Economy.universe,[0,15,25,25])

Politics['Excellent'] = fuzzy.trapmf(Politics.universe,[70,85,100,100])
Politics['Good'] = fuzzy.trapmf(Politics.universe,[55,70,75,75])
Politics['Average'] = fuzzy.trapmf(Politics.universe,[38,55,60,60])
Politics['Poor'] = fuzzy.trapmf(Politics.universe,[25,30,40,40])
Politics['Very_Poor'] = fuzzy.trapmf(Politics.universe,[0,15,25,25])

Literature['Excellent'] = fuzzy.trapmf(Literature.universe,[70,85,100,100])
Literature['Good'] = fuzzy.trapmf(Literature.universe,[55,70,75,75])
Literature['Average'] = fuzzy.trapmf(Literature.universe,[38,55,60,60])
Literature['Poor'] = fuzzy.trapmf(Literature.universe,[25,30,40,40])
Literature['Very_Poor'] = fuzzy.trapmf(Literature.universe,[0,15,25,25])

Language['Excellent'] = fuzzy.trapmf(Language.universe,[70,85,100,100])
Language['Good'] = fuzzy.trapmf(Language.universe,[55,70,75,75])
Language['Average'] = fuzzy.trapmf(Language.universe,[38,55,60,60])
Language['Poor'] = fuzzy.trapmf(Language.universe,[25,30,40,40])
Language['Very_Poor'] = fuzzy.trapmf(Language.universe,[0,15,25,25])

Art['Excellent'] = fuzzy.trapmf(Art.universe,[70,85,100,100])
Art['Good'] = fuzzy.trapmf(Art.universe,[55,70,75,75])
Art['Average'] = fuzzy.trapmf(Art.universe,[38,55,60,60])
Art['Poor'] = fuzzy.trapmf(Art.universe,[25,30,40,40])
Art['Very_Poor'] = fuzzy.trapmf(Art.universe,[0,15,25,25])




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

rule1 = ctrl.Rule(Physics['Excellent'] & Maths['Excellent'] & Chemistry['Excellent'], Engineering['Excellent'])
rule2 = ctrl.Rule(Physics['Excellent'] & Maths['Excellent'] & Chemistry['Good'], Engineering['Excellent'])
rule3 = ctrl.Rule(Physics['Excellent'] & Maths['Excellent'] & Chemistry['Average'], Engineering['Excellent'])
rule4 = ctrl.Rule(Physics['Excellent'] & Maths['Good'] & Chemistry['Excellent'], Engineering['Excellent'])
rule5 = ctrl.Rule(Physics['Excellent'] & Maths['Good'] & Chemistry['Good'], Engineering['Excellent'])
rule6 = ctrl.Rule(Physics['Excellent'] & Maths['Good'] & Chemistry['Average'], Engineering['Excellent'])
rule7 = ctrl.Rule(Physics['Excellent'] & Maths['Average'] & Chemistry['Excellent'], Engineering['Good'])
rule8 = ctrl.Rule(Physics['Excellent'] & Maths['Average'] & Chemistry['Good'], Engineering['Good'])
rule9 = ctrl.Rule(Physics['Excellent'] & Maths['Average'] & Chemistry['Average'], Engineering['Good'])

rule10 = ctrl.Rule(Physics['Good'] & Maths['Excellent'] & Chemistry['Excellent'], Engineering['Excellent'])
rule12 = ctrl.Rule(Physics['Good'] & Maths['Excellent'] & Chemistry['Good'], Engineering['Good'])
rule13 = ctrl.Rule(Physics['Good'] & Maths['Excellent'] & Chemistry['Average'], Engineering['Good'])
rule11 = ctrl.Rule(Physics['Good'] & Maths['Good'] & Chemistry['Excellent'], Engineering['Good'])
rule14 = ctrl.Rule(Physics['Good'] & Maths['Good'] & Chemistry['Good'], Engineering['Good'])
rule15 = ctrl.Rule(Physics['Good'] & Maths['Good'] & Chemistry['Average'], Engineering['Good'])
rule16 = ctrl.Rule(Physics['Good'] & Maths['Average'] & Chemistry['Excellent'], Engineering['Good'])
rule17 = ctrl.Rule(Physics['Good'] & Maths['Average'] & Chemistry['Good'], Engineering['Good'])
rule18 = ctrl.Rule(Physics['Good'] & Maths['Average'] & Chemistry['Average'], Engineering['Good'])

rule19 = ctrl.Rule(Physics['Average'] & Maths['Excellent'] & Chemistry['Excellent'], Engineering['Good'])
rule20 = ctrl.Rule(Physics['Average'] & Maths['Excellent'] & Chemistry['Good'], Engineering['Good'])
rule21 = ctrl.Rule(Physics['Average'] & Maths['Excellent'] & Chemistry['Average'], Engineering['Good'])
rule22 = ctrl.Rule(Physics['Average'] & Maths['Good'] & Chemistry['Excellent'], Engineering['Good'])
rule23 = ctrl.Rule(Physics['Average'] & Maths['Good'] & Chemistry['Good'], Engineering['Good'])
rule24 = ctrl.Rule(Physics['Average'] & Maths['Good'] & Chemistry['Average'], Engineering['Good'])
rule25 = ctrl.Rule(Physics['Average'] & Maths['Average'] & Chemistry['Excellent'], Engineering['Not_good'])
rule26 = ctrl.Rule(Physics['Average'] & Maths['Average'] & Chemistry['Good'], Engineering['Not_good'])
rule27 = ctrl.Rule(Physics['Average'] & Maths['Average'] & Chemistry['Average'], Engineering['Not_good'])


rule28 = ctrl.Rule(Physics['Excellent'] & Biology['Excellent'] & Chemistry['Excellent'], Medicine['Excellent'])
rule29 = ctrl.Rule(Physics['Excellent'] & Biology['Excellent'] & Chemistry['Good'], Medicine['Excellent'])
rule30 = ctrl.Rule(Physics['Excellent'] & Biology['Excellent'] & Chemistry['Average'], Medicine['Excellent'])
rule31 = ctrl.Rule(Physics['Excellent'] & Biology['Good'] & Chemistry['Excellent'], Medicine['Excellent'])
rule32 = ctrl.Rule(Physics['Excellent'] & Biology['Good'] & Chemistry['Good'], Medicine['Excellent'])
rule33 = ctrl.Rule(Physics['Excellent'] & Biology['Good'] & Chemistry['Average'], Medicine['Excellent'])
rule34 = ctrl.Rule(Physics['Excellent'] & Biology['Average'] & Chemistry['Excellent'], Medicine['Good'])
rule35 = ctrl.Rule(Physics['Excellent'] & Biology['Average'] & Chemistry['Good'], Medicine['Good'])
rule36 = ctrl.Rule(Physics['Excellent'] & Biology['Average'] & Chemistry['Average'], Medicine['Good'])

rule37 = ctrl.Rule(Physics['Good'] & Biology['Excellent'] & Chemistry['Excellent'], Medicine['Excellent'])
rule38 = ctrl.Rule(Physics['Good'] & Biology['Excellent'] & Chemistry['Good'], Medicine['Good'])
rule39 = ctrl.Rule(Physics['Good'] & Biology['Excellent'] & Chemistry['Average'], Medicine['Good'])
rule40 = ctrl.Rule(Physics['Good'] & Biology['Good'] & Chemistry['Excellent'], Medicine['Good'])
rule41 = ctrl.Rule(Physics['Good'] & Biology['Good'] & Chemistry['Good'], Medicine['Good'])
rule42 = ctrl.Rule(Physics['Good'] & Biology['Good'] & Chemistry['Average'], Medicine['Good'])
rule43 = ctrl.Rule(Physics['Good'] & Biology['Average'] & Chemistry['Excellent'], Medicine['Good'])
rule44 = ctrl.Rule(Physics['Good'] & Biology['Average'] & Chemistry['Good'], Medicine['Good'])
rule46 = ctrl.Rule(Physics['Good'] & Biology['Average'] & Chemistry['Average'], Medicine['Good'])

rule47 = ctrl.Rule(Physics['Average'] & Biology['Excellent'] & Chemistry['Excellent'], Medicine['Good'])
rule48 = ctrl.Rule(Physics['Average'] & Biology['Excellent'] & Chemistry['Good'], Medicine['Good'])
rule49 = ctrl.Rule(Physics['Average'] & Biology['Excellent'] & Chemistry['Average'], Medicine['Good'])
rule50 = ctrl.Rule(Physics['Average'] & Biology['Good'] & Chemistry['Excellent'], Medicine['Good'])
rule51 = ctrl.Rule(Physics['Average'] & Biology['Good'] & Chemistry['Good'], Medicine['Good'])
rule52 = ctrl.Rule(Physics['Average'] & Biology['Good'] & Chemistry['Average'], Medicine['Good'])
rule53 = ctrl.Rule(Physics['Average'] & Biology['Average'] & Chemistry['Excellent'], Medicine['Not_good'])
rule54 = ctrl.Rule(Physics['Average'] & Biology['Average'] & Chemistry['Good'], Medicine['Not_good'])
rule45 = ctrl.Rule(Physics['Average'] & Biology['Average'] & Chemistry['Average'], Medicine['Not_good'])

rule55 = ctrl.Rule(Accountancy['Excellent'] & Business['Excellent'], Management['Excellent'])
rule56 = ctrl.Rule(Accountancy['Good'] & Business['Excellent'], Management['Excellent'])
rule57 = ctrl.Rule(Accountancy['Average'] & Business['Excellent'], Management['Good'])
rule58 = ctrl.Rule(Accountancy['Excellent'] & Business['Good'], Management['Excellent'])
rule59 = ctrl.Rule(Accountancy['Good'] & Business['Good'], Management['Good'])
rule60 = ctrl.Rule(Accountancy['Average'] & Business['Good'], Management['Not_good'])
rule61 = ctrl.Rule(Accountancy['Excellent'] & Business['Average'], Management['Good'])
rule62 = ctrl.Rule(Accountancy['Good'] & Business['Average'], Management['Good'])
rule63 = ctrl.Rule(Accountancy['Average'] & Business['Average'], Management['Not_good'])

rule64 = ctrl.Rule(Language['Excellent'] & Business['Excellent'], Hospitality['Excellent'])
rule65 = ctrl.Rule(Language['Good'] & Business['Excellent'], Hospitality['Excellent'])
rule66 = ctrl.Rule(Language['Average'] & Business['Excellent'], Hospitality['Good'])
rule67 = ctrl.Rule(Language['Excellent'] & Business['Good'], Hospitality['Excellent'])
rule68 = ctrl.Rule(Language['Good'] & Business['Good'], Hospitality['Good'])
rule69 = ctrl.Rule(Language['Average'] & Business['Good'], Hospitality['Not_good'])
rule70 = ctrl.Rule(Language['Excellent'] & Business['Average'], Hospitality['Good'])
rule71 = ctrl.Rule(Language['Good'] & Business['Average'], Hospitality['Good'])
rule72 = ctrl.Rule(Language['Average'] & Business['Average'], Hospitality['Not_good'])


rule73 = ctrl.Rule(Art['Excellent'] & Language['Excellent'] & History['Excellent'], Chief['Excellent'])
rule74 = ctrl.Rule(Art['Excellent'] & Language['Excellent'] & History['Good'], Chief['Excellent'])
rule75 = ctrl.Rule(Art['Excellent'] & Language['Excellent'] & History['Average'], Chief['Excellent'])
rule76 = ctrl.Rule(Art['Excellent'] & Language['Good'] & History['Excellent'], Chief['Excellent'])
rule77 = ctrl.Rule(Art['Excellent'] & Language['Good'] & History['Good'], Chief['Excellent'])
rule79 = ctrl.Rule(Art['Excellent'] & Language['Good'] & History['Average'], Chief['Excellent'])
rule80 = ctrl.Rule(Art['Excellent'] & Language['Average'] & History['Excellent'], Chief['Excellent'])
rule81 = ctrl.Rule(Art['Excellent'] & Language['Average'] & History['Good'], Chief['Good'])
rule82 = ctrl.Rule(Art['Excellent'] & Language['Average'] & History['Average'], Chief['Good'])

rule83 = ctrl.Rule(Art['Good'] & Language['Excellent'] & History['Excellent'], Chief['Excellent'])
rule84 = ctrl.Rule(Art['Good'] & Language['Excellent'] & History['Good'], Chief['Good'])
rule85 = ctrl.Rule(Art['Good'] & Language['Excellent'] & History['Average'], Chief['Good'])
rule86 = ctrl.Rule(Art['Good'] & Language['Good'] & History['Excellent'], Chief['Good'])
rule87 = ctrl.Rule(Art['Good'] & Language['Good'] & History['Good'], Chief['Good'])
rule88 = ctrl.Rule(Art['Good'] & Language['Good'] & History['Average'], Chief['Good'])
rule89 = ctrl.Rule(Art['Good'] & Language['Average'] & History['Excellent'], Chief['Good'])
rule90 = ctrl.Rule(Art['Good'] & Language['Average'] & History['Good'], Chief['Good'])
rule91 = ctrl.Rule(Art['Good'] & Language['Average'] & History['Average'], Chief['Good'])

rule92 = ctrl.Rule(Art['Average'] & Language['Excellent'] & History['Excellent'], Chief['Good'])
rule93 = ctrl.Rule(Art['Average'] & Language['Excellent'] & History['Good'], Chief['Good'])
rule94 = ctrl.Rule(Art['Average'] & Language['Excellent'] & History['Average'], Chief['Good'])
rule95 = ctrl.Rule(Art['Average'] & Language['Good'] & History['Excellent'], Chief['Good'])
rule96 = ctrl.Rule(Art['Average'] & Language['Good'] & History['Good'], Chief['Good'])
rule97 = ctrl.Rule(Art['Average'] & Language['Good'] & History['Average'], Chief['Good'])
rule98 = ctrl.Rule(Art['Average'] & Language['Average'] & History['Excellent'], Chief['Not_good'])
rule99 = ctrl.Rule(Art['Average'] & Language['Average'] & History['Good'], Chief['Not_good'])
rule78 = ctrl.Rule(Art['Average'] & Language['Average'] & History['Average'], Chief['Not_good'])

