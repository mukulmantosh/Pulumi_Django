# IaaC using Django & Pulumi
<br>

![stack_logo](./misc/images/pulumi_automation.png)

## Prerequisites 

Before starting up this project, make sure you have an AWS account.

### Software Installation

- [x] [AWS Command Line Interface](https://aws.amazon.com/cli/) - The AWS Command Line Interface (CLI) is a unified tool to manage your AWS services.


- [x] [Pulumi](https://www.pulumi.com/) - Universal Infrastructure as Code


## Python Dependencies

- Installing Python Packages

```bash

$ pip install -r requirements.txt

```

## Pulumi Stack

Login to Pulumi and create a new project.

Make sure to name the stack as **aws-python**.


![step1](./misc/images/step1.png)


Update the respective YAML files & django settings in the codebase.

**Pulumi.yaml**

![step2](./misc/images/step2.png)

**settings.py**

![step3](./misc/images/step3.png)


## Pulumi CLI

Run the below command :
- **pulumi login**

![step4](./misc/images/step4.png)




## References

If you are interested to know more about Pulumi.

- [Developing Serverless APIs using AWS Toolkit](https://www.jetbrains.com/pycharm/guide/tutorials/intro-aws/)
- [Developing Django Application using AWS NICE DCV, high-performance remote desktop and application streaming](https://www.jetbrains.com/pycharm/guide/tutorials/django-aws/) 