import requests
import json
import time



r = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = r.json()

# returns the absolute value of the counter
t1 = time.perf_counter()

results = []

for package in packages_json:

	package_name = package['name']

	package_desc = package['desc']

	package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'

	req = requests.get(package_url)
	package_json = req.json()

	package_str = json.dumps(package_json, indent=2)

	installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]

	installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]

	installs_365 = package_json['analytics']['install_on_request']['365d'][package_name]

	data = {
		'name': package_name,
		'desc': package_desc,
		'analytics': {
			'30d': installs_30,
			'90d': installs_90,
			'365d': installs_365
		}
	}

	results.append(data)

	# elapsed measures the time between sending the request and finishing parsing the response headers,
	# not until the full response has been transfered
	time.sleep(req.elapsed.total_seconds())
	print(f'Got {package_name} in {req.elapsed.total_seconds()} seconds')

	# stops the loop
	if package_name == 'apache-drill':
		break

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')

with open('package_info.json', 'w') as f:
	json.dump(results, f, indent=2)




