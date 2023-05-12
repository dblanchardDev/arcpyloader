# arcpyloader
Loads the correct arcgisscripting DLL for ArcPy to function when relaunched from within another Python scripts.

> 🛑 **Deprecated**  
> The arcpyloader was written for ArcMap which is now nearing end of life. Consider using ArcGIS Pro instead, which does not need this tool as it is entriely 64-bit.

---

Under certain circumstances, importing ArcPy while using Python multiprocessing will result in an error like:
```
DLL load failed: %1 is not a valid Win32 application.
```

This is caused by the sub-process attempting to load the wrong version of the arcgisscripting DLL (e.g. loading the x86 version in a x64 environment).

This mainly occurs in ArcGIS Desktop with background processing installed.

The *arcpyloader* file will adjust paths before loading ArcPy ensuring that the correct version of ArcPy is loaded.

## Use
Place the *arcpyloader.py* file in the same directory as your code and use the following code to import ArcPy:
```python
from  arcpyloader  import arcpy
``` 


## Licensing

Copyright 2018 Esri Canada - All Rights Reserved

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

A copy of the license is available in the repository's [LICENSE](../master/LICENSE) file.

## Support

This code is distributed as is and is not supported by Esri Canada, Esri Inc. or any other Esri distributor.
