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
                bat '"C:\\Users\\Akshayyy\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'
                bat '"C:\\Users\\Akshayyy\\AppData\\Local\\Python\\bin\\python.exe" -m pip install pytest-html'
                bat '"C:\\Users\\Akshayyy\\AppData\\Local\\Python\\bin\\python.exe" -m pip install allure-pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\Akshayyy\\AppData\\Local\\Python\\bin\\python.exe" -m pytest -vs --html=reports/report.html --self-contained-html --alluredir=allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat '"C:\\Users\\Akshayyy\\Downloads\\allure-2.42.1\\allure-2.42.1\\bin\\allure.bat" generate allure-results --clean -o allure-report'
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure(
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                )
            }
        }
    }

    post {

        always {

            archiveArtifacts artifacts: 'reports/**, screenshots/**, logs/**, allure-report/**',
                             allowEmptyArchive: true

            publishHTML([
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Pytest Automation Report'
            ])
        }

        success {
            echo 'Automation Execution Completed Successfully'
        }

        failure {
            echo 'Some Test Cases Failed'
        }
    }
}