class SynchDataNamesUseCase:

    def execute(self, selected_objects):
        if len(selected_objects) == 0:
            return {"CANCELLED"}
        for object in selected_objects:
            object.data.name = object.name
        return {"FINISHED"}
