
# AWS Automation with CloudFormation

[![AWS](https://img.shields.io/badge/AWS-100000?style=flat&logo=amazon&logoColor=FFFFFF&labelColor=5C5C5C&color=FF7300)](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html)
[![CloudFormation](https://img.shields.io/badge/AWS_CloudFormation-100000?style=flat&logo=amazonaws&logoColor=white&labelColor=494949&color=FF7300)](https://aws.amazon.com/cloudformation/)


This section covers how to create a stack using AWS CloudFormation. In this demonstration, two stacks are created using a sample template. The first stack is created using the tutorial template provided, while the second stack is created using a modified version of the same template.

## Table of Contents

- [Requirements](#requirements)
- [Steps](#Steps)
- [Conclusion](#conclusion)
- [Contributors](#contributors)


## Requirements
To complete this quest, you will need an AWS account with access to the following services:
- Amazon CloudFormation

##  Step 1: Access the CloudFormation Service
In the AWS Management Console, navigate to the CloudFormation service. Here, you can create, manage, and delete CloudFormation stacks.

### Step 2: Create a Stack
Click the "Create Stack" button to create a new CloudFormation stack. Choose the sample template provided in the tutorial or upload your own template.

``` yaml
Resources:
  RobotAppServer:
    Type: 'AWS::EC2::Instance'
    Properties:
      InstanceType: t2.micro
      ImageId: ami-087c17d1fe0178315
      SecurityGroups:
        - !Ref RobotAppSecurityGroup

  RobotAppSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: Enable SSH access via port 22
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: 0.0.0.0/0

  RobotS3Bucket:
    Type: 'AWS::S3::Bucket'
    DeletionPolicy: Delete

```

### Step 3: Modify the Stack
If you choose to upload your own template, modify the stack as needed. In this demonstration, the template is modified to create a smaller EC2 instance type.

### Step 4: Preview the Stack
Before creating the stack, preview the changes that will be made by the template. This will help you identify any potential issues or errors before the stack is created.

### Step 5: Create the Stack for DIY
After reviewing the changes, create the stack. AWS CloudFormation will then create the resources defined in the template, including EC2 instances, security groups, and S3 buckets.

``` yaml
Resources:
  RobotAppServer:
    Type: 'AWS::EC2::Instance'
    Properties:
      InstanceType: t2.small
      ImageId: ami-087c17d1fe0178315
      SecurityGroups:
        - !Ref RobotAppSecurityGroup

  RobotAppSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: Enable SSH access via port 22
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: 0.0.0.0/0

  RobotS3Bucket:
    Type: 'AWS::S3::Bucket'
    DeletionPolicy: Delete

```


## Conclusion
By completing this demonstration, you should have a basic understanding of how to create a stack using AWS CloudFormation. You should also be familiar with the sample template provided and how to modify it to fit your needs. With CloudFormation automation, you can easily deploy and manage AWS resources at scale.

## Contributors

[Daniele Bocchino](https://danielebocchino.github.io/)

[![GitHub Followers](https://img.shields.io/github/followers/DanieleBocchino?style=social)](https://github.com/DanieleBocchino)  
[![LinkedIn Connect](https://img.shields.io/badge/LinkedIn-Connect-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/daniele-bocchino-aa602a20b/)
