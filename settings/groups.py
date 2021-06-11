from libqtile.config import Group

group_settings = [
    (
        "1",
        {
            "label": "",
            "layout": "monadtall",
        }
    ),
    (
        "2",
        {
            "label": "",
            "layout": "max"
        }
    ),
    (
        "3",
        {
            "label": "",
            "layout": "max"
        }
    ),
    (
        "4",
        {
            "label": "",
            "layout": "max"
        }
    ),
    (
        "5",
        {
            "label": "",
            "layout": "max"
        }
    ),
    (
        "6",
        {
            "label": "",
            "layout": "max"
        }
    ),
    (
        "7",
        {
            "label": "",
            "layout": "monadtall"
        }
    ),
    (
        "8",
        {
            "label": "♬",
            "layout": "monadtall"
        }
    )
]

exports = [Group(name, **kwargs) for name, kwargs in group_settings]
