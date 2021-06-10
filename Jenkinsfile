pipeline{
    agent any
    environment{
        DATABASE_URI = credentials("DATABASE_URI")
      
    }
    stages{
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
                sh 'echo build'
            }
        }
        stage("Push"){
            steps{
                //install docker and docker-compose
                //docker-compose push
                sh 'echo push'
            }
        }
        stage("Configuration Management (Ansible)"){
            steps{
                //install ansible on jenkins machine for Jenkins user
                //ansible-playbook -i inventory.yaml playbook.yaml
                sh 'echo config'
            }
        }
        stage("Deploy"){
            steps{
                //create swarm
                //copy over docker-compose.yaml
                //
                // ssh: docker stack deploy --compose-file docker-compose.yaml character_gen
                //sh "bash jenkins/deploy_stack.sh"
                sh 'echo deploy'

            }
        }
    }
}