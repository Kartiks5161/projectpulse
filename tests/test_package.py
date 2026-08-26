"""Initial package-level tests."""

import unittest

import projectpulse


class PackageTests(unittest.TestCase):
    """Verify the initial package metadata."""

    def test_package_has_version(self) -> None:
        """The package exposes a version for reports and reproducibility."""
        self.assertEqual(projectpulse.__version__, "0.1.0")


if __name__ == "__main__":
    unittest.main()
