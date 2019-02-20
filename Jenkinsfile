pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Showing env...'
                sh 'env'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
