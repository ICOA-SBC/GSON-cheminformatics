import math
import pandas as pd
from nbautoeval import ExerciseFunctionPandas, Args, PPrintCallRenderer


def convert_nM(df):
    Lbioact_nM = []
    for i, row in df.iterrows():
        unit = row['units']
        bioactivity = row['value']
        if unit != "nM":
            if unit == "pM":
                value = float(bioactivity) / 1000
            elif unit == "10'-11M":
                value = float(bioactivity) / 100
            elif unit == "10'-10M":
                value = float(bioactivity) / 10
            elif unit == "10'-8M":
                value = float(bioactivity) * 10
            elif unit == "10'-1microM" or unit == "10'-7M":
                value = float(bioactivity) * 100
            elif unit == "uM" or unit == "/uM" or unit == "10'-6M":
                value = float(bioactivity) * 1000
            elif unit == "10'1 uM":
                value = float(bioactivity) * 10000
            elif unit == "10'2 uM":
                value = float(bioactivity) * 100000
            elif unit == "mM":
                value = float(bioactivity) * 1000000
            elif unit == "M":
                value = float(bioactivity) * 1000000000
            else:
                print('unit not recognized...', unit)
            Lbioact_nM.append(value)
        else:
            Lbioact_nM.append(bioactivity)
    df['value'] = Lbioact_nM
    df['units'] = 'nM'
    return df


bioact_df = pd.read_pickle('data/bioact_df_T1_ChEMBL.p')

inputs_convert_nM = [
    Args(bioact_df[bioact_df.units == 'uM'].sample(4)[['value', 'units']]),
    Args(bioact_df[bioact_df.units == 'nM'].sample(4)[['value', 'units']]),
    Args(bioact_df[bioact_df.units == 'M'].sample(2)[['value', 'units']]),
    Args(bioact_df[bioact_df.units == "10'-1microM"].sample(4)[['value', 'units']]),
    Args(bioact_df[bioact_df.units == "10'1 uM"].sample(4)[['value', 'units']]),
    Args(bioact_df[bioact_df.units == "10'2 uM"].sample(4)[['value', 'units']]),
    Args(bioact_df[bioact_df.units == "/uM"].sample(4)[['value', 'units']]),
    Args(bioact_df[bioact_df.units == "mM"].sample(2)[['value', 'units']]),
]

exo_convert_nM = ExerciseFunctionPandas(
    convert_nM, inputs_convert_nM,
    call_renderer=PPrintCallRenderer(
        show_function=False,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
    ))


def calc_pIC50(df):
    LIC50 = list(df['IC50'])
    LpIC50 = []
    for IC50 in LIC50:
        IC50 = float(IC50)  # IC50 comes as a string, it must be converted to float to calculate pIC50
        pIC50 = 9 - math.log10(IC50)  # pIC50=-log10(IC50 mol/l) --> for nM: -log10(IC50*10**-9)= 9-log10(IC50)
        if pIC50 < 0:
            print(f"Negative pIC50 value for {IC50}")
        LpIC50.append(pIC50)
    df['pIC50'] = LpIC50
    return df


df_IC50 = pd.read_pickle('data/df_IC50_T1_ChEMBL.p')

inputs_calc_pIC50 = [
    Args(df_IC50[['IC50', 'units']].sample(10)),
    Args(df_IC50[['IC50', 'units']].sample(10)),
    Args(df_IC50[['IC50', 'units']].sample(10)),
    Args(df_IC50[['IC50', 'units']].sample(10)),
    Args(df_IC50[['IC50', 'units']].sample(10))
]

exo_calc_pIC50 = ExerciseFunctionPandas(
    calc_pIC50, inputs_calc_pIC50,
    call_renderer=PPrintCallRenderer(
        show_function=False,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
    ))
