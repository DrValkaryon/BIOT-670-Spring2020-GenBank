#Circular view

from dna_features_viewer import BiopythonTranslator, CircularGraphicRecord

#Class that only labels regulatory elements and coding sequences

class ExpressionUnitTranslator(BiopythonTranslator):
    def compute_feature_color(self, feature):
        color_map = {
            "origin_replcation": "1e794b", #green
            "CDS":  "#f6870d", #orange
            "regulatory":  "ff0000", #red
            "misc_recomb":  "d1e9f1", #light blue
            "misc_feature":  "f886ff", #lavender
            "backbone":  "820068", #magenta
        }
        return color_map[feature.type]

    def compute_feature_label(self,feature):
        if feature.type not in ["CDS", "regulatory"]:
            return None
        else:
            return BiopythonTranslator.compute_feature_label(self,feature)

translator = ExpressionUnitTranslator()
grecord = translator.translate_record("DNA.gb", CircularGraphicRecord)
grecord.top_position = 4800 #sequence index appearing at the top
ax, _ = grecord.plot(figure_width = 4)
ax.figure.savefig("C_show_circle.svg", bbox_inches = "tight")
