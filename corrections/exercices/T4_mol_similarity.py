import pandas as pd
from nbautoeval import ExerciseFunction, Args, PPrintCallRenderer


def calculate_enrichment_factor(enrichment, ranked_dataset_percentage_cutoff):
    """
    Get the experimental enrichment factor for a given percentage of the ranked dataset.

    Parameters
    ----------
    enrichment : pd.DataFrame
        Enrichment data: Percentage of ranked dataset by similarity vs. percentage of
        identified true actives.
    ranked_dataset_percentage_cutoff : float or int
        Percentage of ranked dataset to be included in enrichment factor calculation.

    Returns
    -------
    float
        Experimental enrichment factor.
    """

    # Keep only molecules that meet the cutoff
    enrichment = enrichment[
        enrichment["% ranked dataset"] <= ranked_dataset_percentage_cutoff / 100
    ]
    # Get highest percentage of actives and the corresponding percentage of actives
    highest_enrichment = enrichment.iloc[-1]
    enrichment_factor = round(100 * float(highest_enrichment["% true actives identified"]), 1)
    return enrichment_factor


enrichment_data = pd.read_pickle('data/enrichment_data_T4.p')

inputs_calc_EF = [
    Args(enrichment_data["tanimoto_maccs"], 4),
    Args(enrichment_data["tanimoto_maccs"], 5),
    Args(enrichment_data["tanimoto_maccs"], 6),
    Args(enrichment_data["tanimoto_morgan"], 4),
    Args(enrichment_data["tanimoto_morgan"], 5),
    Args(enrichment_data["tanimoto_morgan"], 6),
]

exo_calc_EF = ExerciseFunction(
    calculate_enrichment_factor, inputs_calc_EF,
    call_renderer=PPrintCallRenderer(
        show_function=False,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
    ))


def calculate_enrichment_factor_optimal(molecules, ranked_dataset_percentage_cutoff, pic50_cutoff):
    """
    Get the optimal random enrichment factor for a given percentage of the ranked dataset.

    Parameters
    ----------
    molecules : pandas.DataFrame
        the DataFrame with all the molecules and pIC50.
    ranked_dataset_percentage_cutoff : float or int
        Percentage of ranked dataset to be included in enrichment factor calculation.
    activity_cutoff: float
        pIC50 cutoff value used to discriminate active and inactive molecules

    Returns
    -------
    float
        Optimal enrichment factor.
    """

    ratio = sum(molecules["pIC50"] >= pic50_cutoff) / len(molecules) * 100
    if ranked_dataset_percentage_cutoff <= ratio:
        enrichment_factor_optimal = round(100 / ratio * ranked_dataset_percentage_cutoff, 1)
    else:
        enrichment_factor_optimal = 100.0
    return enrichment_factor_optimal

molsim_df = pd.read_pickle('data/molsim_df_T4.p')

inputs_calc_EF_opt = [
    Args(molsim_df[["molecule_chembl_id", "pIC50"]], 5, 6.3),
    Args(molsim_df[["molecule_chembl_id", "pIC50"]], 10, 6.3),
    Args(molsim_df[["molecule_chembl_id", "pIC50"]], 5, 10.0),
]

exo_calc_EF_opt = ExerciseFunction(
    calculate_enrichment_factor_optimal, inputs_calc_EF_opt,
    call_renderer=PPrintCallRenderer(
        show_function=False,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
    ))
