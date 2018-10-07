import json
import os

class constructor:
    # Create the file config
    def options_txt():
        options = {}
        options["Width"] = 1600
        options["Height"] = 900
        options["Volume"] = 4

        data = json.dumps(options)
        with open("Assets\Data\Options.txt", "w") as file:
            file.write(data)

constructor.options_txt()
