import os
import pandas as pd

from misc import DATA_DIR

# Define paths
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
MAP_DATA_DIR = os.path.join(DATA_DIR, 'map')

# Ensure the map directory exists
os.makedirs(os.path.join(DATA_DIR, 'map'), exist_ok=True)


MAPPING = {
    'districts.csv': {
        'circonscription': 'district',
        'circonscription_id': 'district_id',
        'province_id': 'province_id',
    },
    'voting_sites.csv': {
        'nom_sv': 'voting_site_name',
        'site_vote_id': 'voting_site_id',
        'circonscription_id': 'district_id',
    },
    'results_by_province.csv': {
        'province_id': 'province_id',
        'ordre_bulletin': 'candidate_voting_number',
        'candidat_id': 'candidate_id',
        'nom': 'candidate_name',
        'postnom': 'candidate_surname',
        'prenom': 'candidate_firstname',
        'sigle': 'candidate_political_party',
        'sexe': 'candidate_gender',
        'voixobtenues': 'candidate_votes',
        'pour_cand': 'candidate_percentage',
        'bv_attendus': 'expected_polling_stations',
        'bv_traites': 'processed_polling_stations',
        'pour_bv': 'polling_stations_percentage',
        'electeurs_attendus': 'expected_voters',
        'pour_votants': 'voters_percentage',
        'bulletins_valides': 'valid_votes',
        'bulletins_blancs': 'blank_votes',
        'total_votants': 'total_voters',
    },
    'results_by_voting_site.csv': {
        'site_vote_id': 'voting_site_id',
        'candidat_id': 'candidate_id',
        'voixobtenues': 'candidate_votes',
        'pour_cand': 'candidate_percentage',
        'nom': 'candidate_name',
        'postnom': 'candidate_surname',
        'prenom': 'candidate_firstname',
        'sexe': 'candidate_gender',
        'sigle': 'candidate_political_party',
    },
}


if __name__ == '__main__':
    for filename, columns_mapping in MAPPING.items():
        df = pd.read_csv(os.path.join(RAW_DATA_DIR, filename))
        df.rename(columns=columns_mapping, inplace=True)

        ## drop img column in results datasets
        if 'img' in df.columns:
            df.drop(columns=['img'], inplace=True)

        ## upper case data
        df = df.map(lambda x: x.upper() if isinstance(x, str) else x)

        df.to_csv(os.path.join(MAP_DATA_DIR, filename), index=False)
        print(f">> {filename} remapped")
