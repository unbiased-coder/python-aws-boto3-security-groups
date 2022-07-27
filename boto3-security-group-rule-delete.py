import pprint
from boto3_helper import ec2_delete_security_group_rule

result = ec2_delete_security_group_rule('sg-0a4791007be830b56', 'sgr-02f2ba16855db024f')
pprint.pprint(result)
