pipeline {
    agent any

    environment {
        VENV = 'venv'
        BUILD_NAME = 'flask-app-build'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                . $VENV/bin/activate
                pytest test_app.py --junitxml=test-results.xml
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                mkdir -p build
                zip -r build/${BUILD_NAME}.zip app.py requirements.txt
                '''
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'
            archiveArtifacts artifacts: 'build/*.zip', fingerprint: true
        }
        success {
            echo 'Build and tests completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
