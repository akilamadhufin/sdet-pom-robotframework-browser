pipeline {
    // Run only on the Jenkins agent with the "robot" label.
    // This agent must have Python, Node.js/npm, and Xvfb installed.
    agent { label 'robot' }

    options {
        // Show a timestamp beside every console-log line.
        timestamps()

        // Avoid two builds registering/deleting the same test account at once.
        disableConcurrentBuilds()
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                    # Update pip, then install Python test dependencies.
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt

                    # Download/install Playwright browsers required by
                    # robotframework-browser.
                    python3 -m rfbrowser init
                '''
            }
        }

        stage('Run Robot Framework tests') {
            steps {
                sh '''
                    # Ensure the Robot Framework output directory exists.
                    mkdir -p results

                    # Run Chromium using a virtual display because the current
                    # UI test starts the browser in headed (non-headless) mode.
                    xvfb-run -a python3 -m robot \
                      --loglevel INFO \
                      --outputdir results \
                      TestCases
                '''
            }
        }
    }

    post {
        always {
            // Publish Robot Framework results even if the test fails.
            // Requires the Jenkins Robot Framework plugin.
            robot(
                outputPath: 'results',
                outputFileName: 'output.xml',
                disableArchiveOutput: false,
                passThreshold: 100.0,
                unstableThreshold: 95.0,
                otherFiles: '*.png, playwright-log.txt'
            )

            // Keep raw Robot reports, logs, screenshots, and Playwright logs
            // as downloadable artifacts for each build.
            archiveArtifacts(
                artifacts: 'results/**',
                allowEmptyArchive: true,
                fingerprint: true
            )
        }
    }
}