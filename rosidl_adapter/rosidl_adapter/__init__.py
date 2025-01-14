# Copyright 2018 Open Source Robotics Foundation, Inc.
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

from pathlib import Path


def convert_to_idl(package_dir: Path, package_name: str, interface_file: Path,
                   output_dir: Path) -> Path:
    if interface_file.suffix == '.msg':
        from rosidl_adapter.msg import convert_msg_to_idl
        return convert_msg_to_idl(
            package_dir, package_name, interface_file, output_dir / 'msg')

    if interface_file.suffix == '.srv':
        from rosidl_adapter.srv import convert_srv_to_idl
        return convert_srv_to_idl(
            package_dir, package_name, interface_file, output_dir / 'srv')

    if interface_file.suffix == '.action':
        from rosidl_adapter.action import convert_action_to_idl
        return convert_action_to_idl(
            package_dir, package_name, interface_file, output_dir / 'action')

    assert False, f"Unsupported interface type '{interface_file.suffix}'"
