# CPP-Manager
This is the program I write that is basically a cpp console IDE. It can generate projects, classes, namespaces and more. It can also automatically build and run a project with one command and version controls.

The default output is at OUTPUT_PATH=~/cpp-workspace. It path can be found on line 6 of cpp-run.
You can change the default name at the top of files by changing 'username' on line 17 of bin/parse_new_files.py

Please note that the code for this project needs to be insainely refactor and I will be doing that over the next few days not that I have the generate code down for the project up to this point. After the refactor, I will work on the documentation generation.

# Usage

## Creating A Project

To create a project called test, run the following command:

```cpp-run create project <project name>```

* `<project name>` is the name of your project and default namespace.

The following command will generate a tree as follows:

```
cpp-run create project test

test
├── bin
├── build
│   └── test
│       ├── Debug
│       └── Release
├── doc
├── include
├── lib
│   └── compiled
└── src
    └── test
        ├── doc
        ├── include
        └── src
            └── Main.cpp
```

* 'bin' is where the final executable will go. Each executable will be 
	named by the namespace that you build it from.
* 'build' is where the CMake files, Makefiles, and object files are stored. 
	The build folder is sorted into 'namespace / build/release'
* 'doc' is where the project documentation is held. Currently the docs are 
	not generated, but will be added soon. It will be a compulation of each 
	namespace.
* 'include' and 'lib' are for over-arching files. 'include' is where 
	is for header files and 'lib' is for cpp files. Complied is where the 
	Makefile exports the compiled libraries too. The project does not currently
	natively support .a and .so files. They must be built during building.
* 'src' is where the project source is. The src is sorted by namespaces and
	the default namespace is the name of the project (in this case test). 
	Each namespace is sorted into 'include', for header files, 'src', for 
	.cpp files, and 'doc', for namespace documentation.

Sidenote:
For installing a library, you should do the following:

```
├── include
│   ├── test
│   └── Util
│       └── Print.h
├── lib
│   ├── compiled
│   └── Util
│       └── Print.cpp
```

To use the library, just add the following:

```
#include "lib/Util/Print.h"
```

The default output of Main.cpp is the following:

```C++

/**
	test::Main
	Main.cpp
	purpose: 

	@author Logan Rickert
	@version 0.0.0 07-21-2015 09:49:21
	@updated 07-21-2015 09:49:21
*/

#include <iostream>
#include <string>


using namespace std;

int main() {

	cout << "Hello World\n";

	return 0;

}
```

Documentation
* Line 1 is the namespace::Filename
* Line 2 is the filename
* Line 3 is the reason this file exists
* Line 4 is the author of the file
* Line 5 is the 'version number' 'date the file was created; %m-%d-%Y %H:%M:S'.
	Every time you build the project via cpp-run, the third zero will increment by 
	one. If you increment the other numbers or reset the third number to 0 or any other
	number, cpp-run will roll with it.
* Line 6 is the date and time the file was last compiled.
	* This actually no long works not that I think about it, lol.

* Line 8 is the only instance of using namespace std in any classes or namespaces as it
	is not recommended to be used. You can stop this from being added by editing 
	src/default_class.cpp.
