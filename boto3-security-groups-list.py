import pprint
from boto3_helper import ec2_get_security_group_list

security_groups = ec2_get_security_group_list()
pprint.pprint(security_groups)