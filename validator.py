#
# validator.py
# Created: October 30th, 2017
# Contributors: Jack Allan and Natalie Lampa
# jackall@umich.edu, nlampa@umich.edu
#
#



class patient:
	"""A patient class containing all model variables"""

	def __init__(id, b, c, d, e, f, g, h, i, j, k, l, m , n, o, p, q, r, s, t):
		#bach model
		id.bach_age = b
		id.bach_cpd = c
		id.bach_yrs_smok = d
		id.bach_yrs_quit = e
		id.bach_asbestos = f
		id.bach_sex = g #0 male, 1 female 
		id.bach_quit = h #0 no, 1 yes

		#marcus model
		id.marcus_sex = i
		id.marcus_smok_durat = j
		id.marcus_copd = k
		id.marcus_prior_diag = l
		id.marcus_early_onset = m
		id.marcus_late_onset = n

		#park model
		id.park_age = o
		id.park_smok_status = p
		id.park_asi = q
		id.park_bmi = r
		id.park_phys_activ = s
		id.park_fasting_gluc = t





>>> def bach(id, bach_age, bach_cpd, bach_yrs_smok, bach_yrs_quit, bach_asbestos, bach_sex, 
		bach_quit):
	
	age = bach_age
	cpd = bach_cpd
	yrsSmok = bach_yrs_smok
	yrsQuit = bach_yrs_quit
	asbestos = bach_asbestos
	sex = bach_sex
	quit = bach_quit


	#POST Command
	#unpack what is returned




>>>def marcus():
	pass



>>>def park():
	pass