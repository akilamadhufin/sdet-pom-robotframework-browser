pipeline {
    agent {
        docker {
            image 'basic-swt-rf:latest'
            args '-u root'
        }
    }

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install project') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip install .
                '''
            }
        }

        stage('Run tests via tox') {
            steps {
                sh '''
                    tox
                '''
            }
        }
    }

    post {
        always {
            robot(
                outputPath: 'results',
                outputFileName: 'output.xml',
                disableArchiveOutput: false,
                passThreshold: 100.0,
                unstableThreshold: 95.0,
                otherFiles: '*.png, playwright-log.txt'
            )

            archiveArtifacts(
                artifacts: 'results/**',
                allowEmptyArchive: true,
                fingerprint: true
            )
        }
    }
}
