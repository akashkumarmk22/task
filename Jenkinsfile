pipeline {
    agent any
 
    tools {
        python 'Python3'  // This should match the name you configured in Jenkins
    }
 
    environment {
        PIP_REQUIREMENTS = 'pandas openpyxl'
    }
 
    stages {
        stage('Checkout') {
            steps {
                // Checkout the Git repository
                git 'https://github.com/akashkumarmk22/task.git'
            }
        }
 
        stage('Setup Python Environment') {
            steps {
                // Install necessary Python packages
                sh 'pip install ${PIP_REQUIREMENTS}'
            }
        }
 
        stage('Execute Python Script') {
            steps {
                // Execute the Python script
                sh 'python3 acchu.py'
            }
        }
 
        stage('Send Email') {
            steps {
                // Send an email (this assumes you have email configured in Jenkins)
                mail to: 'akashkumarmk02@gmail.com',
                     subject: 'Jenkins Job Notification',
                     body: 'The Python script has been executed and the Excel file has been created.'
            }
        }
    }
 
    post {
        always {
            // Archive the created Excel file
            archiveArtifacts artifacts: 'student_data.xlsx'
        }
    }
}