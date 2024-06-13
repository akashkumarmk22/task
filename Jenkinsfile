pipeline {
    agent any
 
    environment {
        PIP_REQUIREMENTS = 'pandas openpyxl'
        PYTHON_HOME = 'C:\\Python39\python.exe'
    }
 
    stages {
        stage('Checkout') {
            steps {
                // Checkout the Git repository
                git url: 'https://github.com/akashkumarmk22/task.git', branch: 'new'
            }
        }
 
        stage('Setup Python Environment') {
            steps {
                // Install necessary Python packages
                //sh 'pip install ${PIP_REQUIREMENTS}'
                bat "${PYTHON_HOME} -m pip install -- upgrade pip"
                bat "${PYTHON_HOME} -m pip install ${PIP_REQUIREMENTS}"
            }
        }
 
        stage('Execute Python Script') {
            steps {
                // Execute the Python script
                bat '${PYTHON_HOME} acchu.py'
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