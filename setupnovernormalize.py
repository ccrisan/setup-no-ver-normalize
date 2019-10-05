
import pkg_resources

from setuptools.extern.packaging import version as packaging_version


# Patch Version class to preserve original version string
class NoNormalizeVersion(packaging_version.Version):
    def __init__(self, version):
        self._orig_version = version
        super().__init__(version)

    def __str__(self):
        return self._orig_version


packaging_version.Version = NoNormalizeVersion


# Patch safe_version() to prevent version normalization
pkg_resources.safe_version = lambda v: v
