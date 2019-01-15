import abc
from pht.internal import TrainDescription


class AbstractTrain(abc.ABC):

    @abc.abstractmethod
    def describe(self) -> TrainDescription:
        pass


class SimpleTrain(AbstractTrain):

    def requirements(self):
        pass
