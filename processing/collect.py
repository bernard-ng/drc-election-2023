import requests
from misc import API_BASE_URL, PROVINCE_ID_RANGE, save_json_dataset, save_csv_dataset


def fetch_districts():
    data = []

    for i in PROVINCE_ID_RANGE:
        response = requests.get(f'{API_BASE_URL}?c={i}')
        if response.status_code == 200:
            data.extend(response.json())

    save_json_dataset(data, 'districts.json')
    save_csv_dataset(data, 'districts.csv')

    return data


def fetch_voting_sites(district_id: str):
    response = requests.get(f'{API_BASE_URL}?sv={district_id}')

    if response.status_code == 200:
        data = response.json()

        for site in data:
            site['circonscription_id'] = district_id

        return data
    else:
        return []


def fetch_result_by_province(province_id: str):
    response = requests.get(f'{API_BASE_URL}?value={province_id}&type=pres&circ=province')

    if response.status_code == 200:
        return response.json()
    else:
        return []


def fetch_result_by_voting_site(voting_site_id: str):
    response = requests.get(f'{API_BASE_URL}?value={voting_site_id}&type=pres&circ=sv')

    if response.status_code == 200:
        return response.json()
    else:
        return []


if __name__ == "__main__":
    districts = fetch_districts()

    voting_sites = []
    for district in districts:
        voting_sites.extend(fetch_voting_sites(district['district_id']))

    save_json_dataset(voting_sites, 'voting_sites.json')
    save_csv_dataset(voting_sites, 'voting_sites.csv')

    results_by_province = {}
    results = []
    for province in PROVINCE_ID_RANGE:
        data = fetch_result_by_province(province)
        results_by_province[province] = data
        results.extend(data)

    save_json_dataset(results_by_province, 'results_by_province.json')
    save_csv_dataset(results, 'results_by_province.csv')

    result_by_voting_sites = {}
    results = []
    for site in voting_sites:
        data = fetch_result_by_voting_site(site['site_vote_id'])
        result_by_voting_sites[site['site_vote_id']] = data
        results.extend(data)

    save_json_dataset(result_by_voting_sites, 'result_by_voting_sites.json')
    save_csv_dataset(results, 'result_by_voting_sites.csv', [
        'site_vote_id', 'candidat_id', 'voixobtenues', 'pour_cand',
        'nom', 'postnom', 'prenom', 'sexe', 'sigle', 'img'
    ])
