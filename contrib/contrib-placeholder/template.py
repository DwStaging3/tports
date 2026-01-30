pkgname = "contrib-placeholder"
pkgver = "4.20.69"
pkgrel = 0
build_style = "meta"
# prevent installation
depends = ["virtual:meta:do-not-use!base-files"]
pkgdesc = "Contrib repository placeholder, do not install"
maintainer = "Reaver"
license = "custom:meta"
url = "tartarus placeholder"


@subpackage("contrib-placeholder-dbg")
def _(self):
    self.depends = ["virtual:meta:do-not-use!base-files"]
    return []
