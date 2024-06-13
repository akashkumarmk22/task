pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                checkout scmGit(branches: [[name: '*/new']], extensions: [], userRemoteConfigs: [[credentialsId: 'githubtoken', url: 'https://github.com/akashkumarmk22/task.git']])
            }
        }
        stage('Build'){
            steps {
                git branch: 'new', credentialsId: 'githubtoken', url: 'https://github.com/akashkumarmk22/task.git'
                
            }
        }
    }
}