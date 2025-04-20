from typing import Collection, Dict, Optional, Set, Type, TypeVar, Union
from java.io import File, IOException, InputStream
from java.lang import Class, ClassLoader, Constructor, IllegalAccessException, IllegalArgumentException, InstantiationException, NoSuchMethodException, SecurityException
from java.lang.reflect import InvocationTargetException
from java.net import MalformedURLException, URL, URLClassLoader
from java.security import CodeSigner, CodeSource
from java.util import Collection, ConcurrentHashMap, Enumeration, Map, Set
from java.util.jar import JarEntry, JarFile, Manifest
from java.util.logging import Level
from org.bukkit.plugin import InvalidPluginException, PluginDescriptionFile, SimplePluginManager
from org.jetbrains.annotations import NotNull, Nullable

JavaPlugin = TypeVar('JavaPlugin')

class PluginClassLoader(URLClassLoader):
    """
    A ClassLoader for plugins, to allow shared classes across multiple plugins
    """

    def __init__(self, loader: JavaPluginLoader, parent: Optional[ClassLoader], description: PluginDescriptionFile, dataFolder: File, file: File, libraryLoader: Optional[ClassLoader]) -> None:
        ...

    def getResource(self, name: str) -> Optional[URL]:
        ...

    def getResources(self, name: str) -> Enumeration[URL]:
        ...

    def loadClass(self, name: str, resolve: bool) -> Type:
        ...

    def loadClass0(self, name: str, resolve: bool, checkGlobal: bool, checkLibraries: bool) -> Type:
        ...

    def findClass(self, name: str) -> Type:
        ...

    def close(self) -> None:
        ...

        def getClasses(self) -> Collection[Type]:
        ...

    def initialize(self, javaPlugin: JavaPlugin) -> None:
        ...