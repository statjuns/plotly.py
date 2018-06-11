import _plotly_utils.basevalidators


class BgcolorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self, plotly_name='bgcolor', parent_name='cone.colorbar', **kwargs
    ):
        super(BgcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='colorbars',
            role='style',
            **kwargs
        )
