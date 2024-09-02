from aws_cdk import (aws_ec2 as ec2, aws_ecs as ecs,
                     aws_ecs_patterns as ecs_patterns)

        vpc = ec2.Vpc(self, "ErsiliaVpc", max_azs=3)     # default is all AZs in region

        cluster = ecs.Cluster(self, "ErsiliaCluster", vpc=vpc)

        ecs_patterns.ApplicationLoadBalancedFargateService(self, "ErsiliaFargateService",
            cluster=cluster,            # Required
            cpu=512,                    # Default is 256
            desired_count=6,            # Default is 1
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")),
            memory_limit_mib=2048,      # Default is 512
            public_load_balancer=True)  # Default is True
