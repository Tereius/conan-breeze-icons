import os
from conans import ConanFile, CMake, tools

class BreezeIconsConan(ConanFile):
    name = "breeze-icons"
    license = ("LGPLv3")
    url = "https://github.com/Tereius/conan-breeze-icons"
    homepage = "https://invent.kde.org/frameworks/breeze-icons/-/tree/master"
    topics = ("conan", "cmake", "kde")
    description = "KDE's breeze icons"

    def source(self):
        tools.get("https://invent.kde.org/frameworks/breeze-icons/-/archive/v%s/breeze-icons-v%s.zip" % (self.version, self.version))

    def package(self):
        self.copy("*", src="breeze-icons-v%s" % self.version)
