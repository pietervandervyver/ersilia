import subprocess
import sys

def check_image_exists(image_name):
    """Check if a Docker image exists locally."""
    try:
        result = subprocess.run(['docker', 'images', '-q', image_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.strip() != b''
    except Exception as e:
        print(f"Error checking for Docker image: {e}")
        sys.exit(1)

def pull_docker_image(image_name):
    """Pull the specified Docker image."""
    try:
        print(f"Pulling Docker image: {image_name}")
        subprocess.run(['docker', 'pull', image_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error pulling Docker image: {e}")
        sys.exit(1)

def run_docker_image(image_name):
    """Run the specified Docker image."""
    try:
        print(f"Running Docker image: {image_name}")
        subprocess.run(['docker', 'run', '-d', image_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Docker image: {e}")
        sys.exit(1)

def main():
    image_name = "ersiliaos/eos3b5f"
    
    if check_image_exists(image_name):
        print(f"Docker image {image_name} found.")
        run_docker_image(image_name)
    else:
        print(f"Docker image {image_name} not found. Pulling it now...")
        pull_docker_image(image_name)
        run_docker_image(image_name)

if __name__ == "__main__":
    main()
```

### Explanation:
1. **check_image_exists**: This function checks if the specified Docker image exists locally by running the `docker images -q <image_name>` command.
2. **pull_docker_image**: This function pulls the specified Docker image from Docker Hub using the `docker pull` command.
3. **run_docker_image**: This function runs the Docker image using the `docker run -d <image_name>` command. The `-d` flag runs the container in detached mode.
4. **main**: This is the main function that orchestrates the check, pull, and run operations.

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
   python3 /path/to/startup_script.py