import os
import logging
from datetime import timedelta, datetime, timezone

import bytewax.operators as op
from bytewax.dataflow import Dataflow
from bytewax.testing import TestingSource
from bytewax.influxdb import InfluxDBSource

TOKEN = os.getenv(
    "INLFUXDB_TOKEN",
    "x06p8_fojSJwNXIDq7xia1aiRjtlSdnHy_v0OrU8XmF-qRmusemIjzzhpjrwtdcem1O20vK7kFBe7G9kXrzHkw==",
)
DATABASE = os.getenv("INFLUXDB_DATABASE", "testing")
ORG = os.getenv("INFLUXDB_ORG", "dev")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

flow = Dataflow("a_simple_example")

inp = op.input(
    "inp",
    flow,
    InfluxDBSource(
        timedelta(seconds=5),
        "https://us-east-1-1.aws.cloud2.influxdata.com",
        DATABASE,
        TOKEN,
        "home",
        ORG,
        datetime.now(timezone.utc) - timedelta(days=5),
    ),
)
op.inspect("input", inp)
