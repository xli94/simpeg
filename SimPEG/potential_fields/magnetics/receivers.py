import properties
import numpy as np
from ... import survey


class point_receiver(survey.BaseRx):
    """
    Magnetic point receiver class for integral formulation

    :param numpy.ndarray locs: receiver locations index (ie. :code:`np.c_[ind_1, ind_2, ...]`)
    :param string component: receiver component
         "dbx_dx", "dbx_dy", "dbx_dz", "dby_dy",
         "dby_dz", "dbz_dz", "bx", "by", "bz", "tmi" [default]
    """

    # receiver_index = None

    # component = properties.List(
    #     "Must be a magnetic component of the type",


    #     default=["tmi"]
    # )

    def __init__(self, locations, components={"tmi": []}, **kwargs):

        if isinstance(components, str):
            components = {components: []}

        if isinstance(components, list):
            componentList = components.copy()
            components = {}
            for component in componentList:
                components = {component: []}

        assert np.all([component in [
            "dbx_dx", "dbx_dy", "dbx_dz", "dby_dy",
            "dby_dz", "dbz_dz", "bx", "by", "bz", "tmi"
             ] for component in list(components.keys())]), (
                "Components {0!s} not known. Components must be in "
                "'dbx_dx', 'dbx_dy', 'dbx_dz', 'dby_dy',"
                "'dby_dz', 'dbz_dz', 'bx', 'by', 'bz', 'tmi'. "
                "Arbitrary orientations have not yet been "
                "implemented.".format(components)
            )
        self.components = components

        super(survey.BaseRx, self).__init__(locations=locations, components=components, **kwargs)


    # def __init__(self, component=component, **kwargs):

    #     self.component = component

        # super(point_receiver, self).__init__(location_index, **kwargs)

    def nD(self):

        if self.receiver_index is not None:

            return self.location_index.shape[0]

        elif self.locations is not None:

            return self.locations.shape[0]

        else:

            return None

    def receiver_index(self):

        return self.receiver_index
