pipeline {
    agent {
        docker { image 'python:2-alpine' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
    }
}
