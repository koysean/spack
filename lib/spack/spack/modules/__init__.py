# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""This package contains code for creating environment modules, which can
include Tcl non-hierarchical modules, Lua hierarchical modules, and others.
"""

from typing import Dict, Type

from .common import BaseConfiguration, BaseModuleFileWriter, disable_modules
from .lmod import LmodConfiguration, LmodModulefileWriter
from .tcl import TclConfiguration, TclModulefileWriter

__all__ = ["TclModulefileWriter", "LmodModulefileWriter", "disable_modules"]

module_types: Dict[str, Type[BaseModuleFileWriter]] = {
    "tcl": TclModulefileWriter,
    "lmod": LmodModulefileWriter,
}
module_config_types: Dict[str, Type[BaseConfiguration]] = {
    "tcl": TclConfiguration,
    "lmod": LmodConfiguration,
}
