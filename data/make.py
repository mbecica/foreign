import json

countryTotals = {}
deptTotals = {}

jdata = open('aid.json')
data = json.load(jdata)
jdata.close()

cdata = open('countryList.json')
countries = json.load(cdata)
cdata.close()

'''
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
'''

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

f = open('countryTotals.json', 'w')
f.write('[' + json.dumps(countryTotals, separators = (',', ':')) + '];')
f.close()
