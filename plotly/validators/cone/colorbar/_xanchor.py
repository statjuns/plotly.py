import _plotly_utils.basevalidators


class XanchorValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='xanchor', parent_name='cone.colorbar', **kwargs
    ):
        super(XanchorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='colorbars',
            role='style',
            values=['left', 'center', 'right'],
            **kwargs
        )
