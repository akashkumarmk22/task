pipeline {
    agent any
 
    environment {
        PIP_REQUIREMENTS = 'pandas openpyxl'
        PYTHON_HOME = 'C:/Users/cvsam/AppData/Local/Programs/Python/Python311/python.exe'
        PATH = "${PYTHON_HOME};${env.PATH}"
	    JFROG_CLI_HOME = 'C:/artifactory-pro-7.23.3/jf.exe'  // Update with the path to jfrog executable
        ARTIFACTORY_SERVER_ID = 'artifactory1'
        ARTIFACTORY_REPO = 'Generic-repo1'  // Your Artifactory repository name
	    ARTIFACTORY_CREDENTIALS_USR = 'admin'
	    //FilePath = 'C:/ProgramData/Jenkins/.jenkins/workspace/Artifactory'
        //ARTIFACTORY_URL = 'http://localhost:8082/artifactory/Generic-repo1/'
       // ARTIFACTORY_CREDENTIALS_PSW = credentials('c0f24f0f-6965-476a-a300-1f64b4076b02')
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
                bat '''
                    SET PATH=%PATH%;C:/Scripts
                    C:/Users/cvsam/AppData/Local/Programs/Python/Python311/python.exe -m pip install --upgrade pip
                '''
                //bat "${env.PYTHON_HOME} -m pip install --upgrade pip"
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
                    
                    bat """
                        C:/artifactory-pro-7.23.3/jf.exe rt u "C:/ProgramData/Jenkins/.jenkins/workspace/Artifactory/*" "Generic-repo1/" --url=http://localhost:8082/artifactory/ --user=admin --password=Akash@22 --server-id=artifactory1
                    """
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