pipeline {
    agent any

    environment {
        PIP_REQUIREMENTS = 'psycopg2-binary SQLAlchemy pandas openpyxl'
        PYTHON_HOME = 'C:/Users/cvsam/AppData/Local/Programs/Python/Python311/python.exe'
        PATH = "${PYTHON_HOME};${env.PATH}"
    }


    stages {
        stage('Setup Python Environment') {
            steps {
                // Install necessary Python packages
                //sh 'pip install ${PIP_REQUIREMENTS}'
                bat "${env.PYTHON_HOME} -m pip install --upgrade pip"
                bat "${env.PYTHON_HOME} -m pip install %PIP_REQUIREMENTS%"
            }
        }
        stage('Insert Data') {
            steps {
                script {
                    bat "${env.PYTHON_HOME} insert.py"
                }
            }
        }
        stage('Generate Excel Sheet') {
            steps {
                script {
                    bat "${env.PYTHON_HOME} read.py"
                }
            }
        }
        stage('Upload to JFrog Artifactory') {
            steps {
                script {
                    
                    bat """
                        C:/artifactory-pro-7.23.3/jf.exe rt u "C:/ProgramData/Jenkins/.jenkins/workspace/postgresql/*" "Generic-repo/" --url=http://localhost:8082/artifactory/ --user=admin --password=Akash@22 --server-id=artifactory1
                    """
                }
            }
        }
    }
}
