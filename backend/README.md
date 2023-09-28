# well made backend
System for distributing and executing tasks in an HPC cluster
## **About C++ Codebases**
### **Header files**
In C and C++, "header files" are used in codebases that split source code across multiple files. They are where you can declare functions, classes, variables, etc. that can be accessed from any file that `#include`s them. Classes are typically *declared* in header files (files in `include/` with the `.hpp` extension), and *defined* in source files (files in `src/` with the `.cpp` extension). You'll get a compiler error if you define something in a header file in more than one source file, though, so be careful! Also, header files should always start with `#pragma once`.

<u>Note:</u> You'll see header file names surrounded with `<>` or `""`. The only difference between these two delimiters is that `<>` is used for standard library headers and 3rd party library headers, while `""` is used for headers that are a part of this project. At least, that's how it is in this codebase! :)
s
### **Why did I just get an error message that took up the entirety of the terminal???**
C++ compilers are just like that 😐. Half the time you've unknowingly broken some fundamental rule of the language, and the other half you forgot a semicolon.

## **Building**
On Windows, you'll need [w64devkit](https://github.com/skeeto/w64devkit/releases/download/v1.20.0/w64devkit-1.20.0.zip). Once you've downloaded it, run `w64devkit.exe`. This shell will have the tools needed to build the project.  

You also need to install the MSMPI Runtime and SDK from [this website](https://www.microsoft.com/en-us/download/details.aspx?id=105289).

Here are the build steps once you're in the shell:
- Open `Makefile` and change `MSMPI_PATH` at the top of the file to the root directory of wherever you installed the MS-MPI SDK
- Go to the project's root directory (not `src/`, `include/`, or `bin/`)
- Run `make`

That's it! You can then run the executable created in `bin/`.  
If you run into issues, well... tell me.

## **VSCode Suggestions**
If you want VSCode autocomplete for MPI library stuff, then change the commented paths in `c_cpp_properties.json` to the appropriate ones on your system.