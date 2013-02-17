import sys

from quantumclient.tests.unit.test_cli20 import CLITestV20Base
from quantumclient.quantum.v2_0.networkprofile import CreateNetworkProfile
from quantumclient.tests.unit.test_cli20 import MyApp


class CLITestV20Port(CLITestV20Base):

    def test_create_networkprofile(self):
        resource = 'network-profile'
        cmd = CreateNetworkProfile(MyApp(sys.stdout), None)
        name = 'test_np'
        vlan = '--vlan'
        args = [vlan]
        position_names = []
        position_values = []
        position_values.extend([])
        self._test_create_resource(resource, cmd, name, args, position_names, position_values)

