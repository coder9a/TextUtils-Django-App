pipeline{

    environment {
        registry = "coder9a/textutils"
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
    agent any
    stages{
        stage('Clone git repo') {
            steps {
                git 'https://github.com/coder9a/TextUtils-Django-App'
            }
        }
        stage('Build the image'){
            steps{
                script{
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Deploy the image to Dockerhub'){
            steps{
                script{
                    docker.withRegistry('', registryCredential){
                        dockerImage.push()
                    }
                }
            }
        }
        syage('Cleaning up'){
            steps{
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
    }
}
