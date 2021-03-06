# This file is part of Pynguin.
#
# Pynguin is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pynguin is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pynguin.  If not, see <https://www.gnu.org/licenses/>.

from pynguin.generation.export.unittestexporter import UnitTestExporter


def test_export_sequence(exportable_test_case, tmp_path):
    path = tmp_path / "generated.py"
    exporter = UnitTestExporter()
    exporter.export_sequences(str(path), [exportable_test_case, exportable_test_case])
    assert (
        path.read_text()
        == """# Automatically generated by Pynguin.
import unittest
import tests.fixtures.accessibles.accessible as module0


class GeneratedTestSuite(unittest.TestCase):

    def test_case_0(self):
        var0 = 5
        var1 = module0.SomeType(var0)

    def test_case_1(self):
        var0 = 5
        var1 = module0.SomeType(var0)
"""
    )
