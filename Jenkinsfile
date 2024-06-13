pipeline {
    agent any
 
    environment {
        PIP_REQUIREMENTS = 'pandas openpyxl'
        PYTHON_HOME = 'C:/Python39/python.exe'
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
                bat "%PYTHON_HOME% -m pip install --upgrade pip"
                bat "%PYTHON_HOME% -m pip install %PIP_REQUIREMENTS%"
            }
        }
 
        stage('Execute Python Script') {
            steps {
                // Execute the Python script
                bat '%PYTHON_HOME% acchu.py'
            }
        }
 
        stage('Send Email') {
            steps {
                script {
                    def retries = 3
                    def success = false
                    for (int i = 0; i < retries; i++) {
                        try {
                            emailext (
                                subject: "Jenkins Job Notification",
                                body: "The Python script has been executed and the Excel file has been created.",
                                to: 'user@example.com',
                                replyTo: 'akashkumarmk300@gmail.com',  // Specify your email address here
                                mimeType: 'text/html',
                                attachLog: true
                            )
                            success = true
                            break
                        } catch (Exception e) {
                            echo "Email sending failed on attempt ${i + 1}: ${e}"
                            sleep 30  // Wait for 30 seconds before retrying
                        }
                    }
                    if (!success) {
                        currentBuild.result = 'FAILURE'
                        error("Failed to send email after ${retries} retries.")
                    }
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