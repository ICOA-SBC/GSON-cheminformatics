import math
import pandas as pd
from nbautoeval import ExerciseFunctionPandas, Args, PPrintCallRenderer


def get_enrichment_data(similarity_df, similarity_measure, threshold):
    """
    This function calculates x and y values for enrichment plot:
    x - % ranked dataset
    y - % true actives identified
    """

    # Get number of molecules in data set
    mols_all = len(similarity_df)

    # Get number of active compounds in data set
    actives_all = sum(similarity_df.bioactivity >= threshold)

    # Initialize a list that will hold the counter for actives and compounds while iterating through our dataset
    actives_counter_list = []

    # Initialize counter for actives
    actives_counter = 0

    # Note: Data must be ranked for enrichment plots:
    # Sort compounds by selected similarity measure
    similarity_df.sort_values([similarity_measure], ascending=False, inplace=True)

    # Iterate over the ranked dataset and check each compound if active (by checking bioactivity)
    for value in similarity_df.bioactivity:
        if value >= threshold:
            actives_counter += 1
        actives_counter_list.append(actives_counter)

    # Transform number of molecules into % ranked dataset
    mols_perc_list = [i/mols_all for i in list(range(1, mols_all+1))]

    # Transform number of actives into % true actives identified
    actives_perc_list = [i/actives_all for i in actives_counter_list]

    # Generate DataFrame with x and y values as well as label
    enrich_df = pd.DataFrame({'% ranked dataset':mols_perc_list,
                              '% true actives identified':actives_perc_list,
                              'similarity_measure': similarity_measure})

    return enrich_df


similarity_df = pd.read_pickle('data/similarity_df_T4.p')

inputs_get_enrichment_data = [
    Args(similarity_df[['ChEMBL_ID',
                        'bioactivity',
                        'tanimoto_morgan']], 'tanimoto_morgan', 6.3),
    Args(similarity_df[['ChEMBL_ID',
                        'bioactivity',
                        'tanimoto_MACCS']], 'tanimoto_MACCS', 6.3),
    Args(similarity_df[['ChEMBL_ID',
                        'bioactivity',
                        'dice_MACCS']], 'dice_MACCS', 6.3),
    Args(similarity_df[['ChEMBL_ID',
                        'bioactivity',
                        'dice_morgan']], 'dice_morgan', 6.3),
]

exo_get_enrichment_data = ExerciseFunctionPandas(
    get_enrichment_data, inputs_get_enrichment_data,
    call_renderer=PPrintCallRenderer(
        show_function=False,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
    ))
