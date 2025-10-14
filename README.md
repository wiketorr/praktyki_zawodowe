# Praktyki zawodowe

## Project setup

1. Fetch the project from the repository:
   1. You need to have git installed first. You can find it here https://git-scm.com/downloads
   2. On the repository click the green "code" button and select https
   3. Copy the https link and open your terminal
   4. Navigate to where you want the project saved
   5. Type and run this command: git clone /your https link/ 
2. Build and run the docker container: 
   1. You will need a docker engine for this step. You can learn more here https://docs.docker.com/
   2. Type and run this command ```docker compose up```. This will build the image if it is not present on your machine and start it

## Dependency management
In order to install a new library use a makefile command.

1. To add a production dependency use ```make add``` and follow the prompts
2. To add a dev dependency use ```make add-dev``` and follow the prompts
3. To remove a dependency use ```make remove``` and ```make remove-dev``` respectively
