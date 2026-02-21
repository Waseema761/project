pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t healthcare-app:latest .'
            }
        }

        stage('Deploy Healthcare App') {
            steps {
                sh '''
                docker rm -f healthcare-container >/dev/null 2>&1 || true

                docker run -d \
                --name healthcare-container \
                --network healthcare-net \
                -p 5000:5000 \
                healthcare-app:latest
                '''
            }
        }
    }
}
