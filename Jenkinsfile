pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:/Users/Akash M K/AppData/Local/Programs/Python/Python311/python.exe'
        PATH = "${PYTHON_HOME};${env.PATH}"
    }
    stages {
        stage('Execute Python Script') {
            steps {
                script {
                    bat "${env.PYTHON_HOME} hello.py"
                }
            }
        }
    }
}