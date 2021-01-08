import pandas as pd
from nbautoeval import ExerciseFunction, Args, PPrintCallRenderer
from rdkit import DataStructs
from rdkit.ML.Cluster import Butina

fingerprints_str = pd.read_pickle('data/fingerprints_str_T5.p')

def Tanimoto_distance_matrix_from_str(fp_list_str):
    fp_list = [DataStructs.cDataStructs.CreateFromBitString(fp_str) for fp_str in fp_list_str]
    return Tanimoto_distance_matrix(fp_list)

# Calculate distance matrix for fingerprint list
def Tanimoto_distance_matrix(fp_list):
    dissimilarity_matrix = []
    for i in range(1,len(fp_list)):
        similarities = DataStructs.BulkTanimotoSimilarity(fp_list[i],fp_list[:i])
        # Since we need a distance matrix, calculate 1-x for every element in similarity matrix
        for sim in similarities:
            dissimilarity_matrix.append(1-sim)
    return dissimilarity_matrix

inputs_tan_dist_mat = [
    Args(fingerprints_str[0:3]),
    Args(fingerprints_str[0:1000])

]

exo_tan_dist_mat = ExerciseFunction(
    Tanimoto_distance_matrix_from_str, inputs_tan_dist_mat,
    call_renderer=PPrintCallRenderer(
        show_function=False,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
    ))


def ClusterFps_from_str(fp_list_str, cutoff=0.2):
    fp_list = [DataStructs.cDataStructs.CreateFromBitString(fp_str) for fp_str in fp_list_str]
    return ClusterFps(fp_list, cutoff=0.2)

# Input: Fingerprints and a threshold for the clustering
def ClusterFps(fps,cutoff=0.2):
    # Calculate Tanimoto distance matrix
    distance_matr = Tanimoto_distance_matrix(fps)
    # Now cluster the data with the implemented Butina algorithm:
    clusters = Butina.ClusterData(distance_matr,len(fps),cutoff,isDistData=True)
    return clusters

inputs_ClusterFps = [
    Args(fingerprints_str[0:3], cutoff=0.2),
    Args(fingerprints_str[0:1000], cutoff=0.2)
]

exo_clustFp = ExerciseFunction(
    ClusterFps_from_str, inputs_ClusterFps,
    call_renderer=PPrintCallRenderer(
        show_function=False,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
    ))


fp_clusters_str = pd.read_pickle('data/fingerprints_str_T5.p')


def IntraTanimoto_from_str(fp_list_str, cutoff=0.2):
    fp_list = [DataStructs.cDataStructs.CreateFromBitString(fp_str) for fp_str in fp_list_str]
    return IntraTanimoto(fps_clusters)

# Function to compute Tanimoto similarity for all pairs of fingerprints in each cluster
def IntraTanimoto(fps_clusters):
    intra_similarity =[]
    # Calculate intra similarity per cluster
    for k in range(0,len(fps_clusters)):
        # Tanimoto distance matrix function converted to similarity matrix (1-distance)
        intra_similarity.append([1-x for x in Tanimoto_distance_matrix(fps_clusters[k])])
    return intra_similarity

inputs_IntraTanimoto = [
    Args(fingerprints_str[0:2]),
    Args(fingerprints_str)
]

exo_IntraTanimoto = ExerciseFunction(
    IntraTanimoto_from_str, inputs_IntraTanimoto,
    call_renderer=PPrintCallRenderer(
        show_function=False,
        css_properties={'word-wrap': 'break-word', 'max-width': '40em'},
    ))
