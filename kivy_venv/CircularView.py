#Circular view

from dna_features_viewer import BiopythonTranslator, CircularGraphicRecord
import matplotlib.pyplot as plt
from dna_features_viewer import BiopythonTranslator
from Bio import SeqIO
import numpy as np
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

#Class that only labels regulatory elements and coding sequences

class ExpressionUnitTranslator(BiopythonTranslator):
    def compute_feature_legend (self, feature):
        return feature.type
    def compute_feature_color(self, feature):
        color_map = {
            
            "origin_replcation": "1e794b", #green
            "CDS":  "#f6870d", #orange
            "regulatory":  "ff0000", #red
            "misc_recomb":  "707070", #grey
            "misc_feature":  "f886ff", #lavender
            "backbone":  "820068", #magenta
            "mRNA":"blue",
            "exon":"darkblue",
            "intron": "#fbf3f6"
        }
        return color_map[feature.type]

    def compute_feature_label(self,feature):
        if feature.type not in ["CDS", "regulatory", "mRNA", "gene", "source", "origin_replcation"]:
            return None
        else:
            return BiopythonTranslator.compute_feature_label(self,feature)
def rec_it (record):
    translator = ExpressionUnitTranslator()
    grecord = translator.translate_record(record, CircularGraphicRecord)
    grecord.top_position = 4800 #sequence index appearing at the top
    ax, _ = grecord.plot(figure_width = 4)
    ax.figure.savefig("C_show_circle.svg", bbox_inches = "tight")
    drawing = svg2rlg("C_show_circle.svg")
    renderPM.drawToFile(drawing, "circular.png", fmt="PNG")
