pipeline{
    agent {label 'linux'}

    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
    }
    stages{
        stage('gitclone') {
            steps {
                git 'https://github.com/coder9a/TextUtils-Django-App'
            }
        }
        stage('Build'){
            steps{
                sh 'docker build -t coder9a/textutils:latest .'
            }
        }
        stage('login'){
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR ----password-stdin'
            }
        }
        stage('Push to DockerHub'){
            steps{
                sh 'docker push coder9a/textutils:latest'
            }
        }
    }
    post{
        always{
            sh 'docker logout'
        }
    }
}