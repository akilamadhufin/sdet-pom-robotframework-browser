pipeline {
    agent { label 'robot' }

    options {
        timestamps()
    }

    stages {
        stage('Install Dependencies') {
            steps {
                dir('openweather_api_automation') {
                    sh 'python3 -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run API Tests') {
            steps {
                dir('openweather_api_automation/developer_style_API_testing') {
                    withCredentials([string(credentialsId: 'openweather_api_key', variable: 'OpenWeather_API_KEY')]) {
                        sh 'python3 -m robot -i smoke -L INFO -d results TestCases'
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                step([
                    $class: 'RobotPublisher',
                    outputPath: 'openweather_api_automation/developer_style_API_testing/results',
                    outputFileName: '*.xml',
                    disableArchiveOutput: false,
                    passThreshold: 100,
                    unstableThreshold: 95.0,
                    otherFiles: '*, **/*.png'
                ])
                archiveArtifacts artifacts: 'openweather_api_automation/developer_style_API_testing/results/**', allowEmptyArchive: true, fingerprint: true
            }
        }
        success {
            slackSend(
                channel: 'C0C00AD2TNZ',
                color: 'good',
                failOnError: false,
                message: "API-Testing-Pipeline SUCCESS - View log.html: ${env.BUILD_URL}artifact/openweather_api_automation/developer_style_API_testing/results/log.html"
            )
        }
        failure {
            slackSend(
                channel: 'C0C00AD2TNZ',
                color: 'danger',
                failOnError: false,
                message: "API-Testing-Pipeline FAILED - Check console: ${env.BUILD_URL}console"
            )
        }
    }
}
