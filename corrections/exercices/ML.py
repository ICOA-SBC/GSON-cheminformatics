from rdkit import Chem
from rdkit.Chem import PandasTools, MolFromSmiles, RDKFingerprint, MACCSkeys
from rdkit.Chem.AllChem import GetMorganFingerprintAsBitVect, GetHashedTopologicalTorsionFingerprintAsBitVect
from nbautoeval import ExerciseFunction, Args, PPrintCallRenderer, ExerciseFunctionPandas

def calculate_fp(mol, method='maccs', n_bits=2048):
    # mol = Chem molecule object
    # Function to calculate molecular fingerprints given the number of bits and the method
    if method == 'maccs':
        return MACCSkeys.GenMACCSKeys(mol)
    if method == 'ecfp4':
        return GetMorganFingerprintAsBitVect(mol, 2, nBits=n_bits, useFeatures=False)
    if method == 'ecfp6':
        return GetMorganFingerprintAsBitVect(mol, 3, nBits=n_bits, useFeatures=False)
    if method == 'torsion':
        return GetHashedTopologicalTorsionFingerprintAsBitVect(mol, nBits=n_bits)
    if method == 'rdk5':
        return RDKFingerprint(mol, maxPath=5, fpSize=1024, nBitsPerHash=2)

def print_fp(mol, method='maccs', n_bits=2048):
    return(calculate_fp(mol, method, n_bits).ToBitString())

smiles_1 = MolFromSmiles('CC(=O)NC1=CC=C(C=C1)O')
smiles_2 = MolFromSmiles('CN1CCN(CC1)C2=C3C=CC=CC3=NC4=C(N2)C=C(C=C4)C')
smiles_3 = MolFromSmiles('CCC1C(=O)N(CC(=O)N(C(C(=O)NC(C(=O)N(C(C(=O)NC(C(=O)NC\
(C(=O)N(C(C(=O)N(C(C(=O)N(C(C(=O)N(C(C(=O)N1)C(C(C)CC=CC)O)C)C(C)C)C)CC(C)C)C)CC(C)C)\
C)C)C)CC(C)C)C)C(C)C)CC(C)C)C)C')
smiles_4 = MolFromSmiles('CC1=C(C(CCC1)(C)C)C=CC(=CC=CC(=CC=CC=C(C)C=CC=C(C)C=CC2=C(CCCC2(C)C)C)C)C')
smiles_5 = MolFromSmiles('CCCCCC1=CC(=C(C(=C1)O)C2C=C(CCC2C(=C)C)C)O')
smiles_6 = MolFromSmiles('CC(=O)OC1=CC=CC=C1C(=O)O')
smiles_7 = MolFromSmiles('CN1CCC23C4C1CC5=C2C(=C(C=C5)O)OC3C(C=C4)O')


inputs_calculate_fp = [
    Args(smiles_1),
    Args(smiles_2, method='ecfp4'),
    Args(smiles_3, method='ecfp4', n_bits=1024),
    Args(smiles_4, method='ecfp6'),
    Args(smiles_5, method='torsion'),
    Args(smiles_6, method='rdk5'),
    Args(smiles_7, method='ecfp6', n_bits=1024),
]

exo_calculate_fp = ExerciseFunction(
    print_fp, inputs_calculate_fp,
    call_renderer=PPrintCallRenderer(
        show_function=True,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
    ))

# ________________________________________________________________________________
