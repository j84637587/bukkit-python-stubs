from typing import Optional

from org.bukkit import World
from org.bukkit.command import CommandSender
from org.bukkit.generator import BiomeProvider, ChunkGenerator
from org.bukkit.plugin import Plugin
from org.bukkit import WorldType


class WorldCreator:
    """
    Represents various types of options that may be used to create a world.
    """

    def __init__(self, name: str) -> None:
        """
        Creates an empty WorldCreationOptions for the given world name

        :param name: Name of the world that will be created
        """
        ...

    def copy(self, world: World) -> 'WorldCreator':
        """
        Copies the options from the specified world

        :param world: World to copy options from
        :return: This object, for chaining
        """
        ...

    def copy(self, creator: 'WorldCreator') -> 'WorldCreator':
        """
        Copies the options from the specified WorldCreator

        :param creator: World creator to copy options from
        :return: This object, for chaining
        """
        ...

    def name(self) -> str:
        """
        Gets the name of the world that is to be loaded or created.

        :return: World name
        """
        ...

    def seed(self) -> int:
        """
        Gets the seed that will be used to create this world

        :return: World seed
        """
        ...

    def seed(self, seed: int) -> 'WorldCreator':
        """
        Sets the seed that will be used to create this world

        :param seed: World seed
        :return: This object, for chaining
        """
        ...

    def environment(self) -> World.Environment:
        """
        Gets the environment that will be used to create or load the world

        :return: World environment
        """
        ...

    def environment(self, env: World.Environment) -> 'WorldCreator':
        """
        Sets the environment that will be used to create or load the world

        :param env: World environment
        :return: This object, for chaining
        """
        ...

    def type(self) -> WorldType:
        """
        Gets the type of the world that will be created or loaded

        :return: World type
        """
        ...

    def type(self, type: WorldType) -> 'WorldCreator':
        """
        Sets the type of the world that will be created or loaded

        :param type: World type
        :return: This object, for chaining
        """
        ...

    def generator(self) -> Optional[ChunkGenerator]:
        """
        Gets the generator that will be used to create or load the world.

        :return: Chunk generator
        """
        ...

    def generator(self, generator: Optional[ChunkGenerator]) -> 'WorldCreator':
        """
        Sets the generator that will be used to create or load the world.

        :param generator: Chunk generator
        :return: This object, for chaining
        """
        ...

    def generator(self, generator: Optional[str]) -> 'WorldCreator':
        """
        Sets the generator that will be used to create or load the world.

        :param generator: Name of the generator to use, in "plugin:id" notation
        :return: This object, for chaining
        """
        ...

    def generator(self, generator: Optional[str], output: Optional[CommandSender]) -> 'WorldCreator':
        """
        Sets the generator that will be used to create or load the world.

        :param generator: Name of the generator to use, in "plugin:id" notation
        :param output: CommandSender that will receive any error messages
        :return: This object, for chaining
        """
        ...

    def biomeProvider(self) -> Optional[BiomeProvider]:
        """
        Gets the biome provider that will be used to create or load the world.

        :return: Biome provider
        """
        ...

    def biomeProvider(self, biomeProvider: Optional[BiomeProvider]) -> 'WorldCreator':
        """
        Sets the biome provider that will be used to create or load the world.

        :param biomeProvider: Biome provider
        :return: This object, for chaining
        """
        ...

    def biomeProvider(self, biomeProvider: Optional[str]) -> 'WorldCreator':
        """
        Sets the biome provider that will be used to create or load the world.

        :param biomeProvider: Name of the biome provider to use, in "plugin:id" notation
        :return: This object, for chaining
        """
        ...

    def biomeProvider(self, biomeProvider: Optional[str], output: Optional[CommandSender]) -> 'WorldCreator':
        """
        Sets the biome provider that will be used to create or load the world.

        :param biomeProvider: Name of the biome provider to use, in "plugin:id" notation
        :param output: CommandSender that will receive any error messages
        :return: This object, for chaining
        """
        ...

    def generatorSettings(self, generatorSettings: str) -> 'WorldCreator':
        """
        Sets the generator settings of the world that will be created or loaded.

        :param generatorSettings: The settings that should be used by the generator
        :return: This object, for chaining
        """
        ...

    def generatorSettings(self) -> str:
        """
        Gets the generator settings of the world that will be created or loaded.

        :return: The settings that should be used by the generator
        """
        ...

    def generateStructures(self, generate: bool) -> 'WorldCreator':
        """
        Sets whether or not worlds created or loaded with this creator will have structures.

        :param generate: Whether to generate structures
        :return: This object, for chaining
        """
        ...

    def generateStructures(self) -> bool:
        """
        Gets whether or not structures will be generated in the world.

        :return: True if structures will be generated
        """
        ...

    def hardcore(self, hardcore: bool) -> 'WorldCreator':
        """
        Sets whether the world will be hardcore or not.

        :param hardcore: Whether the world will be hardcore
        :return: This object, for chaining
        """
        ...

    def hardcore(self) -> bool:
        """
        Gets whether the world will be hardcore or not.

        :return: hardcore status
        """
        ...

    def keepSpawnInMemory(self, keepSpawnInMemory: bool) -> 'WorldCreator':
        """
        Sets whether the spawn chunks will be kept loaded.

        :param keepSpawnInMemory: Whether the spawn chunks will be kept loaded
        :return: This object, for chaining
        """
        ...

    def keepSpawnInMemory(self) -> bool:
        """
        Gets whether or not the spawn chunks will be kept loaded.

        :return: True if the spawn chunks will be kept loaded
        """
        ...

    def createWorld(self) -> Optional[World]:
        """
        Creates a world with the specified options.

        :return: Newly created or loaded world
        """
        ...

    @staticmethod
    def name(name: str) -> 'WorldCreator':
        """
        Creates a new WorldCreator for the given world name

        :param name: Name of the world to load or create
        :return: Resulting WorldCreator
        """
        ...

    @staticmethod
    def getGeneratorForName(world: str, name: Optional[str], output: Optional[CommandSender]) -> Optional[ChunkGenerator]:
        """
        Attempts to get the ChunkGenerator with the given name.

        :param world: Name of the world this will be used for
        :param name: Name of the generator to retrieve
        :param output: Where to output if errors are present
        :return: Resulting generator, or null
        """
        ...

    @staticmethod
    def getBiomeProviderForName(world: str, name: Optional[str], output: Optional[CommandSender]) -> Optional[BiomeProvider]:
        """
        Attempts to get the BiomeProvider with the given name.

        :param world: Name of the world this will be used for
        :param name: Name of the biome provider to retrieve
        :param output: Where to output if errors are present
        :return: Resulting biome provider, or null
        """
        ...