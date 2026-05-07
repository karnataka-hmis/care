from plugs.manager import PlugManager
from plugs.plug import Plug  # noqa: F401

plugs = [
    Plug(
        name="care_state_hmis",
        package_name="git+https://github.com/10bedicu/care_state_hmis.git",
        version="@main",
        configs={},
    ),
    Plug(
        name="abdm",
        package_name="git+https://github.com/10bedicu/care_abdm.git",
        version="@production",
        configs={},
    ),
    Plug(
        name="care_kutumba",
        package_name="git+https://github.com/10bedicu/care_kutumba.git",
        version="@main",
        configs={},
    ),
    Plug(
        name="care_scribe",
        package_name="git+https://github.com/10bedicu/care_scribe.git",
        version="@master",
        configs={},
    ),
]


manager = PlugManager(plugs)

