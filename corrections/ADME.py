from rdkit import Chem
from rdkit.Chem import Descriptors
import pandas as pd
from nbautoeval import ExerciseFunction, Args, CallRenderer, PPrintRenderer, PPrintCallRenderer
    
def rule_of_five(smi):
#     Lcondition = [(name, True) if [Descriptors.ExactMolWt(Chem.MolFromSmiles(molecule)) <= 500, Descriptors.NumHAcceptors(Chem.MolFromSmiles(molecule)) <= 10, Descriptors.NumHDonors(Chem.MolFromSmiles(molecule)) <= 5, Descriptors.MolLogP(Chem.MolFromSmiles(molecule)) <= 5].count(True) >= 3 else (name, False) for name, molecule in smi.items()]
#     return Lcondition if len(Lcondition) > 1 else Lcondition[0]

    Lcondition = []
    for name, molecule in smi.items():
    
        # Calculate rule of five chemical properties
        m = Chem.MolFromSmiles(molecule)
        MW = Descriptors.ExactMolWt(m)
        HBA = Descriptors.NumHAcceptors(m)
        HBD = Descriptors.NumHDonors(m)
        LogP = Descriptors.MolLogP(m)
        
        # Rule of five conditions
        Lcondition.append((name, [MW <= 500, HBA <= 10, HBD <= 5, LogP <= 5].count(True) >= 3))
        # Return True if no more than one out of four conditions is violated
    
    return Lcondition if len(Lcondition)>1 else Lcondition[0]

smiles_1 = {'Paracetamol' : 'CC(=O)NC1=CC=C(C=C1)O'}
smiles_2 = {'Clozapine' : 'CN1CCN(CC1)C2=C3C=CC=CC3=NC4=C(N2)C=C(C=C4)C'}
smiles_3 = {'Cyclosporine' :  'CCC1C(=O)N(CC(=O)N(C(C(=O)NC(C(=O)N(C(C(=O)NC(C(=O)NC\
(C(=O)N(C(C(=O)N(C(C(=O)N(C(C(=O)N(C(C(=O)N1)C(C(C)CC=CC)O)C)C(C)C)C)CC(C)C)C)CC(C)C)\
C)C)C)CC(C)C)C)C(C)C)CC(C)C)C)C'}
smiles_4 = {'Beta-carotene' : 'CC1=C(C(CCC1)(C)C)C=CC(=CC=CC(=CC=CC=C(C)C=CC=C(C)C=CC2=C(CCCC2(C)C)C)C)C'}
smiles_5 = {'Cannabidiol' : 'CCCCCC1=CC(=C(C(=C1)O)C2C=C(CCC2C(=C)C)C)O'}
smiles_6 = {'Aspirine' : 'CC(=O)OC1=CC=CC=C1C(=O)O'}
smiles_7 = {'Morphine' : 'CN1CCC23C4C1CC5=C2C(=C(C=C5)O)OC3C(C=C4)O'}
D_smiles = {**smiles_5, **smiles_6, **smiles_7}

inputs_rule_of_five = [
    Args(smiles_1),
    Args(D_smiles),
    Args(smiles_2),
    Args(smiles_3),

]

exo_rule_of_five = ExerciseFunction(
    rule_of_five, inputs_rule_of_five,
    call_renderer=PPrintCallRenderer(
        show_function=False,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
        ))

#________________________________________________________________________________

#def df_rule_of_five(df):
#    
#    m = Chem.MolFromSmiles(df['smiles'])
#    
#    # Calculate rule of five chemical properties
#    MW = Descriptors.ExactMolWt(m)
#    HBA = Descriptors.NumHAcceptors(m)
#    HBD = Descriptors.NumHDonors(m)
#    LogP = Descriptors.MolLogP(m)
#    
#    # Rule of five conditions
#    conditions = [MW <= 500, HBA <= 10, HBD <= 5, LogP <= 5]
#    
#    # Create pandas row for conditions results with values and information whether rule of five is violated
#    return pd.Series([MW, HBA, HBD, LogP, 'yes']) if conditions.count(True) >= 3 else pd.Series([MW, HBA, HBD, LogP, 'no'])
    

def df_rule_of_five(df):
    
    Lsmi = df['smiles']
    Ldescriptors = []
    for smi in Lsmi:
        m = Chem.MolFromSmiles(smi)

        # Calculate rule of five chemical properties
        MW = Descriptors.ExactMolWt(m)
        HBA = Descriptors.NumHAcceptors(m)
        HBD = Descriptors.NumHDonors(m)
        LogP = Descriptors.MolLogP(m)

        # Rule of five conditions
        if [MW <= 500, HBA <= 10, HBD <= 5, LogP <= 5].count(True) >= 3:
            Ldescriptors.append(pd.Series([MW, HBA, HBD, LogP, 'yes']))
        else:
            Ldescriptors.append(pd.Series([MW, HBA, HBD, LogP, 'no']))
    # Create pandas row for conditions results with values and information whether rule of five is violated
    rule5_prop_df = pd.DataFrame(Ldescriptors)
    rule5_prop_df.columns = ['MW', 'HBA', 'HBD', 'LogP', 'rule_of_five_conform']
    df = df.join(rule5_prop_df)
    return(df)

ChEMBL_df = pd.read_csv('../data/T1/EGFR_compounds.csv', index_col=0)

inputs_df_rule_of_five = [
    Args(ChEMBL_df.head())
]

exo_df_rule_of_five = ExerciseFunction(
    df_rule_of_five, inputs_df_rule_of_five,
    call_renderer=PPrintCallRenderer(
        show_function=False,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
        ))

#________________________________________________________________________________

def get_properties_stats(data_df):
    """
    Function that calculates the mean and standard deviation of physicochemical properties of a dataset.
    
    Input: 
    Dataset containing per compound values for physicochemical properties
    HBD, HBA, MW and LogP as columns (with exactly these names).
    
    Output:
    Dataframe with mean and std (columns) for each physicochemical property (rows).
    """
    properties = ["HBD", "HBA", "MW", "LogP"]
    
    data_stats = []
    
    for i in properties:
        std = data_df[i].std()
        mean = data_df[i].mean()
        da = pd.DataFrame([[round(mean, 2), round(std, 2)]], index=[i], columns=["mean", "std"])
        data_stats.append(da)
    
    data_stats = pd.concat(data_stats)
    
    return data_stats

filtered_df = pd.read_csv('../data/T2/EGFR_compounds_lipinski.csv', index_col=0, sep=';')

inputs_get_properties_stats = [
    Args(filtered_df.head())
]

exo_get_properties_stats = ExerciseFunction(
    get_properties_stats, inputs_get_properties_stats,
    call_renderer=PPrintCallRenderer(
        show_function=False,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
        ))
