from conan import ConanFile


class Recipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps", "VirtualRunEnv"

    def layout(self):
        self.folders.generators = "conan"

    def requirements(self):
        self.requires("hedley/15")
        self.requires("json-c/0.17")

    def build_requirements(self):
        self.test_requires("catch2/2.13.10", options={"with_main": True})
