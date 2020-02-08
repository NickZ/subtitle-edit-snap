import snapcraft
import os
import textwrap

# Map bases to Ubuntu releases
_BASE_TO_UBUNTU_RELEASE_MAP = {"core16": "xenial", "core18": "bionic"}

class YourPlugin(snapcraft.BasePlugin):
    
    @classmethod
    def schema(cls):
        return {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'type': 'object',
            'additionalProperties': False,
            'properties': {},
        }

    def enable_cross_compilation(self):
        pass

    @property
    def PLUGIN_STAGE_SOURCES(self):
        mono_repo = "https://download.mono-project.com/repo/ubuntu/"
        ubuntu_repo = "http://us.${prefix}.ubuntu.com/${suffix}/"
        security_repo = "http://${security}.ubuntu.com/${suffix}/"

        return textwrap.dedent(
            """
            deb {mono_repo} {codename} main
            deb {ubuntu_repo} {codename} main universe
            deb {ubuntu_repo} {codename}-updates main universe
            deb {ubuntu_repo} {codename}-security main universe
            deb {security_repo} {codename}-security main universe
            """.format(
                mono_repo=mono_repo,
                ubuntu_repo=ubuntu_repo,
                security_repo=security_repo,
                codename=_BASE_TO_UBUNTU_RELEASE_MAP[self.project.info.base],
            )
        )

    def __init__(self, name, options, project):
        super().__init__(name, options, project)
        try:
            super().run(cmd = ["/usr/bin/apt-key", 
                            "adv", 
                            "--keyserver", 
                            "hkp://keyserver.ubuntu.com:80", 
                            "--recv-keys", 
                            "3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"], 
                        cwd=None)
        except:
            print("Could not add key to keychain")
