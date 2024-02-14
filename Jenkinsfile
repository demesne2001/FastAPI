
pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
               checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'demesne2001', url: 'https://github.com/demesne2001/FastAPI.git']])
                echo 'checkout done'
            }
        }
        stage('requirements install') {
            steps {
                script{
                    bat 'pip install -r requirements.txt'
                }
                echo 'requirements install done'
            }
        }
        stage('Project build') {
            steps {
                script{
                    bat 'uvicorn index:app --host 127.0.0.1 --port 2023'
                }
                echo 'Project startted'
            }
        }
        stage('Reload Server') {
            steps {
                script{
                    bat 'cd c:\\nginx-1.24.0'
                    bat 'nginx -s reload'
                    
                }
                echo 'Project startted'
            }
        }
    }
}