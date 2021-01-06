from rdkit import Chem
from rdkit.Chem import PandasTools, Descriptors, rdMolDescriptors, Lipinski
import pandas as pd
from nbautoeval import ExerciseFunction, Args, PPrintCallRenderer
PandasTools.ChangeMoleculeRendering(renderer='String')


def get_frags_number(df):
    New_column = pd.DataFrame({'Frags_number': [len(Chem.rdmolops.GetMolFrags(mol)) for mol in df['ROMol']]})
    New_column = New_column.set_index(df.index)
    return New_column


df_meds = PandasTools.LoadSDF('./data/meds.sdf', isomericSmiles=True).drop(columns=['molecule_synonyms'])
df_meds = df_meds[df_meds['molecule_type'] == 'Small molecule']

inputs_frags_number = [
    Args(df_meds[['ROMol']].head()),
    Args(df_meds[['ROMol']])
]

exo_frags_number = ExerciseFunction(
    get_frags_number, inputs_frags_number,
    call_renderer=PPrintCallRenderer(
        show_function=False,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
    ))

# ________________________________________________________________________________


def get_descriptors(df):
    Lmol = df['ROMol']
    Ldescriptors = []
    for m in Lmol:

        # Calculer les propriétés chimiques
        MW = round(Descriptors.ExactMolWt(m), 1)
        LogP = round(Descriptors.MolLogP(m), 1)
        TPSA = round(Descriptors.TPSA(m), 1)
        LabuteASA = round(Descriptors.LabuteASA(m), 1)
        HBA = Descriptors.NumHAcceptors(m)
        HBD = Descriptors.NumHDonors(m)
        FCSP3 = Lipinski.FractionCSP3(m)
        MQN8 = rdMolDescriptors.MQNs_(m)[7]
        MQN10 = rdMolDescriptors.MQNs_(m)[9]
        NAR = Lipinski.NumAromaticRings(m)
        NRB = Chem.Descriptors.NumRotatableBonds(m)

        Ldescriptors.append([MW, LogP, TPSA, LabuteASA, HBA, HBD, FCSP3, MQN8, MQN10, NAR, NRB])

    # Create pandas row for conditions results with values and information whether rule of five is violated
    prop_df = pd.DataFrame(Ldescriptors)
    prop_df.columns = ['MW', 'LogP', 'TPSA', 'LabuteASA', 'HBA', 'HBD', 'FCSP3', 'MQN8', 'MQN10', 'NAR', 'NRB']
    prop_df = prop_df.set_index(df.index)

    return prop_df


df_meds['Frags_number'] = get_frags_number(df_meds)
df_meds = df_meds[df_meds['Frags_number'] == 1]
df_meds.dropna(subset=['first_approval'], inplace=True)
df_meds['first_approval'] = df_meds['first_approval'].astype(float)
df_meds = df_meds[df_meds['first_approval'] >= 2000]
df_PCA = df_meds[['natural_product', 'ROMol']]

inputs_df_descriptors = [
    Args(df_PCA[['ROMol']].head()),
    Args(df_PCA[['ROMol']])
]

exo_df_descriptors = ExerciseFunction(
    get_descriptors, inputs_df_descriptors,
    call_renderer=PPrintCallRenderer(
        show_function=False,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
    ))

# ________________________________________________________________________________


def get_administration_type(df):
    Ladm = []
    for a, b in df[['oral', 'parenteral', 'topical']].iterrows():
        oral = b[0]
        parenteral = b[1]
        topical = b[2]
        if oral == 'True' and parenteral == 'False' and topical == 'False':
            Ladm.append('O')
        elif parenteral == 'True' and oral == 'False' and topical == 'False':
            Ladm.append('P')
        elif topical == 'True' and parenteral == 'False' and oral == 'False':
            Ladm.append('T')
        else:
            Ladm.append('M')

    New_column = pd.DataFrame({'Administration': Ladm})
    New_column = New_column.set_index(df.index)
    return New_column


inputs_get_administration_type = [
    Args(df_meds[['oral', 'parenteral', 'topical']].head()),
    Args(df_meds[['oral', 'parenteral', 'topical']])
]

exo_get_administration_type = ExerciseFunction(
    get_administration_type, inputs_get_administration_type,
    call_renderer=PPrintCallRenderer(
        show_function=False,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
    ))
