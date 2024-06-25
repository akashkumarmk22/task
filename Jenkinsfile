pipeline {
    agent any
 
    environment {
        PIP_REQUIREMENTS = 'pandas openpyxl'
        PYTHON_HOME = 'C:/python.exe'
        PATH = "${PYTHON_HOME};${env.PATH}"
	JFROG_CLI_HOME = 'C:/artifactory-pro-7.23.3/jf.exe'  // Update with the path to jfrog executable
        ARTIFACTORY_SERVER_ID = 'artifactory1'
        ARTIFACTORY_REPO = 'Generic-repo1'  // Your Artifactory repository name
	ARTIFACTORY_USER = 'admin'
	    FilePath = 'C:/ProgramData/Jenkins/.jenkins/workspace/pythonProject1'
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
                // Install necessary Python package
		bat "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py"
                bat "${env.PYTHON_HOME} get-pip.py"
                bat "${env.PYTHON_HOME} -m pip install --upgrade pip"
                bat "${env.PYTHON_HOME} -m pip install openpyxl"
                bat "${env.PYTHON_HOME} -m pip install matplotlib"
                //bat "%PYTHON_HOME% -m pip install --upgrade pip"
                //bat "%PYTHON_HOME% -m pip install %PIP_REQUIREMENTS%"
            }
        }
 
        stage('Execute Python Script') {
            steps {
                // Execute the Python script
		bat "${env.PYTHON_HOME} pythonfile.py"
                //bat '%PYTHON_HOME% pythonfile.py'
            }
        }
		
		stage('Upload to JFrog Artifactory') {
            steps {
                script {
                    try {
                        // Upload the Excel file to Artifactory
                        bat "%JFROG_CLI_HOME% rt u 'FilePath' %ARTIFACTORY_REPO%/student_data.xlsx --server-id=%ARTIFACTORY_SERVER_ID%"
                    } catch (Exception e) {
                        echo "Upload to Artifactory failed: ${e}"
                        currentBuild.result = 'FAILURE'
                        error("Stopping pipeline due to upload failure.")
                    }
                }
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
                                to: 'akashkumarmk300@gmail.com',
                                replyTo: 'akashkumarmk02@gmail.com',  // Specify your email address here
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
    }
    post {
        always {
            // Archive the created Excel file
            archiveArtifacts artifacts: 'student_data.xlsx'
        }
    }
}