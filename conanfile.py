from conans import ConanFile, CMake


class DenaAppConan(ConanFile):
    name = "dena_app"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_find_package"

    def build_requirements(self):
        self.build_requires("cmake/3.19.6@")

    def requirements(self):
        self.requires("dena_library/0.1@dena/testing")

    def export_sources(self):
        self.copy("*")

    def _configure_cmake(self):
        cmake = CMake(self)
        #cmake.definitions["SOME_DEFINITION"] = "VALUE"
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        #self.cpp_info.includedirs = ['include']  # Ordered list of include paths
        #self.cpp_info.libs = ['dena_library']  # The libs to link against
        #self.cpp_info.system_libs = []  # System libs to link against
        #self.cpp_info.libdirs = ['lib']  # Directories where libraries can be found
        #self.cpp_info.resdirs = ['res']  # Directories where resources, data, etc. can be found
        self.cpp_info.bindirs = ['bin']  # Directories where executables and shared libs can be found
        #self.cpp_info.srcdirs = []  # Directories where sources can be found (debugging, reusing sources)
        #self.cpp_info.build_modules = {}  # Build system utility module files
        #self.cpp_info.defines = []  # preprocessor definitions
        #self.cpp_info.cflags = []  # pure C flags
        #self.cpp_info.cxxflags = []  # C++ compilation flags
        #self.cpp_info.sharedlinkflags = []  # linker flags
        #self.cpp_info.exelinkflags = []  # linker flags
        #self.cpp_info.components  # Dictionary with the different components a package may have
        #self.cpp_info.requires = None  # List of components from requirements
