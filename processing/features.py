import os
import pandas as pd

from misc import DATA_DIR

# Define paths
MAP_DATA_DIR = os.path.join(DATA_DIR, 'map')
FEATURED_DATA_DIR = os.path.join(DATA_DIR, 'featured')

# Ensure the feature directory exists
os.makedirs(FEATURED_DATA_DIR, exist_ok=True)


def create_provinces():
    df = pd.read_csv(os.path.join(MAP_DATA_DIR, 'results_by_province.csv'), usecols=[
        'province_id', 'province'
    ]).drop_duplicates().dropna()

    additional_provinces_df = pd.DataFrame([
        {'province_id': 27, 'province': 'AFRIQUE DU SUD'},
        {'province_id': 28, 'province': 'BELGIQUE'},
        {'province_id': 29, 'province': 'CANADA'},
        {'province_id': 30, 'province': "ETATS - UNIS D'AMERIQUE"},
        {'province_id': 31, 'province': 'FRANCE'}
    ])

    province_df = pd.concat([df, additional_provinces_df], ignore_index=True).sort_values(by='province_id')
    province_df.to_csv(os.path.join(FEATURED_DATA_DIR, 'provinces.csv'), index=False)


def create_candidates():
    df = pd.read_csv(os.path.join(MAP_DATA_DIR, 'results_by_province.csv'), usecols=[
        'candidate_id', 'candidate_voting_number', 'candidate_name', 'candidate_surname',
        'candidate_firstname', 'candidate_gender', 'candidate_political_party'
    ]).drop_duplicates().dropna(subset=['candidate_voting_number'])

    df['candidate_voting_number'] = df['candidate_voting_number'].astype(int)
    df.sort_values(by='candidate_voting_number').to_csv(
        os.path.join(FEATURED_DATA_DIR, 'candidates.csv'), index=False
    )


def create_demographics():
    # Define columns with their respective data types
    dtype_mapping = {
        'province_id': 'Int64',
        'expected_polling_stations': 'Int64',
        'processed_polling_stations': 'Int64',
        'expected_voters': 'Int64',
        'valid_votes': 'Int64',
        'blank_votes': 'Int64',
        'total_voters': 'Int64'
    }

    # Read the necessary columns and set dtypes directly to optimize memory usage
    df = pd.read_csv(os.path.join(MAP_DATA_DIR, 'results_by_province.csv'), usecols=[
        'province_id', 'expected_polling_stations', 'processed_polling_stations', 'polling_stations_percentage',
        'expected_voters', 'valid_votes', 'blank_votes', 'total_voters', 'voters_percentage'
    ], dtype={col: dtype_mapping[col] for col in dtype_mapping}).drop_duplicates().dropna()

    ## recalculate the percentages
    df['valid_votes_percentage'] = round(df['valid_votes'] / df['total_voters'] * 100, 2)
    df['blank_votes_percentage'] = round(df['blank_votes'] / df['total_voters'] * 100, 2)
    df['polling_stations_percentage'] = round(df['processed_polling_stations'] / df['expected_polling_stations'] * 100, 2)
    df['voters_percentage'] = round(df['total_voters'] / df['expected_voters'] * 100, 2)

    df.sort_values(by='province_id').to_csv(
        os.path.join(FEATURED_DATA_DIR, 'demographics_by_province.csv'), index=False
    )


def create_places():
    voting_sites = pd.read_csv(os.path.join(MAP_DATA_DIR, 'voting_sites.csv'), usecols=['voting_site_id', 'district_id', 'voting_site_name'])
    districts = pd.read_csv(os.path.join(MAP_DATA_DIR, 'districts.csv'), usecols=['district_id', 'province_id', 'district'])
    provinces = pd.read_csv(os.path.join(FEATURED_DATA_DIR, 'provinces.csv'), usecols=['province_id', 'province'])

    df = voting_sites.merge(districts, on='district_id').merge(provinces, on='province_id')
    (df[['voting_site_id', 'district_id', 'province_id', 'voting_site_name', 'district', 'province']]
     .sort_values(by='province_id')
     .to_csv(os.path.join(FEATURED_DATA_DIR, 'places.csv'), index=False))


def pivoted_results_by_province():
    results = pd.read_csv(os.path.join(MAP_DATA_DIR, 'results_by_province.csv'), usecols=['province_id', 'candidate_id', 'candidate_votes'])

    df = results.pivot_table(index='province_id', columns='candidate_id', values='candidate_votes', fill_value=0)
    df = df.astype(int)
    df.reset_index(inplace=True)
    df.sort_values(by='province_id').to_csv(
        os.path.join(FEATURED_DATA_DIR, 'pivoted_results_by_province.csv'), index=False
    )


def pivoted_results_by_voting_site():
    results = pd.read_csv(os.path.join(MAP_DATA_DIR, 'results_by_voting_site.csv'), usecols=['voting_site_id', 'candidate_id', 'candidate_votes'])

    df = results.pivot_table(index='voting_site_id', columns='candidate_id', values='candidate_votes', fill_value=0)
    df = df.astype(int)
    df.reset_index(inplace=True)
    df.sort_values(by='voting_site_id').to_csv(
        os.path.join(FEATURED_DATA_DIR, 'pivoted_results_by_voting_site.csv'), index=False
    )


if __name__ == '__main__':
    create_provinces()
    create_candidates()
    create_demographics()
    create_places()
    pivoted_results_by_province()
    pivoted_results_by_voting_site()
