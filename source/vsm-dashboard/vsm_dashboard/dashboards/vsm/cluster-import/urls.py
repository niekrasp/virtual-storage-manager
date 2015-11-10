
# Copyright 2014 Intel Corporation, All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the"License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.

from django.conf.urls import patterns, url
from .views import IndexView
from .views import ImportClusterView
<<<<<<< HEAD
from .views import import_cluster,check_cluster_tobe_import
=======
from .views import import_cluster
>>>>>>> 308e6e1b30f56636211c70add3c002e16f34d6c1

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^importcluster/$', ImportClusterView.as_view(), name='importcluster'),
    url(r'^import_cluster/$', import_cluster, name='import_cluster'),
<<<<<<< HEAD
    url(r'^check_cluster_tobe_import/$', check_cluster_tobe_import, name='check_cluster_tobe_import'),
=======
>>>>>>> 308e6e1b30f56636211c70add3c002e16f34d6c1
)