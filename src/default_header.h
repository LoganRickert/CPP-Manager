
/**
	{{project_name}}
	{{class_name}}.h
	purpose: 

	@author Logan Rickert
	@version 0.0.0 {{date}}
*/

#include <iostream>
#include <string>

using namespace std;

#ifndef {{class_name_caps}}_H
#define {{class_name_caps}}_H

class {{class_name}} {

	public:
		{{class_name}}();
		{{class_construct_full}}

		~{{class_name}}();

{{getters_setters}}
	private:
{{class_fields}}
};

#endif
