from json import JSONEncoder


class Mate(JSONEncoder):
    def __init__(self, material_0_index: int, material_1_index: int, blend_weight: float, unknown: int):
        """
        Object definition of a single material entry in a .mate file

        :param material_0_index:    Index of 0th material
        :param material_1_index:    Index of 1st material
        :param blend_weight:        Amount to blend two materials
        :param unknown:             Unknown
        """
        self.material_0_index = material_0_index
        self.material_1_index = material_1_index
        self.blend_weight = blend_weight
        self.unknown = unknown

    # def __str__(self) -> str:
    #     """
    #     Returns an informal string representation of object
    #
    #     :return:    String representation of object
    #     """
    #     return "Mate \{ material_0_index: {0}, material_1_index: {1}, blend_weight: {2}, unknown: {3} \}".format(
    #         self.material_0_index,
    #         self.material_1_index,
    #         self.blend_weight,
    #         self.unknown
    #     )

    # def __repr__(self) -> str:
    #     """
    #     Returns a printable representation of object
    #
    #     :return:    String representation of object
    #     """
    #     return repr({
    #         "material_0_index": self.material_0_index,
    #         "material_1_index": self.material_1_index,
    #         "blend_weight": self.blend_weight,
    #         "unknown": self.unknown
    #     })

    def to_json(self):
        return {
            "material_0_index": self.material_0_index,
            "material_1_index": self.material_1_index,
            "blend_weight": self.blend_weight,
            "unknown": self.unknown
        }
