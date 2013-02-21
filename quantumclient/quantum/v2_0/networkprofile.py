# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
#@author Abhishek Raut, Cisco Systems
#@author Sergey Sudakovich, Cisco Systems

import logging
from quantumclient.quantum.v2_0 import ListCommand, ShowCommand, CreateCommand, DeleteCommand, UpdateCommand

RESOURCE = 'network_profile'


#TODO Finish parameters
class ListNetworkProfile(ListCommand):
    """List network profiles that belong to a given tenant."""

    resource = RESOURCE
    log = logging.getLogger(__name__ + '.ListNetworkProfile')
    _formatters = {}
    list_columns = ['id', 'name', 'segment_type', 'segment_range', 'multicast_ip_index', 'multicast_ip_range']


class ShowNetworkProfile(ShowCommand):
    """Show information of a given network profile."""

    resource = RESOURCE
    log = logging.getLogger(__name__ + '.ShowNetworkProfile')
    allow_names = False


class CreateNetworkProfile(CreateCommand):
    """Creates a network profile."""

    resource = RESOURCE
    log = logging.getLogger(__name__ + '.CreateNetworkProfile')

    def add_known_arguments(self, parser):
        #TODO Change to mutually exclusive groups
        parser.add_argument('name', help='Name for Network Profile')
        parser.add_argument('--vlan', dest='vlan', action='store_true', help='VLAN')
        parser.add_argument('--segment_range', help='Range for the Segment')
        parser.add_argument('--vxlan', dest='vxlan', action='store_true', help='VxLAN')
        parser.add_argument('--multicast_ip_range', help='Multicast IPv4 Range')
        parser.add_argument("--add-tenant", help="Add tenant to the network profile")
        parser.add_argument("--remove-tenant", help="Remove tenant from the network profile")


    def args2body(self, parsed_args):
        body = {'network_profile': {'name': parsed_args.name}}
        if parsed_args.vlan:
            body['network_profile'].update({'segment_type': 'vlan'})
        if parsed_args.vxlan:
            body['network_profile'].update({'segment_type': 'vxlan'})
        if parsed_args.segment_range:
            body['network_profile'].update({'segment_range': parsed_args.segment_range})
        if parsed_args.multicast_ip_range:
            body['network_profile'].update({'multicast_ip_range': parsed_args.multicast_ip_range})
        if parsed_args.add_tenant:
            body['network_profile'].update({'add_tenant': parsed_args.add_tenant})
        if parsed_args.remove_tenant:
            body['network_profile'].update({'remove_tenant': parsed_args.remove_tenant})
        return body


class DeleteNetworkProfile(DeleteCommand):
    """Delete a given network profile."""

    log = logging.getLogger(__name__ + '.DeleteNetworkProfile')
    resource = RESOURCE
    allow_names = False


class UpdateNetworkProfile(UpdateCommand):
    """Update network profile's information."""

    resource = RESOURCE
    log = logging.getLogger(__name__ + '.UpdateNetworkProfile')
