# Copyright (c) 2015 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_config import cfg

ec2_api_opt = cfg.BoolOpt('ec2_api',
                          default=True,
                          help='Does the test environment have the ec2 api '
                               'running?')

boto_group = cfg.OptGroup(name='boto',
                          title='EC2/S3 options')
BotoGroup = [
    cfg.StrOpt('ec2_url',
               default="http://localhost:8773/services/Cloud",
               help="EC2 URL"),
    cfg.StrOpt('s3_url',
               default="http://localhost:8080",
               help="S3 URL"),
    cfg.StrOpt('aws_secret',
               help="AWS Secret Key",
               secret=True),
    cfg.StrOpt('aws_access',
               help="AWS Access Key"),
    cfg.StrOpt('aws_zone',
               default="nova",
               help="AWS Zone for EC2 tests"),
    cfg.StrOpt('s3_materials_path',
               default="/opt/stack/devstack/files/images/"
                       "s3-materials/cirros-0.3.0",
               help="S3 Materials Path"),
    cfg.StrOpt('ari_manifest',
               default="cirros-0.3.0-x86_64-initrd.manifest.xml",
               help="ARI Ramdisk Image manifest"),
    cfg.StrOpt('ami_manifest',
               default="cirros-0.3.0-x86_64-blank.img.manifest.xml",
               help="AMI Machine Image manifest"),
    cfg.StrOpt('aki_manifest',
               default="cirros-0.3.0-x86_64-vmlinuz.manifest.xml",
               help="AKI Kernel Image manifest"),
    cfg.StrOpt('instance_type',
               default="m1.tiny",
               help="Instance type"),
    cfg.IntOpt('http_socket_timeout',
               default=3,
               help="boto Http socket timeout"),
    cfg.IntOpt('num_retries',
               default=1,
               help="boto num_retries on error"),
    cfg.IntOpt('build_timeout',
               default=60,
               help="Status Change Timeout"),
    cfg.IntOpt('build_interval',
               default=1,
               help="Status Change Test Interval"),
]
