pipeline{
    agent any
    environment{
        DATABASE_URI = credentials("DATABASE_URI")
        DOCKER_USERNAME = credentials("DOCKER_USERNAME")
        DOCKER_PASSWORD = credentials("DOCKER_PASSWORD")
      
    }
    stages{
        stage("Requirements"){
            steps{
                sh 'bash jenkins/install-requirements.sh'
            }
        }

        stage("Test"){
            steps{
                //pytest
                //run for each service
                //produce cov reports
                sh 'bash jenkins/test.sh'
            }
        }
        stage("Build"){
            steps{
                //docker-compose build
                sh 'docker-compose down'
                sh 'docker system prune --force --all'
                sh 'docker-compose build'
            }
        }
        stage("Push"){
            steps{
                //install docker and docker-compose
                //docker-compose push
                sh 'docker-compose push'
            }
        }
        stage("Configuration Management (Ansible)"){
            steps{
                //install ansible on jenkins machine for Jenkins user
                sh 'cd ansible && ~/.local/bin/ansible-playbook -i inventory.yaml playbook.yaml'
            }
        }
        stage("Deploy"){
            steps{
                //create swarm
                //copy over docker-compose.yaml
                //
                // ssh: docker stack deploy --compose-file docker-compose.yaml character_gen
                sh 'bash jenkins/deploy_stack.sh'

            }
        }
    }
}