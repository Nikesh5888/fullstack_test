#!/usr/bin/env python3

from aws_cdk import core
from cdk.cdk_stack import FlightDataStack

app = core.App()
FlightDataStack(app, "FlightDataStack")
app.synth()