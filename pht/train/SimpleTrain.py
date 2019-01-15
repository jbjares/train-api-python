import abc
from pht.internal.describe.algorithm import AlgorithmRequirement


class SimpleTrain(abc.ABC):
    """
    Implements the Train API. For implementing a Train, you want to implement this class
    """
    def algorithm_requirements(self) -> AlgorithmRequirement:
        pass


    # def print_model_summary(self, run_info: StationRuntimeInfo) -> PrintModelSummaryResponse:
    #     """
    #     Executed when the print_model_summary command is executed.
    #     :param run_info:
    #     :return:
    #     """
    #     return PrintModelSummaryResponse(content=self.model_summary(run_info))
    #
    # @abc.abstractmethod
    # def run_algorithm(self, run_info: StationRuntimeInfo) -> RunAlgorithmResponse:
    #     pass
    #
    # def unmet_requirements(self):
    #     pass
    #
    # @abc.abstractmethod
    # def list_requirements(self, run_info: StationRuntimeInfo) -> ListRequirementsResponse:
    #     #  TODO
    #     pass
    #
    # @abc.abstractmethod
    # def model_summary(self, run_info: StationRuntimeInfo) -> str:
    #     pass
