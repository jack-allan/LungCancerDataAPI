#
# validator.py
# Created: October 30th, 2017
# Contributors: Jack Allan and Natalie Lampa
# jackall@umich.edu, nlampa@umich.edu
#
#

import requests

#base url for using kgrid server activartor
url = "http://"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache", #?
    'postman-token': "830323d5-1a21-4458-50d7-e0c0b3bb55eb" #?
    }

#model specific urls
bach_url
marcus_url
park_url



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
		id.marcus_age = i
		id.marcus_sex = j
		id.marcus_smok_durat = k
		id.marcus_copd = l
		id.marcus_prior_diag = m
		id.marcus_early_onset = n
		id.marcus_late_onset = o

		#park model
		id.park_age = p
		id.park_smok_status = q
		id.park_asi = r
		id.park_bmi = s
		id.park_phys_activ = t
		id.park_fasting_gluc = u



#how to make it patient specific/does it need to be patient specific if it is called line by line 
	#and automatically written to the spreadsheet

 def bach(id, bach_age, bach_cpd, bach_yrs_smok, bach_yrs_quit, bach_asbestos, bach_sex, 
		bach_quit):
	

	payload = "{\"age\":bach_age, \"cpd\":bach_cpd, \"yrsSmok\":bach_yrs_smok, \
		\"yrsQuit\":bach_yrs_quit, \"asbestos\":bach_asbestos, \"sex\":bach_sex, \"quit\":bach_quit}" 
		#?is this the right way to split up lines?

	response = requests.request("POST", bach_url, data=payload headers=headers)
	bach_data = json.loads(response.content)

	return bach_data


def marcus(id, marcus_age, marcus_sex, marcus_smok_durat, marcus_copd, marcus_prior_diag,
		marcus_early_onset, marcus_late_onset):
	

	payload = "{\"age\":marcus_age,\"sex\":marcus_sex,\"smokDurat\":marcus_smok_durat,\
		\"copd\":marcus_copd,\"priorDiag\":marcus_prior_diag,\"earlyOnset\":marcus_early_onset,\
		\"lateOnset\":marcus_late_onset}"

	response = requests.request("POST", url, data=payload, headers=headers)
	marcus_data = json.loads(response.content)

	return marcus_data


def park(id, park_age, park_smok_status, park_asi, park_bmi, park_phys_activ, park_fasting_gluc):


	payload = "{\"age\":park_age,\"smokerStatus\":park_smok_status,\"asi\":park_asi,\
		\"bmi\":park_bmi,\"physActiv\":park_phys_activ,\"fastingGluc\":park_fasting_gluc}"


	response = requests.request("POST", url, data=payload, headers=headers)
	park_data = json.loads(response.content)

	return park_data




