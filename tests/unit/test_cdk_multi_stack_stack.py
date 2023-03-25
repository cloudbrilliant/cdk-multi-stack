import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_multi_stack.cdk_multi_stack_stack import CdkMultiStackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_multi_stack/cdk_multi_stack_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkMultiStackStack(app, "cdk-multi-stack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
