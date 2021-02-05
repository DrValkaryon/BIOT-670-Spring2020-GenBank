#Download the DNA features Viewer library

#linear view with legend

from dna_features_viewer import BiopythonTranslator

class CustomTranslator(BiophythonTranslator):

    #To determine the features's label
    label_areas = ["label", "note", "name", "gene"]

    def compute_feature_legend (self, feature):
        return feature.type

    #hex colors for feature legend color
    def compute_feature_color (self, feature):
        return {
            "origin_replcation":  "1e794b", #green
            "CDS":  "#f6870d", #orange
            "regulatory":  "ff0000", #red
            "misc_recomb":  "d1e9f1", #light blue
            "misc_feature":  "f886ff", #lavender
            "backbone":  "820068", #magenta
            )[feature.type]

    #background color for legend box
    def compute_feature_box_background(self, feature):
        return "ffffff"

    def compute_feature_box_lindewidth(self, feature):
        return 0

translator = CustomTranslator()
graphic-record = translator.translate_record("DNA.gb")
ax, _ = graphic_record.plot(figure_width=15, strand_in_label_threshold=7)
graphic_record.plot_legend(ax=ax, loc=1, ncol=3, frameon=False)
ax.figure.savefig("A_linear_graph.svg", bbox_inch="tight")

            
            
