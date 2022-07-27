import pprint
from boto3_helper import ec2_add_security_group_rule

result = ec2_add_security_group_rule('sg-0a4791007be830b56', 'tcp', 9000, 9001, '0.0.0.0/0')
pprint.pprint(result)
