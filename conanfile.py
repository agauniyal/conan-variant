from conans import ConanFile, tools

class VariantConan(ConanFile):
    name = "variant"
    version = "1.2.2"
    license = "BSL 1.0"
    url = "https://github.com/mpark/variant"
    description = "C++17 std::variant for C++11/14/17 https://mpark.github.io/variant"

    def source(self):
        self.run("git clone https://github.com/mpark/variant.git")
        self.run("cd variant && git checkout single-header")

    def package(self):
        self.copy(pattern="*.hpp", src="variant/v1.2.2", dst="include", keep_path=False)
