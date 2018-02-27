test = {

    'name': '4B',
    'points': 3,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The name 'mean_ts_face_voxel' should be present
                    >>> 'mean_ts_face_voxel' in vars()
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The name 'centered_ts_face_voxel' should be present
                    >>> 'centered_ts_face_voxel' in vars()
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The name 'fig_ts_face_voxel' should be present
                    >>> 'fig_ts_face_voxel' in vars()
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The name 'fig_ts_face_voxel' should be a figure
                    >>> import matplotlib
                    >>> isinstance(fig_ts_face_voxel, matplotlib.figure.Figure)
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '',
            'teardown': '',
            'type': 'doctest'
        },
        
]}