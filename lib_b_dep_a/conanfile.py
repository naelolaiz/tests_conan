from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps

class LibBDepAConan(ConanFile):
    name = "lib_b_dep_a"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"

    def requirements(self):
        self.requires("lib_a_nodeps/1.0")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src=".")
        self.copy("*lib_b_dep_a.lib", dst="lib", keep_path=False)
        self.copy("*lib_b_dep_a.so", dst="lib", keep_path=False)
        self.copy("*lib_b_dep_a.dylib", dst="lib", keep_path=False)
        self.copy("*lib_b_dep_a.a", dst="lib", keep_path=False)

