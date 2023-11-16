from conan import ConanFile
from conan.tools.cmake import CMake

class AppDepBConan(ConanFile):
    name = "app_dep_b"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    exports_sources = "CMakeLists.txt", "*.cpp"

    def requirements(self):
        self.requires("lib_b_dep_a/1.0")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.exe", dst="bin", keep_path=False)

