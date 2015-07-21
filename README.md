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
	The build folder is sorted into 'namespace / Debug/Release'
* 'doc' is where the project documentation is held. Currently the doc generation is
	not implemented, but will be added soon. It will be a compulation of each 
	namespace.
* 'include' and 'lib' are for over-arching files. 'include' is where 
	is header files go and 'lib' is for cpp files. Complied is where the 
	Makefile exports the compiled libraries too. The project does not currently
	natively support .a and .so files. They must be built during building and are 
	put in the lib/compiled to be reused instead of rebuilt on building.
* 'src' is where the project source is. The src is sorted by namespaces and
	the default namespace is the name of the project (in this case test). 
	Each namespace is sorted into 'include', for header files, 'src', for 
	.cpp files, and 'doc', for namespace documentation.

upon creating a project, it will also init a git. It will also add all files 
directories and commit them with 'Initial project setup.'

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
	one. If you increment the other numbers or reset the third number to 0, cpp-run will roll with it.
* Line 6 is the date and time the file was last compiled.
	* This actually and line 5 no long works not that I think about it, lol.

* Line 8 is the only instance of using namespace std in any classes or namespaces as it
	is not recommended to be used. You can stop this from being added by editing 
	src/default_class.cpp.

## Creating A Class

To create a class, do the following:

```
cpp-run create class <project name> <namespace> <class name> [class members]
```

* `<project name>` is the name of the project.
* `<namespace>` is the name of the namespace inside of the project. If the namespace
	and project name are the same, you can sub this with a period.
* `<class name>` is the name of the class.
* `[class members]` are members you want cpp-run to automatically add. It will generate 
	getters and setters and a contructor([class members]) automatically.

The following are two examples, one with no [class members] arg, and one with one.

```
cpp-run create class test test Person

tree test/src/test
├── doc
├── include
│   └── Person.h
└── src
    ├── Main.cpp
    └── Person.cpp
```

```C++

/**
	test::Person
	Person.cpp
	purpose: 

	@author Logan Rickert
	@version 0.0.0 07-21-2015 10:24:28
	@updated 07-21-2015 10:24:28
*/

#include "test/include/Person.h"

Person::Person() {

}

Person::~Person() {

}
```

```C++

/**
	test::Person
	Person.h
	purpose: 

	@author Logan Rickert
	@version 0.0.0 07-21-2015 10:24:28
	@updated 07-21-2015 10:24:28
*/

#include <iostream>
#include <string>

#ifndef PERSON_H
#define PERSON_H

class Person {

	public:
		Person();

		~Person();

	private:

};

#endif
```

`#include "test/include/Person.h"` is automatically added to Main.cpp below `#include <string>`. If there are 
no library calls and two new lines below them, it won't actually work.

```
cpp-run create class test . Student std::string name int age double gpa

tree test/src/test
├── doc
├── include
│   ├── Person.h
│   └── Student.h
└── src
    ├── Main.cpp
    ├── Person.cpp
    └── Student.cpp
```

```C++

/**
	test::Student
	Student.h
	purpose: 

	@author Logan Rickert
	@version 0.0.0 07-21-2015 10:30:26
	@updated 07-21-2015 10:30:26
*/

#include <iostream>
#include <string>

#ifndef STUDENT_H
#define STUDENT_H

class Student {

	public:
		Student();
		Student(std::string, int, double);

		~Student();

		std::string getName();
		int getAge();
		double getGpa();

		void setName(std::string sName);
		void setAge(int sAge);
		void setGpa(double sGpa);

	private:
		std::string name;
		int age;
		double gpa;

};

#endif
```

```C++

/**
	test::Student
	Student.cpp
	purpose: 

	@author Logan Rickert
	@version 0.0.0 07-21-2015 10:30:26
	@updated 07-21-2015 10:30:26
*/

#include "test/include/Student.h"

Student::Student() {

}

Student::Student(std::string sName, int sAge, double sGpa) {
	name = sName;
	age = sAge;
	gpa = sGpa;
}

Student::~Student() {

}

std::string Student::getName() {
	return name;
}

void Student::setName(std::string sName) {
	name = sName;
}

int Student::getAge() {
	return age;
}

void Student::setAge(int sAge) {
	age = sAge;
}

double Student::getGpa() {
	return gpa;
}

void Student::setGpa(double sGpa) {
	gpa = sGpa;
}
```

After each new class generation, cpp-run automatically git add classname.cpp and classname.h 
and commits with the message: 'Added '$CLASS_NAME' cpp and h to '$namespace' namespace.'

## Building

To build your namespace, do the following:

```cpp-run build <project name> <namespace> [Default:Debug/Release] [No git commit]```
* `<project name>` is the name of the project
* `<namespace>` is the name of the namespace you want to build. If the namespace is 
	the same as the project name, you can sub it for a peroid.
* `[Default:Debug/Release]` is whether or not you want to build the namespace in
	debug or release. No argument means it will build in Debug.
* `[No git commit]` means if this argument is present, it will not run `git add .` `git commit -a`.

An example:

```
cpp-run build test . Debug

Added a util print function and #include "*.h"s to Main.
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
#       new file:   include/Util/Print.h
#       new file:   lib/Util/Print.cpp
#       modified:   src/test/src/Main.cpp
#

Hello World
```

Our new tree for bin and build looks like this:

```
test
├── bin
│   ├── old
│   └── test
├── build
│   └── test
│       ├── Debug
│       │   ├── CMakeCache.txt
│       │   ├── CMakeFiles
│       │   │   ├── 2.8.12.2
│       │   │   │   ├── CMakeCCompiler.cmake
│       │   │   │   ├── CMakeCXXCompiler.cmake
│       │   │   │   ├── CMakeDetermineCompilerABI_C.bin
│       │   │   │   ├── CMakeDetermineCompilerABI_CXX.bin
│       │   │   │   ├── CMakeSystem.cmake
│       │   │   │   ├── CompilerIdC
│       │   │   │   │   ├── a.out
│       │   │   │   │   └── CMakeCCompilerId.c
│       │   │   │   └── CompilerIdCXX
│       │   │   │       ├── a.out
│       │   │   │       └── CMakeCXXCompilerId.cpp
│       │   │   ├── cmake.check_cache
│       │   │   ├── CMakeDirectoryInformation.cmake
│       │   │   ├── CMakeOutput.log
│       │   │   ├── CMakeTmp
│       │   │   ├── Makefile2
│       │   │   ├── Makefile.cmake
│       │   │   ├── progress.marks
│       │   │   ├── TargetDirectories.txt
│       │   │   └── test.dir
│       │   │       ├── build.make
│       │   │       ├── cmake_clean.cmake
│       │   │       ├── CXX.includecache
│       │   │       ├── DependInfo.cmake
│       │   │       ├── depend.internal
│       │   │       ├── depend.make
│       │   │       ├── flags.make
│       │   │       ├── home
│       │   │       │   └── logan
│       │   │       │       └── cpp-workspace
│       │   │       │           └── test
│       │   │       │               └── src
│       │   │       │                   └── test
│       │   │       │                       └── src
│       │   │       │                           ├── Main.cpp.o
│       │   │       │                           ├── Person.cpp.o
│       │   │       │                           └── Student.cpp.o
│       │   │       ├── link.txt
│       │   │       └── progress.make
│       │   ├── cmake_install.cmake
│       │   ├── CMakeLists.txt
│       │   └── Makefile
│       └── Release
```

When you run `cpp-run build`, it generates a CMake file in the build/namespace/Debug directory.
It then runs the CMake file by running 'cmake -G "Unix Makefiles"'. The command will generate a
Makefile in the Debug folder and cpp-run then runs 'make'. Once it's done, it runs 'git add .' and 
'git commit -a'. You can enter in a commit message and it will then run the new program.

You can view the new program at bin/namespace.

## Creating A New Namespace

Creating a new namespace is super easy, just run:

```
cpp-run create namespace <project name> <namespace>
```

* `<project name>` is the name of the project.
* `<namespace>` is the name of the namespace.

Your tree of src should now look like this:

```
tree test/src/
├── test
│   ├── doc
│   ├── include
│   │   ├── Person.h
│   │   └── Student.h
│   └── src
│       ├── Main.cpp
│       ├── Person.cpp
│       └── Student.cpp
└── testOther
    ├── doc
    ├── include
    └── src
        └── Main.cpp
```

On running the command, cpp-run will git add src/$namespace and commit with
the following: 'Added '$namespace' namespace and initial Main.cpp.'.

The following is the CMake file that was generated for test. (I'm still new to 
CMake so I'm sure you could optimize it by a lot.)

(The )
```
cmake_minimum_required(VERSION 2.8)

project("test")

include_directories("/home/logan/cpp-workspace/test/src")
include_directories("/home/logan/cpp-workspace/test/include")

add_executable("test"
	"/home/logan/cpp-workspace/test/src/test/src/Person.cpp"
	"/home/logan/cpp-workspace/test/src/test/src/Student.cpp"
	"/home/logan/cpp-workspace/test/src/test/src/Main.cpp"
)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY /home/logan/cpp-workspace/test/lib/compiled)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY /home/logan/cpp-workspace/test/lib/compiled)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY /home/logan/cpp-workspace/test/bin)

set_target_properties("test"
	PROPERTIES
	ARCHIVE_OUTPUT_DIRECTORY "/home/logan/cpp-workspace/test/lib/compiled"
	LIBRARY_OUTPUT_DIRECTORY "/home/logan/cpp-workspace/test/lib/compiled"
	RUNTIME_OUTPUT_DIRECTORY "/home/logan/cpp-workspace/test/bin"
)
```

## Libraries

File: `/test/src/test/src/Main.cpp`

```C++
#include <iostream>
#include <string>

#include "test/include/Student.h"
#include "test/include/Person.h"
#include "include/Util/Print.h"
```

File: `/test/include/Util/Print.h`

```C++

/**
	test::Print
	Print.h
	purpose: 

	@author Logan Rickert
	@version 0.0.0 07-21-2015 10:24:28
	@updated 07-21-2015 10:24:28
*/

#include <iostream>
#include <string>

#ifndef PRINT_H
#define PRINT_H

class Print {

	public:
		Print();

		~Print();

	private:

};

#endif
```

File: `/test/lib/Util/Print.h`

```C++

/**
	test::Print
	Print.cpp
	purpose: 

	@author Logan Rickert
	@version 0.0.0 07-21-2015 10:24:28
	@updated 07-21-2015 10:24:28
*/

#include "include/Util/Print.h"

Print::Print() {

}

Print::~Print() {

}
```

tree of lib and include:

```
├── include
│   └── Util
│       └── Print.h
├── lib
│   ├── compiled
│   └── Util
│       └── Print.cpp
```

Now lets build like normal:

```
cpp-run build test . Debug .
```

tree of lib and include:

```
├── include
│   └── Util
│       └── Print.h
├── lib
│   ├── compiled
│   │   └── lib.Util.Print.a
│   └── Util
│       └── Print.cpp
```

## Final Git Log:

```
commit 53e20e9bd19a10c30bdb98796a2504046fcea637
Author: Logan Rickert <myemail>
Date:   Tue Jul 21 10:53:42 2015 -0400

    Added 'testOther' namespace and initial Main.cpp.

commit 48396f4cdfa24bda8a3059409c49d9c17e36b8a3
Author: Logan Rickert <myemail>
Date:   Tue Jul 21 10:45:17 2015 -0400

    Added a util print function and #include "*.h"s to Main.

commit 6f467fb0aebbe3351e2b85e5ff17baa46fd9d97d
Author: Logan Rickert <myemail>
Date:   Tue Jul 21 10:30:26 2015 -0400

    Added 'Student' cpp and h to 'test' namespace.

commit 293d1f5038e68b2b4dde4f7870a0286f684c9c2e
Author: Logan Rickert <myemail>
Date:   Tue Jul 21 10:24:28 2015 -0400

    Added 'Person' cpp and h to 'test' namespace.

commit 634bbc170f57a0602006fd9d2c9ac6be31a98c2e
Author: Logan Rickert <myemail>
Date:   Tue Jul 21 09:49:21 2015 -0400

    Initial project setup.
```

A pretty nice log if I do say so myself for only actually
writing one commit message.

## Future Features

* Fix @updated and @version to work again
* Don't run ./namespace is CMake and make fails.
* Autogenerate docs
* On building of file, it organizes class files (Not Main) functions alphabetically.
* On building of file, it organizes #include <> and #include "" alphabetically. 
