CXX = g++
S = src\\
I = include\\
B = bin\\
# Change this to your path!
MSMPI_PATH = D:\MSMPI-SDK\\

# TODO: auto-find MSMPI SDK path?
FLAGS = -I$(I) -I$(MSMPI_PATH)Include -I$(MSMPI_PATH)Include\x64 -L$(MSMPI_PATH)Lib\x64 -lmsmpi -std=c++20

OBJ_FILES = $(B)main.o

$(B)backend.exe: $(OBJ_FILES)
	$(CXX) $^ -o $@ $(FLAGS)

$(B)main.o: $(S)main.cpp
	$(CXX) -c $< -o $@ $(FLAGS)

exe: $(B)backend.exe
	-del $(OBJ_FILES)

debug: FLAGS += -g
debug: $(B)backend.exe

optimized: FLAGS += -O3
optimized: $(B)backend.exe

clean:
	-del $(B)backend.exe $(OBJ_FILES)