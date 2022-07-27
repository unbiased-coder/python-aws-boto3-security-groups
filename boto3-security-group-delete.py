import pprint
from boto3_helper import ec2_delete_security_group

result = ec2_delete_security_group('sg-0148ad8f0314a586b')
pprint.pprint(result)
