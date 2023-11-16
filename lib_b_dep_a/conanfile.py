from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout

class LibBDepAConan(ConanFile):
    name = "lib_b_dep_a"
    version = "1.0"

    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps", "CMakeToolchain"
    exports_sources = "CMakeLists.txt", "*.cpp", "*.h"

    def requirements(self):
        self.requires("lib_a_nodeps/1.0")

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

