from aws_cdk import core # type: ignore
from aws_cdk import aws_dynamodb as dynamodb # type: ignore

class FlightDataStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create DynamoDB table
        table = dynamodb.Table(
            self, "FlightsTable",
            partition_key=dynamodb.Attribute(name="flight_id", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )
