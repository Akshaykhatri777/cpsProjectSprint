pipeline {

```
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

post {

    always {

        archiveArtifacts artifacts: 'reports/**, screenshots/**, logs/**',
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
        echo 'Build Successful'
    }

    failure {
        echo 'Build Failed'
    }
}
```

}
