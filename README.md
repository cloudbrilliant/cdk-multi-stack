# AWS CDK - Using multiple stacks in a single CDK project

AWS CDK, a framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation.

After learning the basics of CDK, you will quickly reach a point when you will want archiecture and structure your app using one or more CDK stacks within a single CDK project.

Here is basic example of branching out into multiple stacks within the same CDK project.

- CdkMultiStackStack
- CdkMultiStackStack2

Deploy all stacks

```bash
cdk deploy --require-approval never --all
```

Deploy a specific stack

```bash
cdk deploy --require-approval never CdkMultiStackStack2
```

## Resources

- [https://docs.aws.amazon.com/cdk/v2/guide/home.html](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
- [https://docs.aws.amazon.com/cdk/api/v2/python/index.html](https://docs.aws.amazon.com/cdk/api/v2/python/index.html)
- [https://github.com/aws/aws-cdk](https://github.com/aws/aws-cdk)

---

## Welcome to your CDK Python project (boiler plate)

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
