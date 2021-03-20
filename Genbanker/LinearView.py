#Download the DNA features Viewer library

#linear view with legend
import matplotlib.pyplot as plt
from dna_features_viewer import BiopythonTranslator
from Bio import SeqIO
import numpy as np

from dna_features_viewer import BiopythonTranslator
import matplotlib.pyplot as plt
from dna_features_viewer import BiopythonTranslator
from Bio import SeqIO
import numpy as np
from bokeh.embed import file_html
from bokeh.resources import CDN
       
            

class CustomTranslator(BiopythonTranslator):
    #To determine the features's label
    label_fields = ['label', 'note', 'name', 'gene']

    def compute_feature_legend (self, feature):
        return feature.type

    #hex colors for feature legend color
    def compute_feature_color (self, feature):
        return {
            "origin_replcation": "1e794b", #green
            "CDS":  "#f6870d", #orange
            "regulatory":  "ff0000", #red
            "misc_recomb":  "707070", #grey
            "misc_feature":  "f886ff", #lavender
            "backbone":  "820068", #magenta
            "mRNA":"blue",
            "exon":"darkblue",
            "intron": "#fbf3f6"
        }[feature.type]

    #background color for legend box
    def compute_feature_box_background(self, feature):
        return "white"

    def compute_feature_box_lindewidth(self, feature):
        return 0
    
def rec_itL(file):
    translator = CustomTranslator()
    graphic_record = translator.translate_record(file)
    ax,_ = graphic_record.plot(figure_width = 13, strand_in_label_threshold=7)

    graphic_record.plot_legend(ax=ax, loc = 1, ncol = 3, frameon = False)
    ax.figure.savefig("linear_from_paper.svg", bbox_inches = "tight")
    bokeh_plot = graphic_record.plot_with_bokeh(figure_width=10, figure_height=2)
    html = file_html(bokeh_plot, CDN, "my plot")
    with open("F_bokeh_plot.html", "w") as f:
        f.write(html) 
