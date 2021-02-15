#Circular view

from dna_features_viewer import BiopythonTranslator, CircularGraphicRecord

#Class that only labels regulatory elements and coding sequences

class ExpressionUnitTranslator(BiopythonTranslator):
    def compute_feature_color(self, feature):
        color_map = {
            
            "origin_replcation": "green", #green
            "CDS":  "orange", #orange
            "regulatory":  "red", #red
            "mRNA":  "lightblue", #light blue
            "gene":  "gold", #lavender
            "source":  "magenta", #magenta
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
