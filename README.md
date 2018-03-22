# arcpyloader
Loads the correct arcgisscripting DLL for ArcPy to function when relaunched from within another Python scripts.

---

Under certain circumstances, the use of the Python multiprocessing module in combination with ArcPy from ArcGIS Desktop will result in Python attempting to load the wrong version of the ArcPy DLL. For example, it will attempt to load the x86 DLL while running Python in x64.

In this circumstance, use the provided *arcpyloader.py* file instead of loading ArcPy directly.

## Use
Place the *arcpyloader.py* file in the same directory as your code and use the following code to import ArcPy:
```python
from	arcpyloader	import arcpy
``` 


## Licensing

Copyright 2018 Esri Canada - All Rights Reserved

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

A copy of the license is available in the repository's [LICENSE](../master/LICENSE) file.

## Support

This code is distributed as is and is not supported by Esri Canada, Esri Inc. or any other Esri distributor.