#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

from typing import Tuple

from .._models import HttpResponse
from ..client_utils import DEFAULT
from ._base import BaseNode


class BaseAsyncNode(BaseNode):
    """Base class for Async HTTP node implementations"""

    async def perform_request(
        self,
        method,
        target,
        body=None,
        request_timeout=DEFAULT,
        ignore_status=(),
        headers=None,
    ) -> Tuple[HttpResponse, bytes]:  # pragma: nocover
        raise NotImplementedError()

    async def close(self):  # pragma: nocover
        raise NotImplementedError()