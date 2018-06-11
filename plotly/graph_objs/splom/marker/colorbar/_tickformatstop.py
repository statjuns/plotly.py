from plotly.basedatatypes import BaseTraceHierarchyType


class Tickformatstop(BaseTraceHierarchyType):

    # dtickrange
    # ----------
    @property
    def dtickrange(self):
        """
        range [*min*, *max*], where *min*, *max* - dtick values which
        describe some zoom level, it is possible to omit *min* or *max*
        value by passing *null*
    
        The 'dtickrange' property is an info array that may be specified as a
        list or tuple of 2 elements where:
    
    (0) The 'dtickrange[0]' property accepts values of any type
    (1) The 'dtickrange[1]' property accepts values of any type

        Returns
        -------
        list
        """
        return self['dtickrange']

    @dtickrange.setter
    def dtickrange(self, val):
        self['dtickrange'] = val

    # value
    # -----
    @property
    def value(self):
        """
        string - dtickformat for described zoom level, the same as
        *tickformat*
    
        The 'value' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['value']

    @value.setter
    def value(self, val):
        self['value'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'splom.marker.colorbar'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        dtickrange
            range [*min*, *max*], where *min*, *max* - dtick values
            which describe some zoom level, it is possible to omit
            *min* or *max* value by passing *null*
        value
            string - dtickformat for described zoom level, the same
            as *tickformat*
        """

    def __init__(self, dtickrange=None, value=None, **kwargs):
        """
        Construct a new Tickformatstop object
        
        Parameters
        ----------
        dtickrange
            range [*min*, *max*], where *min*, *max* - dtick values
            which describe some zoom level, it is possible to omit
            *min* or *max* value by passing *null*
        value
            string - dtickformat for described zoom level, the same
            as *tickformat*

        Returns
        -------
        Tickformatstop
        """
        super(Tickformatstop, self).__init__('tickformatstops')

        # Import validators
        # -----------------
        from plotly.validators.splom.marker.colorbar import (
            tickformatstop as v_tickformatstop
        )

        # Initialize validators
        # ---------------------
        self._validators['dtickrange'] = v_tickformatstop.DtickrangeValidator()
        self._validators['value'] = v_tickformatstop.ValueValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.dtickrange = dtickrange
        self.value = value

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
