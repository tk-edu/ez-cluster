// Standard Library
#include <iostream>
#include <format>

// MS-MPI
#include <mpi.h>

// Project
#include "typedefs.hpp"
#include "common.hpp"

// https://learn.microsoft.com/en-us/archive/blogs/windowshpc/how-to-compile-and-run-a-simple-ms-mpi-program
int main(int argc, char* argv[]) {
    MPI_Init(&argc, &argv);

    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 0) {
        String hello = "Hello, World";
        /* If a function asks for a "const char*" instead of a String,
        call `.c_str()` on the String you're trying to pass */
        MPI_Send(hello.c_str(), hello.size(), MPI_CHAR, 1, 0, MPI_COMM_WORLD);
    }
    else if (rank == 1) {
        // Normal strings are literally character arrays in C/C++
        char received_string[13]; // 12 + NULL terminator (Strings have to end with a NULL element)
        MPI_Recv(received_string, sizeof(received_string)/sizeof(received_string[0]), MPI_CHAR, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        DEBUG(std::format("Rank 1 received string {} from Rank 0", received_string))
    }

    MPI_Finalize();
}