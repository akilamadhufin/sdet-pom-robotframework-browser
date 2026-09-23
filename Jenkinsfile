pipeline {
    agent { label 'robot' }

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {

        stage('Install project') {
            steps {
                sh '''
                    # Install your project (pyproject.toml)
                    python3 -m pip install --upgrade pip
                    pip install .
                '''
            }
        }

        stage('Run tests via tox') {
            steps {
                sh '''
                    # Run everything through tox
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
