pipeline {
    agent { label 'docker-agent' }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run tests via tox') {
            steps {
                script {
                    docker.image('basic-swt-rf:latest').inside {
                        sh 'tox'
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
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
