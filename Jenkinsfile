pipeline {

    agent any

    stages {

        stage('Checkout Source Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'pip install pytest-html'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest -vs --html=reports/report.html --self-contained-html'
            }
        }
    }
}
