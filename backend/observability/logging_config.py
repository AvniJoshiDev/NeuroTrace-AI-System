import logging
import json


class JSONFormatter(logging.Formatter):

    def format(self, record):

        return json.dumps(
            {
                "level": record.levelname,
                "message": record.getMessage()
            }
        )


logger = logging.getLogger(
    "neurotrace"
)


handler = logging.StreamHandler()

handler.setFormatter(
    JSONFormatter()
)


logger.addHandler(handler)

logger.setLevel(
    logging.INFO
)
