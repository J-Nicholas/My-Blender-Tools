import pytest
from my_addon.core.name_synch.name_synch_usecase import SynchDataNamesUseCase


class TestNameSyncher:
    use_case = SynchDataNamesUseCase()

    def test_nothing_selected_when_executed_then_cancelled(self):
        empty = []
        result = self.use_case.execute(empty)
        assert result == {"CANCELLED"}

    def test_no_data_when_executed_then_cancelled(self):
        no_data = [{"name": "some name"}]
        result = self.use_case.execute(no_data)
        assert result == {
            "CANCELLED"
        }, "result should be cancelled if the object has a name but no data"
