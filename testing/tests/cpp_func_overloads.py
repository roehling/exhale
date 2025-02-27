# -*- coding: utf8 -*-
########################################################################################
# This file is part of exhale.  Copyright (c) 2017-2021, Stephen McDowell.             #
# Full BSD 3-Clause license available here:                                            #
#                                                                                      #
#                https://github.com/svenevs/exhale/blob/master/LICENSE                 #
########################################################################################
"""
Tests for the ``cpp_func_overloads`` project.
"""

from __future__ import unicode_literals

from testing.base import ExhaleTestCase
from testing.decorators import no_cleanup
from testing.hierarchies import compare_file_hierarchy, file_hierarchy


class CPPFuncOverloads(ExhaleTestCase):
    """
    Primary test class for project ``cpp_func_overloads``.
    """

    test_project = "cpp_func_overloads"
    """.. testproject:: cpp_func_overloads"""

    @no_cleanup
    def test_builds(self):
        """Test deliberately kept to serve as a perpetual reminder this is still broken."""
        self.app.build()

    def test_file_hierarchy(self):
        """Verify the file hierarchy."""
        compare_file_hierarchy(self, file_hierarchy(self.file_hierarchy_dict()))
