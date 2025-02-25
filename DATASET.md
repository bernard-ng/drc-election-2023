# Dataset Description

This document provides an overview of the dataset files and their respective mappings to standardized column names.

## Files and Column Mappings

### 1. districts.csv
This file contains information about districts and their corresponding province identifiers.

| Original Column Name     | Standardized Column Name |
|-------------------------|-------------------------|
| circonscription        | district                |
| circonscription_id     | district_id             |
| province_id           | province_id             |

### 2. voting_sites.csv
This file lists the voting sites, including their names and corresponding district identifiers.

| Original Column Name     | Standardized Column Name |
|-------------------------|-------------------------|
| nom_sv                 | voting_site_name        |
| site_vote_id           | voting_site_id          |
| circonscription_id     | district_id             |

### 3. results_by_province.csv
This file provides election results aggregated by province.

| Original Column Name     | Standardized Column Name                 |
|-------------------------|-----------------------------------------|
| province_id            | province_id                             |
| ordre_bulletin        | candidate_voting_number                 |
| candidat_id          | candidate_id                             |
| nom                  | candidate_name                           |
| postnom              | candidate_surname                        |
| prenom               | candidate_firstname                      |
| sigle                | candidate_political_party                |
| sexe                 | candidate_gender                         |
| voixobtenues         | candidate_votes                          |
| pour_cand            | candidate_percentage                     |
| bv_attendus          | expected_polling_stations               |
| bv_traites           | processed_polling_stations               |
| pour_bv              | processed_polling_stations_percentage    |
| electeurs_attendus   | expected_voters                          |
| pour_votants         | voters_percentage                        |
| bulletins_valides    | valid_votes                              |
| bulletins_blancs     | blank_votes                              |
| total_votants        | total_voters                             |

### 4. results_by_voting_site.csv
This file contains election results at the voting site level.

| Original Column Name     | Standardized Column Name |
|-------------------------|-------------------------|
| site_vote_id           | voting_site_id          |
| candidat_id           | candidate_id            |
| voixobtenues         | candidate_votes         |
| pour_cand            | candidate_percentage    |
| nom                  | candidate_name         |
| postnom              | candidate_surname      |
| prenom               | candidate_firstname    |
| sexe                 | candidate_gender       |
| sigle                | candidate_political_party |

