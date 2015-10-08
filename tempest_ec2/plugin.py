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

import os

from tempest import config
from tempest.test_discover import plugins

from tempest_ec2 import config as ec2_config


class EC2TempestPlugin(plugins.TempestPlugin):
    def load_tests(self):
        base_path = os.path.split(os.path.dirname(
            os.path.abspath(__file__)))[0]
        test_dir = "tempest_ec2/tests"
        full_test_dir = os.path.join(base_path, test_dir)
        return full_test_dir, base_path

    def register_opts(self, conf):
        if not conf.get('boto', False):
            config.register_opt_group(conf, ec2_config.boto_group,
                                      ec2_config.BotoGroup)
        if not conf.get('compute_feature_enabled', False):
            if not hasattr(conf['compute_feature_enabled'], 'ec2_api'):
                conf.register_opt(ec2_config.ec2_api_opt,
                                  group='compute_feature_enabled')

    def get_opt_lists(self):
        return [('boto', config.BotoGroup)]
