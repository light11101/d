pipeline {
    agent any
    environment {
        IMAGE_NAME      = "myapp"
        DOCKER_HUB_USER = "<username>" //change
    }
    stages {
        stage('Clone') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/<username>/flask-app.git' //change
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -t $DOCKER_HUB_USER/$IMAGE_NAME:latest .'
            }
        }
        stage('Push to Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                      echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                      docker push $DOCKER_HUB_USER/$IMAGE_NAME:latest
                    '''
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5200:5000 $DOCKER_HUB_USER/$IMAGE_NAME:latest'
            }
        }
    }
}
