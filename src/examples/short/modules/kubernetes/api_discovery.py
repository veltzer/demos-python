# Copyright 2016 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Reads the list of available API versions and prints them. Similar to running
`kubectl api-versions`.
"""

import kubernetes.client
import kubernetes.config


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    kubernetes.config.load_kube_config()

    print("Supported APIs (* is preferred version):")
    versions = ",".join(kubernetes.client.CoreApi().get_api_versions().versions)
    core = "core"
    print(f"{core:<40} {versions}")
    for api in kubernetes.client.ApisApi().get_api_versions().groups:
        versions = []
        for v in api.versions:
            name = ""
            if v.version == api.preferred_version.version and len(
                    api.versions) > 1:
                name += "*"
            name += v.version
            versions.append(name)
        versions_str = ",".join(versions)
        print(f"{api.name:<40} {versions_str}")


if __name__ == "__main__":
    main()
