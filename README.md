# Ersilia.io Assignment

Container deployment was done with two options

OPTION 1 - DIRECTLY TO EC2

Steps involved:

1) Create VPC;
2) Create IAM Roles for:
  a) A non-root user with access rights to create and manage resources;
  b) A dedicated EC2 user to execute tasks inside the instance.
3) Create Security Group(s);
4) Create Networking Resources:
  a) Network Interface;
  b) Subnet(s).
5) AZs.

Once deployed, the container can be pulled and run using the following steps:

0) Login to the the EC2 instance by executing "from a local machine":

$ ssh -i "resilia-key-pair.pem" ec2-user@ec2-3-133-12-163.us-east-2.compute.amazonaws.com

(replace the IP adderess with the relevant one that can be obtained from the Networking tab found in the instance Console).

1) The EC2 IAM user has to be root to perform Docker tasks:

$ sudo su

2) List available containers:

$ docker ps

3a) If the desired image is available, execute:

$ docker run -d -p 80:80 --name ersiliaos/eos3b5e

3b) If not, pull the image and then run:

$ docker pull ersiliaos/eos3b5e

$ docker ps

$ docker run -d -p 80:80 --name ersiliaos/eos3b5e

These steps can be placed in a script to be run at EC2 instance startup time.

Refer to:

startup_script.py.

### Setting Up the Startup Script:
1. **Save the Script**: Save the above script as `startup_script.py`.
2. **Make the Script Executable**:
   ```bash
   chmod +x startup_script.py
   ```
3. **Configure EC2 Instance**:
   - Use the EC2 User Data feature to run this script at instance launch. You can add the following to the User Data section when launching an EC2 instance:

   ```bash
   #!/bin/bash
   yum update -y
   yum install -y docker
   service docker start
   # Replace the following line with the path to your startup script
   python3 /path/to/startup_script.py.

4) Test if the image "locally":

$ curl -X POST "http://localhost/info" -H "accept: */*" -H "Content-Type: application/json" -d "{}"

$ curl -X POST "http://localhost/run" -H "accept: */*" -H "Content-Type: application/json" -d "[{\"input\":\"CC(=O)OC1=CC=CC=C1C(=O)O\"}]"

5) Test if the image is available on the public internet by executing the following from a local machine, i.e. NOT from within the created EC2 instance:

$ curl -X POST "http://ec2-3-133-12-163.us-east-2.compute.amazonaws.com/run" -H "accept: */*" -H "Content-Type: application/json" -d "[{\"input\":\"CC(=O)OC1=CC=CC=C1C(=O)O\"}]"

This call can be made using the .py file provided by executing:

$ python3 ./molmass.py


OPTION 2 - CLUSTERED INFRASTRUCTURE USING ECS AND FARGATE

Refer to cdk stack.


# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
