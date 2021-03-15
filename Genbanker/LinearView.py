#Download the DNA features Viewer library

#linear view with legend
import matplotlib.pyplot as plt
from dna_features_viewer import BiopythonTranslator
from Bio import SeqIO
import numpy as np

from dna_features_viewer import BiopythonTranslator

class CustomTranslator(BiopythonTranslator):
    #To determine the features's label
    label_areas = ['label', 'note', 'name', 'gene']

    def compute_feature_legend (self, feature):
        return feature.type

    #hex colors for feature legend color
    def compute_feature_color (self, feature):
        color_map = {
            "origin_replcation": "green", #green
            "CDS":  "orange", #orange
            "regulatory":  "red", #red
            "misc_recomb":  "grey", #grey
            "misc_feature":  "lavender", #lavender
            "backbone":  "magenta", #magenta
            "mRNA":  "lightblue", #light blue
            "gene":  "gold", #lavender
            "source":  "magenta", #magenta
        }
        return color_map[feature.type]

    #background color for legend box
    def compute_feature_box_background(self, feature):
        return "white"

    def compute_feature_box_lindewidth(self, feature):
        return 0
    
def rec_itL(file):
    translator = CustomTranslator()
    grecord = translator.translate_record(file)
    
    ax, _ = grecord.plot(figure_width=15, strand_in_label_threshold=9)
    grecord.plot_legend(ax=ax, loc=1, ncol=3, frameon=False)
    ax.figure.tight_layout()
    ax.figure.savefig("A_linear_graph.svg", bbox_inch="tight")

            
            
