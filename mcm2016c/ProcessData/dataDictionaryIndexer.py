from enum import Enum, unique
# , IntEnum
try:
    @unique
    class dataDictionaryIndexer(Enum):
        NODE = 0
        devCategory = 1
        developerFriendlyName = 2
        APIDataType = 3
        VARIABLENAME = 4
        VALUE = 5
        LABEL = 6
        SOURCE = 7
        NOTES = 8


except ValueError as e:
    print(e)
