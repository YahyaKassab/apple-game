// pipeline {
//     agent any
    
//     stages {
//         stage('Build') {
//             steps {
//                 // Your build steps here
//                 echo 'Building...'
//             }
//         }
        
//         stage('Test') {
//             steps {
//                 // Your test steps here
//                 echo 'Testing...'
//             }
//         }
        
//         stage('Deploy') {
//             steps {
//                 // Your deployment steps here
//                 echo 'Deploying...'
//             }
//         }
//     }
    
//     post {
//         success {
//             echo 'Pipeline succeeded! Send notifications, etc.'
//         }
//         failure {
//             echo 'Pipeline failed! Send notifications, etc.'
//         }
//     }
// }
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Define your build steps here
                echo 'Building the project...'
            }
        }

        stage('Test') {
            steps {
                // Define your test steps here
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                // Define your deployment steps here
                echo 'Deploying the application....'
            }
        }
    }
}