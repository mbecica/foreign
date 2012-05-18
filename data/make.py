import json

countryTotals = {}
deptTotals = {}
yearCD = {}

jdata = open('aid.json')
data = json.load(jdata)
jdata.close()

'Dept, country, year'
for dept, d in data.iteritems():
	if dept not in yearCD:
		yearCD[dept] = {}
	for country, t in d.iteritems():
		for year, val in t.iteritems():
			try:
				val += 0
			except TypeError:
				val = 0
			if country not in yearCD[dept]:
				yearCD[dept][country] = {} 
			if year not in yearCD[dept][country]:
				yearCD[dept][country][year] = val 
	

'''
'Dept, year, country'
for dept, d in data.iteritems():
	if dept not in yearCD:
		yearCD[dept] = {}
	for country, t in d.iteritems():
		for year, val in t.iteritems():
			try:
				val += 0
			except TypeError:
				val = 0
			if year not in yearCD[dept]:
				yearCD[dept][year] = {} 
			if country not in yearCD[dept][year]:
				yearCD[dept][year][country] = val 
	
'Country, dept, year'
for dept, d in data.iteritems():
  for country, t in d.iteritems():
    if country not in yearCD:
      yearCD[country] = {}
    for year, val in t.iteritems():
      try:
        val += 0
      except TypeError:
        val = 0
      if dept not in yearCD[country]:
        yearCD[country][dept] = {} 
      if year not in yearCD[country][dept]:
        yearCD[country][dept][year] = val
	
'Year, Country, Dept'
for dept, d in data.iteritems():
	for country, t in d.iteritems():
		for date, val in t.iteritems():
			try:
				val += 0
			except TypeError:
			 	val = 0	
			if date not in yearCD:
				yearCD[date] = {}
			if country not in yearCD[date]:
				yearCD[date][country] = {} 
			if dept not in yearCD[date][country]:
				yearCD[date][country][dept] = val 
	
'Dept Totals'
for dept, d in data.iteritems():
	if dept not in deptTotals:
		deptTotals[dept] = {}
	for country, t in d.iteritems():
		for date, val in t.iteritems():
			try:
				val += 0
			except TypeError:
			 	val = 0	
			if date not in deptTotals[dept]:
				deptTotals[dept][date] = val
			else:
				deptTotals[dept][date] += val

'Country Totals'
for dept, d in data.iteritems():
	for country, t in d.iteritems():
		if country not in countryTotals:
			countryTotals[country] = {}
		for date, val in t.iteritems():
			try:
				val += 0
			except TypeError:
			 	val = 0	
			if date not in countryTotals[country]:
				countryTotals[country][date] = val
			else:
				countryTotals[country][date] += val

'''
f = open('dept_country_year.json', 'w')
f.write('[' + json.dumps(yearCD, separators = (',', ':')) + '];')
f.close()
